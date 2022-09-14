from django.urls import path
from . import views
urlpatterns=[path(route='',view=views.home,name='home'),path(route='stu/',view=views.stu,name='student'),
             path(route='ad/',view=views.ad,name='ad'),path(route='stu/show/',view=views.show,name='show'),
             path(route='ad/log/',view=views.log,name='log'),path(route='ad/log/sh/',view=views.show,name='sh'),
             path(route='ad/log/del/',view=views.de,name='del'),path(route='ad/log/ins/',view=views.ins,name='ins'),
             path(route='ad/log/upt/',view=views.upt,name='upt'),path(route='ad/reg/',view=views.reg,name='reg'),
             path(route='ad/reg/s/',view=views.s,name='s')]
