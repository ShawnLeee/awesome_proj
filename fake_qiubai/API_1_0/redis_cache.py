# encoding: utf-8
from redis import Redis
from .models import *
import time
import json

r = Redis(host='localhost', port=6379, db=0)


def get_cached_hot_post(per_page=20, page=1, conn=r):
    start = (page - 1) * per_page
    end = start + per_page -1

    # 1.get post ids
    ids = conn.zrange('hot_post:', start, end)
    posts = []

    for post_id in ids:
        post_json = conn.get(post_id)
        posts.append(json.loads(post_json))
        # post_dict = conn.hgetall(post_id)
        # posts.append(post_dict)
    return posts


def cache_hot_post(conn=r):

    def _cache_posts(posts):
        for post in posts:
            post_id = 'post:' + str(post.id)
            conn.zadd('hot_post:', post_id, post.comment_count)
            conn.set(post_id, json.dumps(post.to_dict()))
            # conn.hmset(post_id, post.to_dict())

    posts, page = Post.objects.get_hot_post()
    total_pages = page.pages

    for i in range(total_pages):
        posts, page = Post.objects.get_hot_post(current_page=i + 1)
        _cache_posts(posts)


def cache_max_floor(post_id, max_floor, conn=r):
    post_max_floor = 'post_max_floor:' + str(post_id)
    conn.set(post_max_floor, max_floor)

def get_max_floor(post_id, conn=r):
    max_floor = conn.get('post_max_floor:' + str(post_id))
    return max_floor


def cache_reply_msg(post_id, max_floor=None):
    if max_floor is None:
        max_floor = Reply.objects.max_floor(post_id=post_id)
        if max_floor is None:
            max_floor = 0

    total_reply = Reply.objects.total_reply(post_id=post_id)

    reply_msg = {'max_floor': max_floor, 'total_reply': total_reply}

    reply_msg_key = 'reply_msg:' + str(post_id)
    r.hmset(reply_msg_key, reply_msg)
    return reply_msg

def get_reply_msg(post_id):
    reply_msg = r.hgetall('reply_msg:' + str(post_id))
    if len(reply_msg) == 0:
        reply_msg = cache_reply_msg(post_id=post_id)
    return reply_msg





# __all__ = ['get_cached_hot_post']



