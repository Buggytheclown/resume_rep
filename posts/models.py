from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


# Create your models here.
class MailModel(models.Model):
    sender = models.ForeignKey(User, related_name='sender1')
    recipient = models.ForeignKey(User, related_name='recipient2')
    content = models.TextField(max_length=600)
    timestamp = models.DateTimeField(auto_now_add=True)


class PlusModel(models.Model):
    on_rating = models.ForeignKey('Post')
    user_plus = models.PositiveIntegerField()

    def __str__(self):
        return str(self.user_plus)


class MinusModel(models.Model):
    on_rating = models.ForeignKey('Post')
    user_minus = models.PositiveIntegerField()

    def __str__(self):
        return str(self.user_minus)


class CommentModel(models.Model):
    user = models.ForeignKey(User)
    in_post = models.ForeignKey('Post')
    content = models.TextField('Your comment', max_length=600)
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

    def get_rating(self):
        plus = PlusModel.objects.filter(on_rating=self.id).count()
        minus = MinusModel.objects.filter(on_rating=self.id).count()
        return plus - minus

    class Meta:
        ordering = ["-updated", "-timestamp"]


class ContactModel(models.Model):
    name = models.CharField('Name/Organization', max_length=120)
    email = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=120, blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class ProfileModel(models.Model):
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

    def get_user_score(self):
        posts = Post.objects.filter(user=self.user)
        plus = 0
        minus = 0
        for post in posts:
            plus += PlusModel.objects.filter(on_rating=post).count()
            minus += MinusModel.objects.filter(on_rating=post).count()
        return plus - minus

    def get_comment_count(self):
        return CommentModel.objects.filter(user=self.user).count()

    def get_posts_count(self):
        return Post.objects.filter(user=self.user).count()

    def get_mail_count(self):
        return MailModel.objects.filter(recipient=self.user).count()

    def __str__(self):
        return self.user.get_username()
