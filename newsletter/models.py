from django.db import models

from django.conf import settings
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient

# Create your models here.
class NewsletterSubscriber(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, unique=True)
    conf_num = models.CharField(max_length=15) # a confirmation number (for valid email addresses)
    confirmed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-created_on"]
    
    # def __str__(self):
    #     return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return  self.name + ":" + self.email + " (" + ("not " if not self.confirmed else "") + "confirmed)"
    
class Newsletter(models.Model):
    subject = models.CharField(max_length=100)
    contents = models.FileField(upload_to='saipar_files/saipar_newsletters')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
     
    def __str__(self):
        return self.subject + self.created_on.strftime("%Y-%m-%d")
    
    # sending the newslwetter to all subscribers
    def send(self, request):
        contents = self.contents.read().decode('utf-8')
        subscribers = NewsletterSubscriber.objects.filter(confirmed=True)
        send_grid = SendGridAPIClient(settings.SENDGRID_API_KEY)
        for sub in subscribers:
            message = Mail(
                    from_email=settings.FROM_EMAIL,
                    to_emails=sub.email,
                    subject=self.subject,
                    html_content=contents + (
                        '<br><a href="{}/delete/?email={}&conf_num={}">Unsubscribe</a>.').format(
                            request.build_absolute_uri('/delete/'),
                            sub.email,
                            sub.conf_num))
            send_grid.send(message)