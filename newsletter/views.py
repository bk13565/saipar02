from django.shortcuts import render, redirect, reverse
from django.views import generic
from .forms import NewsletterForm
import random
from django.views.decorators.csrf import csrf_exempt
from .models import NewsletterSubscriber
from sendgrid.helpers.mail import Mail
from django.conf import settings
from sendgrid import SendGridAPIClient

class SubscriberCreateView(generic.CreateView):
    template_name = "newsletter/subscriber_create.html"
    form_class = NewsletterForm
    
    def get_success_url(self):
        return reverse("newsletter:new-subscriber")
    
    #generate random number for confirmation code
    def random_digits(self):
        return "%0.12d" % random.randint(0, 999999999999)
 
    @csrf_exempt
    def new_subscriber(self, request):
        if request.method == "POST":
            subscriber = NewsletterSubscriber(email=request.POST['email'], 
                                            conf_num=self.random_digits())
            subscriber.save()
            message = Mail(
                from_email=settings.FROM_EMAIL,
                to_emails=subscriber.email,
                subject="Newsletter SignUp Confirmation",
                html_content='Thank you for signing up for SAIPAR newsletter! \
                    Please complete the process by \
                    <a href="{}/confirm/?email={}&conf_num={}"> clicking here to \
                    confirm your registration</a>.'.format(request.build_absolute_uri('/confirm/'),
                                                        subscriber.email,
                                                        subscriber.conf_num), 
            )
            sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            response = sg.send(message)
            # print('sending email')
            # print(settings.SENDGRID_API_KEY)

            return (request, 'newsletter/subscriber_create.html', {'email': subscriber.email, 'action': 'added', 'form': NewsletterForm(),
                                                                   'message': 'Thanks for subscribing!'})
            # return redirect("newsletter:new-subscriber")
        # firsrt time page loading
        else:
            return render(request,'newsletter/subscriber_create.html' , {'form': NewsletterForm()})
        

class SubscriberConfirmView(generic.View):
    template_name = "newsletter/subscriber_confirm.html"
    form_class = NewsletterForm
    
    def get_success_url(self):
        return reverse("newsletter:confirm-subscriber")
    
    def confirm_new_subscriber(request):
        sub = NewsletterSubscriber.objects.get(email=request.GET['email'])
        if sub.conf_num == request.GET['conf_num']:
            sub.confirmed = True
            sub.save()
            return render(request, 'newsletter/subscriber_confirm.html', {'email': sub.email, 'action': 'confirmed'})
        else:
            return render(request, 'newsletter/subscriber_confirm.html', {'email': sub.email, 'action': 'denied'})

class SubscriberDeleteView(generic.DeleteView):
    template_name = "newsletter/subscriber_delete.html"
    form_class = NewsletterForm
    
    def get_success_url(self):
        return reverse("newsletter:delete-subscriber")
    
    def delete_subscriber(request):
        sub = NewsletterSubscriber.objects.get(email=request.GET['email'])
        if sub.conf_num == request.GET['conf_num']:
            sub.delete()
            return render(request, 'newsletter/subscriber_delete.html', {'email': sub.email, 'action': 'confirmed'})
        else:
            return render(request, 'newsletter/subscriber_delete.html', {'email': sub.email, 'action': 'denied'})
    
        
            
        