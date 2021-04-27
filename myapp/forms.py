from django import forms
from django.contrib.auth import login, authenticate
from .models import Comment


class AddNewForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    content = forms.CharField(label='Content', widget=forms.Textarea)


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']



