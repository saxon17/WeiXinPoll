# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from polls.views import indext

#patterns 返回的是一个列表，这个列表里面存储的是url对象	
#url是一个析构函数，返回的是url对象
'''
urlpatterns = [
    url(r'^$', views.index, name='index')
]
'''
#patterns函数可以 通过prefix参数

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WeixinPoll.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),  #include解释：服务器从admin后面的'/'反斜杠截段
    url(r'^$', indext,name='firstPage')			#然后继续在include的url对象列表中寻找
    											#在django.conf.urls文档中有更像详尽描述	



)





