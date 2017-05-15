from django.conf.urls import url
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    # posts
    url(r'^post/$', views.ReplyView.as_view()),
    url(r'^posts/$', cache_page(60 * 10)(views.PostsView.as_view()), name='post-list'),
    # url(r'^posts/$', views.PostsView.as_view(), name='post-list'),
    url(r'^hot-post/$', views.HotPostView.as_view()),
    url(r'^postdetail/$', views.PostDetail.as_view()),
    url(r'^post/create/$', views.PostCreateView.as_view()),
    url(r'^hotpost/$', views.PostsView.as_view()),
    url(r'^recent/$', views.RecentPosts.as_view()),

    url(r'^test_auth/$', views.TestAuth.as_view()),
    url(r'^postreplies/$', views.PostReplyView.as_view()),
    url(r'^register/$', views.RegisterView.as_view()),
    url(r'^token/$', views.TokenView.as_view()),
    url(r'^reply/$', views.ReplyCreateView.as_view()),
    url(r'^login/$', views.TokenView.as_view()),
    url(r'^usermsg/$', views.UserMsg.as_view()),
    url(r'^setpassword/$', views.UserPassword.as_view()),
    url(r'^supersetpassword/$', views.SuperSetPassword.as_view()),

    #vote
    # url(r'vote/$', views.VoteView.as_view()),
    url(r'vote/$', views.VoteFormView.as_view()),
]