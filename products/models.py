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
	MEID = models.CharField('Meter equipment identifier',max_length=120,null=False,blank=True,primary_key=True)
	DType  = models.CharField('Device_type',max_length=120,null=True,blank=True)
	Commu_Method = models.CharField('Device_type',max_length=120,null=True,blank=True)
	D_Date = models.CharField('Delivery date',max_length=120,null=True,blank=True,help_text='例:20140721')
	Modem_IMEI = models.CharField('GPRS modem',max_length=120,null=True,blank=True)
	SIM_IMSI = models.CharField('SIM IMSI',max_length=120,null=True,blank=True)	
	SIM_ICC_id = models.CharField('SIM ICC_id',max_length=120,null=True,blank=True)
	IP_Address = models.CharField('IP address',max_length=120,null=True,blank=True)
	Firmware_Version  = models.CharField('firmware_version',max_length=120,null=True,blank=True)
	LLS_Secret = models.CharField('LLS_secret',max_length=120,null=True,blank=True)
	HLS_Secret = models.CharField('HLS_secret',max_length=120,null=True,blank=True)
	Authentication_Key = models.CharField('Authentication_key',max_length=120,null=True,blank=True)
	Encryption_Key = models.CharField('Encryption_key',max_length=120,null=True,blank=True)
	#pub_date = models.DateTimeField('date published')

	def save(self, *args, **kwargs):	
	        if self.SIM_ICC_id == "":
	            self.SIM_ICC_id = None# Yoko shall never have her own blog!
	            self.Modem_IMEI = None
	        # else:
	            super(Product, self).save(*args, **kwargs)


															#Poll动作
#   	def __unicode__(self):
#					return self.MEID
#	def was_published_recently(self):
#		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

#	was_published_recently.admin_order_field = 'pub_date'  #在管理界面中可以排序
#	was_published_recently.boolean = True    #faulse&True  以图表显示
#	was_published_recently.short_description = 'Published recently?'  #字段别名
	
class NullCharField(models.Field):
    def db_type(self, connection):
        return 'mytype'