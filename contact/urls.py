from django.urls import path
from . import views
from .views import ContactSuccessView


app_name = "contact"
contact_form = views.ContForm()

urlpatterns = [
    path("", contact_form.contact, name="contact"), 
    path("success/", ContactSuccessView.as_view(), name="success")   
]

