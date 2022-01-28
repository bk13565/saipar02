from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.views import generic
from django.conf import settings


from django.core.exceptions import ValidationError
# from django.core.validators import validate_email

# Create your views here.
class ContForm:

    def contact(self, request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                subject = form.cleaned_data['subject']
                # print(subject)
                email_address = form.cleaned_data['email_address']
                body = {
                'name': form.cleaned_data['name'], 
                'subject': form.cleaned_data['subject'],
                'message':form.cleaned_data['message'], 
                }
                message = "\n".join(body.values())

                try:
                    # status_code = send_mail(subject, message, settings.SAIPAR_EMAIL, settings.ADMIN_EMAILS, fail_silently=False) 
                    status_code = send_mail(subject, message, settings.SAIPAR_EMAIL, settings.ADMIN_EMAILS, fail_silently=False) 
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                
                context = {"status_code" : status_code}
                return render(request, "contact/contact.html", context)
                    
                # if status_code == 1:
                #     context = {'Message' : "Email successfully sent"}
                # else:
                #     context = {'Message' : "Your email wasn't delivered. Try sending it again"}
                # return redirect('contact:success')

        # new empty instance of the contact form
        form = ContactForm()
        return render(request, "contact/contact.html", {'form':form})
    
class ContactSuccessView(generic.TemplateView):
    template_name = 'contact/success.html'
    context_object_name = "success"