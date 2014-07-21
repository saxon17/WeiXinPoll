# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin



from polls import views  #尽管导入了views 还是不能直接调用 views里面的函数(相当于打开了一个文件
							#还没有进行任何操作)
# from polls.views import index
admin.autodiscover()



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
    url(r'^$',views.index,name='index')			#然后继续在include的url对象列表中寻找
    											#在django.conf.urls文档中有更像详尽描述	



)

# urlpatterns = patterns('',
# 		url(r'^admin/', include(admin.site.urls)),
# 		#匹配'polls'后带着polls之后字符们，去polss.urls里面继续匹配
# 	 	url(r'^polls/', include('polls.urls')),  
# 		# ex: /polls/
# 		url(r'^$', views.index, name='index'),
# 		# ex: /polls/5/
# 		url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
# 		# ex: /polls/5/results/
# 		url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
# 		# ex: /polls/5/vote/
# 		url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
# 	)




