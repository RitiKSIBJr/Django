from django import forms
from .models import Post,Comment

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        widgets = {
            'author': forms.TextInput(attrs={'placeholder': 'Author Name', 'class': 'author'}),
            'title': forms.TextInput(attrs={'placeholder': 'Title', 'class': ' Title'}),
            'text': forms.Textarea(attrs={'placeholder':'Content', 'class': 'editable meduim-post-post contentpost'})
        }

class CommentFrom(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs={'placeholder': 'Author Name', 'class': 'author'}),
            'text': forms.Textarea(attrs={'placeholder':'Content', 'class': 'editable meduim-post-post contentpost'})
        }
