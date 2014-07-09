# -*- coding: utf-8 -*-
from django.contrib import admin
from polls.models import Poll,Choice
from products.models import Product
# Register your models here.


##Product管理表显示设置
class ProductAdmin(admin.ModelAdmin):
#list全记录操作     
		list_display = ('MEID','DType','Commu_Method',
			'D_Date','Modem_IMEI','SIM_IMSI','SIM_ICC_id','IP_Address','Firmware_Version',
			'LLS_Secret','HLS_Secret','Authentication_Key','Encryption_Key')
		#list_display=('field分组名称','表字段'，'表动作' ）  	




#单记录操作	
		search_fields = ['MEID','D_Date']
		list_filter = ['D_Date']
admin.site.register(Product,ProductAdmin)
