# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Poll,Choice
#from django.template import RequestContext, loader
from django.shortcuts import render
from django.http import Http404


# Create your views here.


# def index(request):
# 	return HttpResponse("HEello,My name is saxon")

def detail(request, poll_id):  #http:// = request , poll_id = 'polls/1/'
	return HttpResponse("You're looking at poll %s." % poll_id)
def results(request, poll_id):
	return HttpResponse("You're looking at the results of poll %s." % poll_id)
def vote(request, poll_id):
	return HttpResponse("You're voting on poll %s." % poll_id)

# def index(request):
# 	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]	#Poll.objects 加载Poll表（类）中的所有实列
# 	template = loader.get_template('polls/index.html')			#取template
# 	context = RequestContext(request, {
# 	'latest_poll_list': latest_poll_list,
# 	})
# 	return HttpResponse(template.render(context))

def index(request):
	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
	context = {'latest_poll_list': latest_poll_list}	#等待翻译的MAP
	return render(request, 'polls/index.html', context)  #这里用到request是因为request带了用户需要的变量

def detail(request, poll_id):
	try:
		poll = Poll.objects.get(pk=poll_id)  #在objects列表中找到pk为poll_id的对象
	except Poll.DoesNotExist:
		raise Http404
	return render(request, 'polls/detail.html', {'poll': poll})