from django.urls import path, include
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostList.as_view(), name="blog_posts"),
    # path("/<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
    path("<int:pk>/", views.PostDetail.as_view(), name="post_detail"),
]