# encoding: utf-8
from django.contrib import admin
import xadmin
from django.core import urlresolvers
from .models import FakeUser, Post

# Register your models here.

# class UserAdmin(object):
#     search_fields = ('username')
#     fields = ('id', 'username')
#     ordering = ('id')
#     save_on_top = True

# xadmin.site.register(FakeUser, UserAdmin)

# @xadmin.sites.register(Post)
class PostAdmin(object):
    list_display = ("author", "up_vote", "down_vote","comment_count","created_at","content",)
    search_fields = ['content', ]

xadmin.site.register(Post, PostAdmin)