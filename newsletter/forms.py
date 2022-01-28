from django import forms
from .models import NewsletterSubscriber

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ('name', 'email')
        
# class NewletterForm(forms.Form):
#     name = forms.CharField(max_length=30)
#     email = forms.EmailField(max_length=40)