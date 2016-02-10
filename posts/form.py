from django import forms

from .models import Post, ContactModel, ProfileModel, CommentModel
from django.contrib.admin import widgets

class CommentModelForm (forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = [
            'content',
        ]


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

class ProfileForm(forms.ModelForm):

    class Meta:
        birthdate = forms.DateField(widget=widgets.AdminDateWidget())
        model = ProfileModel
        fields = [
            'first_name',
            'last_name',
            'gender',
            'avatar',
        ]