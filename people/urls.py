from django.urls import include, path
from rest_framework import routers
from .views import PeopleView, ResearchPeopleView, ResearchViewSet, StaffViewSet

# router = routers.DefaultRouter()
# router.register(r'heroes', views.HeroViewSet)

app_name = "people"

router2 = routers.DefaultRouter()
router2.register(r'staff', StaffViewSet)

router3 = routers.DefaultRouter()
router3.register(r'director', ResearchViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('staff', include(router2.urls)),
    # path('', include(router.urls)),
    # path('directors', include(router3.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', PeopleView.as_view(), name="staff-list"),
    path('research-members/', ResearchPeopleView.as_view(), name="research-members")
]