from django.conf.urls import url
from django.contrib import admin
from article import views
from article.views import RSSFeed

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name = 'home'),
    url(r'^(?P<id>\d+)/$',views.detail,name='detail'),
    url(r'^archives/$', views.archives, name = 'archives'),
    url(r'^aboutme/$', views.about_me, name ='about_me'),
    url(r'^tag(?P<tag>\w+)/$', views.search_tag, name = 'search_tag'),
    url(r'^search/$',views.blog_search,name = 'search'),
    url(r'^feed/$', RSSFeed(), name = "RSS"), #add urlconf,and set name as RSS,so we can use the url in model
    ]
