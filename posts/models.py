from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


# Create your models here.

class CommentModel(models.Model):
    user = models.ForeignKey(User)
    in_post = models.ForeignKey('Post')
    content = models.TextField('Your comment', max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'id': self.in_post_id})

class Post(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=120)
    image = models.FileField(null=True, blank=True)
    content = models.TextField()
    updated = models.DateTimeField('Was updated', auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField('Was created', auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'id': self.id})

    class Meta:
        ordering = ["-updated", "-timestamp"]


class ContactModel (models.Model):
    name = models.CharField('Name/Organization', max_length=120)
    email = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=120, blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class ProfileModel (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(blank=True, null=True, max_length=50)
    last_name = models.CharField(blank=True, null=True, max_length=50)
    avatar = models.ImageField(blank=True, null=True)
    # gender
    Male = 'ml'
    Female = 'fm'
    Male_to_Female = 'mlf'
    Female_to_Male = 'ftm'
    Two_spirit = '2sp'
    Other = 'oth'
    gender_choices = (
        (Male, 'Male'),
        (Female, 'Female'),
        (Male_to_Female, 'Male to Female'),
        (Female_to_Male, 'Female to Male'),
        (Two_spirit, 'Two spirit'),
        (Other, 'Other'),
    )
    gender = models.CharField(max_length=3, choices=gender_choices, default=Other)

    def __str__(self):
        return self.user.get_username()