from django.urls import path
from app_blog import  views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('about/', views.AboutView.as_view(), name="about"),
    path('home/', views.PostListView.as_view(), name='home'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name="detail"),
    path('post/create/', login_required(views.CreatePostView.as_view()), name="create"),
    path('post/<int:pk>/update/', login_required(views.UpdatePostView.as_view()), name="update"),
    path('post/<int:pk>/delete/', login_required(views.DeletePostView.as_view()), name="delete"),
    path('post/draft', login_required(views.DraftListView.as_view()), name="draft"),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment'),
    path('post/<int:pk>/arpove', views.comment_approve, name='comment_approve'),
    path('post/<int:pk>/delete', views.commnet_remove, name='comment_remove'),
    path('post/<int:pk>/publish', views.post_pusblish, name='post_publish')
]