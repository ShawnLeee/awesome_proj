# encoding: utf-8
from django.conf import settings
from django.db import connection, models, transaction
from django.db.models import Q, F

class Pages(object):
    '''
    分页查询类
    '''
    def __init__(self, count, current_page=1, list_rows=20):
        self.total = count
        self._current = int(current_page)
        self.size = list_rows
        self.pages = self.total // self.size + (1 if self.total % self.size else 0)

        if (self.pages == 0) or (self._current < 1) or (self._current > self.pages):
            self.start = 0
            self.end = 0
            self.index = 1
        else:
            self.start = (self._current - 1) * self.size
            self.end = self.size + self.start
            self.index = self._current
        self.prev = self.index - 1 if self.index > 1 else self.index
        self.next = self.index + 1 if self.index < self.pages else self.index

    @property
    def current_page(self):
            return self._current

    def __str__(self):
        return "----total:{}-size:{}-pages:{}----".format(self.total, self.size, self.pages)


def query_to_dicts(query_string, *query_args):
    """
    Run a simple query and produce a generator
    as a bunch of dictionaries 
    with keys for the column values selected.
    """
    cursor = connection.cursor()
    cursor.execute(query_string, query_args)
    col_names = [desc[0] for desc in cursor.description]
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        row_dict = dict(izip(col_names, row))
        yield row_dict
    return

class UserManager(models.Manager):

    def get_user_name(self, like=None):
        query_set = self.get_queryset().filter(Q(nickname__contains=like))
        return query_set

    def user_xingzuo(self, xingzuo):
        query_set = self.get_queryset().filter(Q(user_xingzuo__contains=xingzuo))
        return query_set


class PostManager(models.Manager):
    def get_all_post(self, num=20, current_page=1):
        count = self.get_queryset().count()
        page = Pages(count, current_page, num)
        query = self.get_queryset().select_related('author').\
        order_by('-id')[page.start:page.end]
        if settings.DEBUG:
            print(page)
        return query, page

    def get_hot_post(self, num=20, current_page=1):
        count = self.get_queryset().count()
        page = Pages(count, current_page, num)
        query = self.get_queryset().select_related('author').\
        order_by('-id')[page.start: page.end]
        return query, page

class ReplyManager(models.Manager):

    def get_all_replies_by_post_id(self, post_id, num=20, current_page=1):
        count = self.get_queryset().filter(post_id=post_id).count()
        page = Pages(count, current_page, num)
        query = self.get_queryset().select_related('author').\
        filter(post_id=post_id).order_by('-floor')[page.start:page.end]
        return query, page

    def get_user_all_replies(self, uid, num=16, current_page=1):
        count = self.get_queryset().filter(author_id=uid).count()
        page = Pages(count, current_page, num)
        query = sel.get_queryset().select_related('post', 'post__author').\
        filter(author_id=uid).order_by('-id')[page.start:page.end]
        return query, page

    def max_floor(self, post_id):
        cursor = connection.cursor()
        cursor.execute("""SELECT MAX(floor) FROM API_1_0_reply WHERE post_id=%s""", [post_id])
        return cursor.fetchone()[0]

    def total_reply(self, post_id):
        cursor = connection.cursor()
        cursor.execute("""SELECT COUNT(*) AS totoal 
                          FROM API_1_0_reply 
                          WHERE post_id = %s;""", [post_id])
        return cursor.fetchone()[0]