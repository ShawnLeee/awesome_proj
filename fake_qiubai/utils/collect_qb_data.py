# encoding: utf-8
from utils.spider import *
from redis import Redis
from API_1_0.models import *
import time
import json
from django.conf import settings

from django.db import IntegrityError


r = Redis(host='localhost', port=6379, db=0)

def shedule_row_cache(row_id, delay, conn=r):
    conn.zadd('delay:', row_id, delay)
    conn.zadd('schedule:', row_id, time.time())

def cache_rows(conn=r):
    while True: 
        next_ = conn.zrange('schedule:', 0, 0, withscores=True)
        now = time.time()
        if not next_ or next_[0][1] > now:
            time.sleep(.05)
            continue

        row_id = next_[0][0]
        delay = conn.zscore('delay:', row_id)
        if delay <= 0:
            conn.zrem('delay:', row_id)
            conn.zrem('schedule:', row_id)
            conn.delete('post:'+row_id)
        row = Status.objects.get(id=row_id)
        print row
        conn.zadd('schedule:', row_id, now + delay)
        conn.set('post:' + row_id, json.dumps(row.to_dict()))


def process_user(user_id):
    # 获取用户信息
    user_profile = get_user_profile(user_id=user_id)
    if user_profile is not None:
        f_user = FakeUser.user_with_userdict(user_profile)
        try:
            f_user.save()
        except IntegrityError as e:
            raise Exception(e)


def process_comments(comments):
    pass


def process_article(article_id):
    article_dict, comments = get_article(article_id=article_id)
    if article_dict is not None:
        t_post = Post.post_withdict(article_dict)
        try:
            t_post.save()
        except IntegrityError as e:
            raise Exception(e)

    # 存储评论 
    for comment in comments:
        comment['post_id'] = article_id
        try:
            # 存储评论用户
            process_user(comment.get('author_id'))
            reply = Reply.reply_withdict(comment)
            reply.save()
        except Exception as e:
            continue


def process_user_articles(user_id):
    # 获取用户的所有糗事id
    article_ids = get_user_articles(user_id=user_id)
    for art_id in article_ids:
        process_article(article_id=art_id)


def collect(page=1):
    print('start collecting page %d data...\n' % page)
    # 获取第一页内容的所有用户id
    user_ids = get_userids(page_index=page)
    # 获取用户发布的所有糗事
    for u_id in user_ids:
        try:
            # 处理用户信息
            process_user(user_id=u_id)
            # 处理用户的所有糗事
            process_user_articles(user_id=u_id)
            # 处理评论
        except Exception as e:
            continue

if __name__ == '__main__':
    collect()

