from django import forms
from .models import Post

class CreatePostForm(forms.ModelForm):
    post_content = forms.CharField(widget=forms.Textarea(attrs={

    }),
    label="Content",
    max_length=5000)

    class Meta:
        model = Post
        fields = ["post_content"]