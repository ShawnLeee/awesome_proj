# encoding: utf-8
from bs4 import BeautifulSoup
import urllib2
from headers import headers
import unittest

QB_BASE_URL = 'http://www.qiushibaike.com'


def enum(**enums):
    return type('Enum', (), enums)

QBCategory = enum(Hot='http://www.qiushibaike.com/8hr/page/',
                 HR24='http://www.qiushibaike.com/hot/page/',
                 ImgRank='http://www.qiushibaike.com/imgrank/page/')


def user_url(user_id):
    return QB_BASE_URL + '/users/%s/' % user_id


def user_soup(user_id, num_retries=2):
    try:
        u_url = user_url(user_id)
        soup = soup_page(u_url)
    except urllib2.URLError as e:
        if hasattr(e, 'code') and 500 <= e.code < 600:
            return user_soup(user_id, num_retries-1)

    return soup


def user_articles_soup(user_id, num_retries=2, page=1):
    try:
        articles_url = QB_BASE_URL + '/users/%s/articles/page/%s/' % (user_id, page)
        soup = soup_page(articles_url)

    except urllib2.URLError as e:
        if hasattr(e, 'code') and 500 <= e.code < 600:
            return user_soup(user_id, num_retries-1, page)

    return soup


def article_soup(article_id):
    try:
        article_url = QB_BASE_URL + '/article/%s' % article_id
        art_soup = soup_page(article_url)
    except urllib2.URLError:
        return None
    return art_soup



def soup_page(url):
    '''
    将制定URL获取的html页面，转换为bs对象
    '''
    try:
        req = urllib2.Request(url, headers=headers)
        res = urllib2.urlopen(req)
        page = res.read().decode('utf-8')
        soup = BeautifulSoup(page, 'lxml')
        return soup
    except urllib2.URLError as e:
        if hasattr(e, 'reason'):
            print("连接失败:", e.reason)
        return None


def get_page(page_type=QBCategory.Hot, page_index=1):
    '''
    获取一页糗事
    '''
    page_url = page_type+'%s/' % page_index
    the_soup_page = soup_page(page_url)
    return the_soup_page


def get_max_page():
    max_num = 1
    page_s = get_page()
    pgs = page_s.find_all('ul', class_='pagination')
    for li in pgs[0].children:
        page_num_sp = li.find('span')
        if isinstance(page_num_sp, int):
            pass
        else:
            try:
                page_num = int(page_num_sp.string)
                if page_num > max_num:
                    max_num = page_num
            except Exception as e:
                pass
    return max_num


def get_userids(page_index=1):
    """
    获取一页中所有的用户id
    Args:
        page_index: 页码

    Returns:用户id数组

    """

    page_soup = get_page(page_index=page_index)
    users = []
    if page_soup is None:
        return users
    posts_soup = page_soup.find_all('div', class_='article block untagged mb15')
    for post in posts_soup:
        author = post.find('div', class_='author').find('a', rel='nofollow')

        if author is None:
            continue
        else:
            try:
                user_id = author['href'].split('/')[2]
            except Exception as e:
                print e
            users.append(user_id)
    return users


def get_users(friends_soup):
        user_ids = []
        friends_li_soup = friends_soup.find_all('li')
        if len(friends_li_soup) == 0:
            pass
        for user in friends_li_soup:
            userid = user.find('a', rel='nofollow')['href'].split('/')[2]
            user_ids.append(userid)
        return user_ids


def get_friends(userid):
    friends_url = QB_BASE_URL + '/users/%s/followers/' % userid

    follow_friends = []
    followers_frieds = []
    each_friends = []
    friends_soup = soup_page(friends_url)

    if friends_soup is not None:
        f_soup = friends_soup.find_all('div', class_='user-block user-follow')
        if len(f_soup) > 0:
            # 关注的用户
            follow_soup = f_soup[0]
            follow_friends = get_users(follow_soup)

            # 粉丝用户
            followers_soup = f_soup[1]
            followers_frieds = get_users(followers_soup)

            # 互粉好友
            each_follow_soup = f_soup[2]
            each_friends = get_users(each_follow_soup)
    else:
        pass
    relatonships = {'user_id': userid,
                    'follow_friends': follow_friends,
                    'followers_friends': followers_frieds,
                    'each_friends': each_friends
                    }

    return relatonships


def get_relationships(page=1):
    relationships = []
    users = get_authors(page_index=page)
    for user_id in users:
        relation = get_friends(user_id)
        relationships.append(relation)

    return relationships


def get_user_profile(user_id):
    """
    获取一个用户的资料
    Args:
        user_id: 用户id
    """
    
    user_sp = user_soup(user_id)
    if user_sp is not None:
        user_name = user_sp.find('div', class_='user-header-cover').find('h2').text
        user_avatar = user_sp.find('div', class_='user-header').find('a', class_='user-header-avatar').find('img').get('src','')

        user_msg_soup = user_sp.find_all('div', class_='user-statis')
        try:
            user_index = user_msg_soup[0].find_all('li')
            user_followers = str(user_index[0].contents[1])
            user_follow = str(user_index[1].contents[1])
            user_articles = str(user_index[2].contents[1])
            user_comments = str(user_index[3].contents[1])
            user_selected = str(user_index[4].contents[1])

            user_detail = user_msg_soup[1].find_all("li")
            user_married = str(user_detail[0].contents[1])
            user_xingzuo = unicode(user_detail[1].contents[1])
            user_career = unicode(user_detail[2].contents[1])
            user_hometown = unicode(user_detail[3].contents[1])
            user_signup_age = unicode(user_detail[4].contents[1])

        except IndexError:
            return None
        user_profile = {
                "user_name": user_name,
                "user_avatar": user_avatar,
                "user_id": user_id,
                "user_followers": user_followers,
                "user_follow": user_follow,
                "user_articles": user_articles,
                "user_comments": user_comments,
                "user_selected": user_selected,
                "user_marrieg": user_married,
                "user_xingzuo": user_xingzuo,
                "user_career": user_career,
                "user_hometown": user_hometown,
                "user_signup_age": user_signup_age,
            }

    return user_profile


def pure_stripped_string(stripped_strings):
    finnal_string = ''
    for string in stripped_strings:
        finnal_string += repr(string)

    return finnal_string


def get_user_articles(user_id, page=1):

    def get_article_id(article_soup_p):
        user_article_id = article_soup_p['id'][7:]
        return user_article_id

    soup = user_articles_soup(user_id, page)
    articles_soup = soup.find_all('div', class_='user-block user-article')

    article_ids = []
    for article_s in articles_soup:
        article_id = get_article_id(article_s)
        article_ids.append(article_id)

    return article_ids


def get_article(article_id):
    art_soup = article_soup(article_id)
    if art_soup is not None:
        content = art_soup.find('div', id='single-next-link').find('div', class_='content').text.strip()
        up_vote = art_soup.find('div', class_='stats').find('span', class_='stats-vote').find('i').text
        comment_count = art_soup.find('div', class_='stats').find('span', class_='stats-comments').find('i').text
        author_id = art_soup.find('div', class_='author').find('a').get('href').split('/')[2]
        article_dict = {
            'article_id': article_id,
            'content': content,
            'up_vote': up_vote,
            'comment_count': comment_count,
            'author_id': author_id,
        }
        comments = get_article_comments(art_soup)
        return article_dict, comments


def get_article_comments(article_sp):
    comments = []
    comments_sp = article_sp.find('div', class_='comments-wrap').find_all('div', class_='comment-block')
    for com_sp in comments_sp:
        comment_dict = {
            'comment_content': com_sp.find('div', class_='replay').find('span').text,
            'author_id': com_sp.find('div', class_='replay').find('a').get('href').split('/')[2],
            'report': com_sp.find('div', class_='report').text
        }
        comments.append(comment_dict)
    return comments
