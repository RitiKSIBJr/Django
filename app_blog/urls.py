from django.urls import path
from . import  views

app_name = "app_blog"

urlpatterns = [
    path('about/', views.AboutView.as_view(), name="about"),
    path('home/', views.PostListView.as_view(), name='home'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name="detail"),
    path('post/create/', views.CreatePostView.as_view(), name="create"),
    path('post/<int:pk>/update/', views.UpdatePostView.as_view(), name="update"),
    path('post/<int:pk>/delete/', views.DeletePostView.as_view(), name="delete"),
    path('post/draft', views.DraftListView.as_view(), name="draft")
]