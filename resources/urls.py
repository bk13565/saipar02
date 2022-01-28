from django.urls import path
from .views import EventListView


app_name = "resources"

urlpatterns = [
    path("", EventListView.as_view(), name="event-list"),   
]