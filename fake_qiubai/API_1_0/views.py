# encoding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from models import Reply, Post, FakeUser
from rest_framework.response import Response
from .redis_cache import *
from utils.fake_tool import timecounter
from django.db import IntegrityError
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
import datetime
from PIL import ImageFile
from django.conf import settings
from uuid import uuid4
import os
from django.views.decorators.csrf import csrf_exempt

class TestAuth(APIView):
    def get(self, request):
        authentication_classes = (SessionAuthentication, TokenAuthentication)
        permission_classes = (IsAuthenticated,)
        return Response({'status': 'OK'})

class UserMsg(APIView):

    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        the_user = request.user
        user = FakeUser.objects.get(id=the_user.id)
        return Response(user.to_dict())

class UserPassword(APIView):

    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request):

        new_password = request.POST.get('newpassword')

        try:
            the_user = FakeUser.objects.get(id=request.user.id)
            the_user.password = new_password
            the_user.save()
            return Response({'status':0, 'msg':'更改密码成功'})
        except Exception as e:
            return Response({'status':1, 'errormsg':e})


class SuperSetPassword(APIView):

    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            req_user = request.user
            the_req_user = FakeUser.objects.get(id=req_user.id)

            to_set_user_id = request.POST.get('userid')
            to_set_user = FakeUser.objects.get(id=to_set_user_id)
            new_password = request.POST.get('newpassword')

            if the_req_user.is_superuser:
                to_set_user.password = new_password
                to_set_user.save()
                return Response({'status': 0, 'msg':'更新密码成功'})
        except Exception as e:
            return Response({'status':1, 'errormsg':e})




class RegisterView(APIView):

    def post(self, request):
        err_msg = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username is None:
            err_msg['status'] = 3
            err_msg['msg'] = '缺少用户名'
            return Response(err_msg)
        if password is None:
            err_msg['status'] = 4
            err_msg['msg'] = '缺少密码'
            return Response(err_msg)
        if len(password) <= 6:
            err_msg['status'] = 5
            err_msg['msg'] = '密码长度小于6位'
            return Response(err_msg)

        try:
            new_user = FakeUser.objects.create_user(username=username, password=password)
            new_user.save()
            return Response({
                'status' : 0,
                'msg' : '注册成功',
                })
        except IntegrityError as e:
            if 'Duplicate' in e[1]:
                err_msg['status'] = 6
                err_msg['msg'] = '注册失败(用户名已被注册)'
            else:
                pass
            return Response(err_msg)


class TokenView(APIView):

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            try:
                user_token = Token.objects.get(user_id = user.id)
            except Token.DoesNotExist:
                user_token = Token.objects.create(user=user)

            user_dict = FakeUser.objects.get(id=user.id).to_dict()
            user_dict['token'] = user_token.key

            return Response({'status':0, 'user':user_dict})
        else:
            return Response({'status':1,'error_msg':'用户名密码错误'})


class PostView(APIView):

    # @timecounter
    def get(self, request):
        page = request.GET.get('page', 1)
        posts, page = Post.objects.get_all_post(current_page=page)
        return Response([post.to_dict() for post in posts])


class PostsView(APIView):

    def get(self, request):
        page = request.GET.get('page', 1)
        posts, page = Post.objects.get_all_post(current_page=page)
        res = {
            'num': page.size,
            'total_pages': page.pages,
            'current_page': page.current_page,
            'posts': [post.to_dict() for post in posts]
        }
        return Response(res)


class PostDetail(APIView):
    '''
    获取指定ID的post
    '''

    def get(self, request):
        article_id = request.GET.get('articleid')
        if article_id is None:
            return Response({'status': 6, 'errorMsg':'Parameter articleid is missing!'})
        else:
            try:
                post = Post.objects.get(id=article_id)
                return Response(post.to_dict())
            except ObjectDoesNotExist:
                return Response({'status':5, 'errorMsg':'Post %s does not exist!' % article_id})


class ReplyView(APIView):

    def get(self, request):
        post_id = request.GET.get('post_id')
        page = request.GET.get('page', 1)
        replies, page = Reply.objects.\
        get_all_replies_by_post_id(post_id=post_id, current_page=page)
        return Response([rep.to_dict() for rep in replies])


class HotPostView(APIView):

    # @timecounter
    def get(self, request):
        page = int(request.GET.get('page', 1))
        per_page = int(request.GET.get('per_page', 20))
        hot_posts = get_cached_hot_post(per_page=per_page,page=page)
        return Response(hot_posts)


class PostReplyView(APIView):
    def get(self, request):
        articleid = request.GET.get('articleid')
        page = int(request.GET.get('page', 1))
        if articleid is None:
            err_msg = {
                'error_message': '缺少参数(articleid)',
                'status': 1,
            }
            return Response(err_msg)

        replies, page= Reply.objects.\
        get_all_replies_by_post_id(post_id=articleid, current_page=page)
        reply_msg = get_reply_msg(post_id=articleid)

        return Response({'reply_msg':reply_msg, 'data': [rep.to_dict() for rep in replies]})


class PostCreateView(APIView):

    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    
    @csrf_exempt
    def post(self, request):
        content = request.POST.get('content')
        files = request.FILES.getlist('pic')

        post_dict = {
            "content": content,
            "author_id": request.user.id,
            "up_vote": 0,
            "down_vote": 0,
            "comment_count": 0,
        }
        post = Post.post_withdict(post_dict)
        try:
            post.save()
        except Exception as e:
            return Response(e)

        pics = []
        for f in files:
            parser = ImageFile.Parser()
            for chunk in f.chunks():
                parser.feed(chunk)
            img = parser.close()
            imgpath = os.path.join(settings.MEDIA_URL, uuid4().hex+'.jpeg')
            img_abs_path = os.path.join(settings.BASE_DIR, imgpath)
            img.save(img_abs_path)
            post_img = PostImage(img=imgpath, post_id=post.id)
            pics.append(post_img)

        try:
            for pic in pics:
                pic.save()
            return Response({"status": 0, "post": post.to_dict()})
        except Exception as e:
            return Response(e)



class ReplyCreateView(APIView):

    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user = request.user
        articleid = request.POST.get('articleid')
        content = request.POST.get('content')
        created_at = datetime.datetime.now()
        author_id = user.id

        # 从缓存中取回复统计
        reply_msg = get_reply_msg(post_id=articleid)
        if reply_msg is None:
            # 从数据库中取floor
            max_floor = Reply.objects.max_floor(post_id=articleid)
        else:
            max_floor = reply_msg.get('max_floor')

        new_reply = Reply.reply_withdict({
            'post_id': articleid,
            'comment_content': content,
            'author_id': user.id,
            'created_at': created_at,
            'floor': int(max_floor) + 1,
            })
        try:
            new_reply.save()
            # 更新缓存
            cache_reply_msg(post_id=articleid, max_floor=int(max_floor) + 1)
            return Response(new_reply.to_dict())

        except Exception as e:
            return Response(e)




