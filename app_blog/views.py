from django.shortcuts import render, get_object_or_404, redirect
from app_blog.models import Comment, Post
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from app_blog.forms import PostForm, CommentFrom
from django.views.generic import (CreateView, DeleteView, 
                                    DetailView, UpdateView,
                                    TemplateView, ListView)

# Create your views here


#------------HOME----------------------------------------
class PostListView(ListView):

    model = Post
    template_name = 'post_list.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


#---------------BLOG-------------------------
class PostDetailView(DetailView):

    model = Post   


#-------------------ABOUT----------------------------------------
class AboutView(TemplateView):

    template_name = 'about.html'


#--------------------CREATE POST-----------------------------

class CreatePostView(CreateView):
    login_url = 'login/'
    redirect_field_name = 'post_detail.html'

    form_class = PostForm

    model = Post
    template_name = 'post_form.html'

#----------------UPDATE POST----------------------

class UpdatePostView(UpdateView):

    login_url = 'login/'
    redirect_field_name = 'post_detail.html'

    from_class = PostForm

    model = Post

#--------------DELETE POST--------------------

class DeletePostView(DeleteView):

    model = Post

    success_url = reverse_lazy('post_list')


class DraftListView(ListView):

    login_url = 'login/'
    redirect_field_name = 'post_list.html'

    model = Post

    template_name = 'post_draft_list.html'

    def get_queryset(self):
        return  Post.objects.filter(published_date__isnull = True).order_by('created_date')


###########################################################################################
@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentFrom(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', pk = post.pk)

        else:
            form = CommentFrom()

        return render(request, 'comment_form.html', {'form':form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()

    return redirect('post_detail',pk=comment.post.pk)


@login_required
def commnet_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail.html', pk=post_pk)


@login_required
def post_pusblish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish
    return redirect('post_detail', pk=pk)