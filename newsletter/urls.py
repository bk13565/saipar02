from django.urls import path, include
from .views import SubscriberCreateView, SubscriberConfirmView, SubscriberDeleteView

app_name = "newsletter"

urlpatterns = [
	path('new/', SubscriberCreateView.as_view(), name="new-subscriber"),
 	path('confirm/', SubscriberConfirmView.as_view(), name="confirm-subscriber"),
    path('confirm/', SubscriberDeleteView.as_view(), name="delete-subscriber")  
]
