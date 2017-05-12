# encoding: utf-8
from __future__ import unicode_literals
from itertools import *
from django.contrib.auth.models import AbstractUser
from django.db import connection, models, transaction
# from datetime import datetime
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
import datetime
from django.db.models import Q, F
from manager import UserManager, PostManager, ReplyManager, Pages

def xlocaltime():
    return timezone.localtime(timezone.now())

class NormalTextField(models.TextField):
    def db_type(self, connection):
        return 'text'


class FakeUser(AbstractUser):
    nickname = models.CharField(max_length=200, null=True, blank=True)
    avatar = models.CharField(max_length=200, null=True, blank=True)
    signature = models.CharField(max_length=500, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    role = models.IntegerField(null=True, blank=True)
    reputation = models.IntegerField(null=True, blank=True)
    self_intro = models.CharField(max_length=500, null=True, blank=True)
    updated = models.DateTimeField(null=True, blank=True, default=timezone.now)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    github = models.CharField(max_length=200, null=True, blank=True)
    douban = models.CharField(max_length=200, null=True, blank=True)
    weibo = models.CharField(max_length=200, null=True, blank=True)

    user_articles = models.IntegerField(default=0)
    user_selected = models.IntegerField(default=0)
    user_marriage = models.CharField(max_length=16, null=True, blank=True)
    user_comments = models.IntegerField(default=0)
    user_signup_age = models.CharField(max_length=50, null=True, blank=True)
    user_followers = models.IntegerField(default=0)
    user_xingzuo = models.CharField(max_length=36, null=True, blank=True)
    user_hometown = models.CharField(max_length=200, null=True, blank=True)

    objects = models.Manager()
    xobjects = UserManager()

    def to_dict(self):
        user_dict = {
            'username': self.username,
            'avatar': self.avatar,
            'user_id': self.id,
            'marriage': self. user_marriage,
        }
        return user_dict

    @classmethod
    def user_with_userdict(cls, user_dict):
        f_user = cls()
        f_user.nickname = user_dict.get('user_name')
        f_user.username= user_dict.get('user_name')
        f_user.user_hometown = user_dict.get('user_hometown')
        f_user.user_articles = user_dict.get('user_articles')
        f_user.user_selected = user_dict.get('user_selected')
        f_user.user_marriage = user_dict.get('user_marrieg')
        f_user.user_comments = user_dict.get('user_comments')
        f_user.user_followers = user_dict.get('user_follow')
        f_user.user_signup_age = user_dict.get('user_signup_age')
        f_user.id = user_dict.get('user_id')
        f_user.user_xingzuo = user_dict.get('user_xingzuo')
        f_user.avatar = user_dict.get('user_avatar')
        return f_user


class Post(models.Model):
    '''
    糗事表，定义糗事的基本单位
    '''
    content = NormalTextField(null=True, blank=True)
    author = models.ForeignKey(FakeUser, related_name='post_author', null=True, blank=True)
    up_vote = models.IntegerField(null=True,blank=True, default=0)
    down_vote = models.IntegerField(null=True,blank=True, default=0)
    comment_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(null=True, blank=True, default=timezone.now)

    objects = PostManager()

    def to_dict(self):
        # user = FakeUser.objects.get(id=self.author_id)
        user = self.author
        # print(dir(self.author))
        po_dict = {
                    'content': self.content,
                    'post_id': self.id,
                    'author': user.to_dict(),
                    'up_vote': self.up_vote,
                    'down_vote': self.down_vote,
                    'comment_count': self.comment_count,
                    'created_at': self.created_at,
                  }

        try:
            post_img = PostImage.objects.get(post_id=po_dict.get('post_id'))
            po_dict['img'] = 'http://localhost:8000/' + post_img.img
        except ObjectDoesNotExist:
            pass
        return po_dict

    @classmethod
    def post_withdict(cls, article_dict):
        t_post = cls()
        t_post.content = article_dict.get('content')
        t_post.author_id = article_dict.get('author_id')
        t_post.up_vote = article_dict.get('up_vote')
        t_post.id = article_dict.get('article_id')
        t_post.comment_count = article_dict.get('comment_count')
        return t_post


class Reply(models.Model):
    post = models.ForeignKey(Post, null=True, blank=True)
    author = models.ForeignKey(FakeUser, related_name='reply_author', null=True, blank=True)
    content = NormalTextField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True, default=timezone.now)
    updated = models.DateTimeField(null=True, blank=True, default=timezone.now)
    up_vote = models.IntegerField(null=True, blank=True)
    down_vote = models.IntegerField(null=True, blank=True)
    floor = models.IntegerField(null=True, blank=True)

    objects = ReplyManager()

    def to_dict(self):
        user = FakeUser.objects.get(id=self.author_id)
        r_dict = {
            'post_id': self.post_id,
            'user': user.to_dict(),
            # 'author_id': self.author_id,
            'content': self.content,
            'floor': self.floor,
            }
        return r_dict

    @classmethod
    def reply_withdict(cls, comment_dict):
        rep = cls()
        rep.post_id = comment_dict.get('post_id')
        rep.author_id = comment_dict.get('author_id')
        rep.floor = comment_dict.get('report')
        rep.content = comment_dict.get('comment_content')
        rep.created_at = comment_dict.get('created_at')
        rep.floor = comment_dict.get('floor')
        return rep



class Vote(models.Model):
    status = models.IntegerField(null=True, blank=True)
    involved_type = models.IntegerField(null=True, blank=True, default=0)
    involved_user = models.ForeignKey(FakeUser, related_name='vote_user', null=True, blank=True)
    involved_reply = models.ForeignKey(Reply, related_name='vote_reply', null=True, blank=True)
    involved_post = models.ForeignKey(Post, related_name='vote_poset', null=True, blank=True)
    trigger_user = models.ForeignKey(FakeUser, related_name='vote_trigger', null=True, blank=True)
    occurrence_time = models.DateTimeField(null=True, blank=True, default=xlocaltime)

    def to_dict(self):
        return {
            'status': self.status,
            'occurrence_time': self.occurrence_time.strftime('%Y-%m-%d-%H-%M')
        }




class Relation(models.Model):
    rel_user = models.ForeignKey(FakeUser, related_name='rel_user', null=True, blank=True)
    follower = models.ForeignKey(FakeUser, related_name='follower', null=True, blank=True)
    rel_type = models.IntegerField(null=True, blank=True)
    follow_each = models.IntegerField(null=True, blank=True)


class PostImage(models.Model):
    img = models.CharField(max_length=200, null=True, blank=True)
    post = models.ForeignKey(Post, related_name='post')














