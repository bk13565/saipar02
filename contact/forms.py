from django import forms

class ContactForm(forms.Form):
    email_address = forms.EmailField(max_length=254, required=False)
    name = forms.CharField(max_length=50, required=True)
    subject = forms.CharField(max_length=100, required=False)
    message = forms.CharField(widget=forms.Textarea, max_length=2000, required=True)

