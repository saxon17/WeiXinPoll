# -*- coding: utf-8 -*-
import datetime
from django.utils import timezone
from django.db import models
'''# Create your models here.
class Poll(models.Model):									#表内容
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')   #date published是在admin中
														#显示的pub_date的别名
											'''

class Product(models.Model):
	MEID = models.CharField(max_length=120,null=False,blank=True,primary_key=True)
	DType  = models.CharField(max_length=120,null=False,blank=True)
	Commu_Method = models.CharField(max_length=120,null=False,blank=True)
	D_Date = models.CharField(max_length=120,null=False,blank=True)
	Modem_IMEI = models.CharField(max_length=10,null=True,blank=True)
	SIM_IMSI = models.CharField(max_length=120,null=False,blank=True)
	SIM_ICC_id = models.CharField(max_length=120,null=True,blank=True)
	IP_Address = models.CharField(max_length=120,null=True,blank=True)
	Firmware_Version  = models.CharField(max_length=120,null=True,blank=True)
	LLS_Secret = models.CharField(max_length=120,null=True,blank=True)
	HLS_Secret = models.CharField(max_length=120,null=True,blank=True)
	Authentication_Key = models.CharField(max_length=120,null=True,blank=True)
	Encryption_Key = models.CharField(max_length=120,null=True,blank=True)
	#pub_date = models.DateTimeField('date published')



															#Poll动作
#   	def __unicode__(self):
#					return self.MEID
#	def was_published_recently(self):
#		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

#	was_published_recently.admin_order_field = 'pub_date'  #在管理界面中可以排序
#	was_published_recently.boolean = True    #faulse&True  以图表显示
#	was_published_recently.short_description = 'Published recently?'  #字段别名
	
