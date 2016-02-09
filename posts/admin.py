from django.contrib import admin

# Register your models here.
from posts.models import Post, ContactModel


class PostModelAdmin (admin.ModelAdmin):
    list_display = ['title', 'updated', 'timestamp']
    list_filter = ['updated', 'timestamp']
    search_fields = ['title', 'content']


admin.site.register(Post, PostModelAdmin)


class ContactModelAdmin (admin.ModelAdmin):
    list_display = ['name','subject', 'email', 'timestamp']
    list_filter = ['timestamp']

admin.site.register (ContactModel, ContactModelAdmin )