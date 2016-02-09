from django import forms
from .models import Post, ContactModel


class PostModel (forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
        ]

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = [
            'name',
            'email',
            'subject',
            'content',
        ]