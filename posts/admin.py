from django.contrib import admin

# Register your models here.
from posts.models import Post, ContactModel, ProfileModel, CommentModel, PlusModel, MinusModel


class PostModelAdmin (admin.ModelAdmin):
    list_display = ['id', 'title', 'updated', 'timestamp']
    list_filter = ['updated', 'timestamp']
    search_fields = ['title', 'content']


admin.site.register(Post, PostModelAdmin)


class ContactModelAdmin (admin.ModelAdmin):
    list_display = ['name','subject', 'email', 'timestamp']
    list_filter = ['timestamp']

admin.site.register (ContactModel, ContactModelAdmin )

admin.site.register(ProfileModel)


class CommentModelAdmin (admin.ModelAdmin):
    list_display = ['in_post', 'user', 'content', 'timestamp']
    list_filter = ['in_post',]
admin.site.register(CommentModel, CommentModelAdmin)


class PlusModelAdmin (admin.ModelAdmin):
    list_display = ['on_rating', 'user_plus']
    list_filter = ['on_rating','user_plus']
admin.site.register(PlusModel, PlusModelAdmin)

class MinusModelAdmin (admin.ModelAdmin):
    list_display = ['on_rating', 'user_minus']
    list_filter = ['on_rating','user_minus']
admin.site.register(MinusModel, MinusModelAdmin)