from django.urls import path, include
from .views import PublicationsView


app_name = "pubs"

urlpatterns = [
    path("", PublicationsView.as_view(), name="pubs" ),
]