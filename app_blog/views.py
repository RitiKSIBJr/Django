from django.shortcuts import render
from .models import Comment, Post
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import PostForm, CommentFrom
from django.views.generic import (CreateView, 
                                    DeleteView, 
                                    DetailView, 
                                    FormView, 
                                    UpdateView,
                                    TemplateView,
                                    ListView)

# Create your views here


#------------HOME----------------------------------------
class PostListView(ListView):

    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


#---------------BLOG-------------------------
class PostDetailView(DetailView):

    model = Post   


#-------------------ABOUT----------------------------------------
class AboutView(TemplateView):

    template_name = 'about.html'


#--------------------CREATE POST-----------------------------
class CreatePostView(CreateView, login_required):
    login_url = 'login/'
    redirect_field_name = 'post_detail.html'

    from_class = PostForm

    model = Post

#----------------UPDATE POST----------------------
class UpdatePostView(UpdateView, login_required):

    login_url = 'login/'
    redirect_field_name = 'post_detail.html'

    from_class = PostForm

    model = Post

#--------------DELETE POST--------------------
class DeletePostView(DeleteView, login_required):

    model = Post

    success_url = reverse_lazy('post_list')

class DraftListView(ListView, login_required):

    login_url = 'login/'
    redirect_field_name = 'post_list.html'

    model = Post

    def get_queryset(self):
        return  Post.objects.filter(published_date__isnull = True).order_by('creadted_date')