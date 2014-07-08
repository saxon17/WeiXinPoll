# -*- coding: utf-8 -*-
import datetime
from django.utils import timezone
from django.db import models
# Create your models here.
class Poll(models.Model):									#表内容
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')   #date published是在admin中
														#显示的pub_date的别名
														
															#Poll动作
   	def __unicode__(self):
					return self.question
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

	was_published_recently.admin_order_field = 'pub_date'  #在管理界面中可以排序
	was_published_recently.boolean = True    #faulse&True  以图表显示
	was_published_recently.short_description = 'Published recently?'  #字段别名
	
	search_fields = ['question']

class Choice(models.Model):
	Poll = models.ForeignKey(Poll)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)	
	def __unicode__(self):
		return self.choice_text
