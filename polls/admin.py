# -*- coding: utf-8 -*-
from django.contrib import admin  #导入总admin
from polls.models import Poll,Choice

# Register your models here.


#StackedInline  是一个堆积起来的表（类）   类名可以随便填写
class ChoiceInline(admin.TabularInline):
		model = Choice
		extra = 3

#Poll表显示设置
class PollAAAAAdmin(admin.ModelAdmin):
#list全记录操作
		list_display = ('question', 'pub_date', 'was_published_recently')
		#list_display=('field分组名称','表字段'，'表动作' ）  	
#单记录操作	
#区域集合
		fieldsets = [

        ('投票主题',               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
		inlines =  [ChoiceInline]
		list_filter = ['pub_date']
		search_fields = ['question']





#在admin首页中添加Poll管理模块（首页显示）
#以及管理模块的界面(PollAAAAAdmin)
#这两个是有联系的所以打包注册
admin.site.register(Poll,PollAAAAAdmin)


#下面一句与默认管理表对接
#admin.site.register(Poll)



