"""saipar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
from resources.views import HomepageView, AboutUsView, ZLIIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomepageView.as_view(), name='homepage'),
    path('aboutus/', AboutUsView.as_view(), name='aboutus'),
    path('zlii/', ZLIIView.as_view(), name='zlii'),
    path('contact-us/', include('contact.urls', namespace="contact")),
    path('blog/', include('blog.urls', namespace="blog")),
    path('newsletter/', include('newsletter.urls', namespace="newsletter")),
    path('events&resources/', include('resources.urls', namespace="resources")),
    path('people/', include('people.urls', namespace="people")),
    path('programs/', include('programs.urls', namespace="programs")),
    path('publications/', include('pubs.urls', namespace="publications")),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)