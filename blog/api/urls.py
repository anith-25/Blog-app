from django.urls import path
from .views import BlogListAPIView, BlogDetailAPIView, BlogCreateAPIView, BlogUpdateAPIView, BlogDeleteAPIView

urlpatterns = [
    path("blogs/", BlogListAPIView.as_view(), name="blog_list_api"),
    path("blogs/<int:pk>/", BlogDetailAPIView.as_view(), name="blog_detail_api"),
    path("blogs/create/", BlogCreateAPIView.as_view(), name="blog_create_api"),
    path("blogs/<int:pk>/update/", BlogUpdateAPIView.as_view(), name="blog_update_api"),
    path("blogs/<int:pk>/delete/", BlogDeleteAPIView.as_view(), name="blog_delete_api")
]
