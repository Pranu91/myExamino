
from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name='home'),
    path('createtest/<int:class_id>/',views.createtest,name='createtest'),
    path('test1/<int:class_id>/',views.test1,name='test1'),
    path('test1confirm/', views.test1confirm, name='test1confirm'),
    path('test2/<int:class_id>/', views.test2, name='test2'),
    path('test2confirm/', views.test2confirm, name='test2confirm'),
    path('test3/<int:class_id>/', views.test3, name='test3'),
    path('test3confirm/', views.test3confirm, name='test3confirm'),
    path('que1/', views.que1, name='que1'),
    path('que2/', views.que2, name='que2'),
    path('que3/', views.que3, name='que3'),
    path('que4/', views.que4, name='que4'),
    path('que5/', views.que5, name='que5'),
    path('scores/', views.scores, name='scores'),

    path('base/',views.base,name='base'),
    path('base1/', views.base1, name='base1'),
    path("about/", views.about, name='about'),
    path('pricing/', views.pricing, name='pricing'),



    path('contact/',views.contact,name='contact'), #yha hamesha piche slash lgta h or jo contact.html m url lga h wo best h for use
    path('create/', views.create, name='create'), #jinke page nhi hote unhe ese hi likhna hota h
    path('join/',views.join,name='join'),
    path('joinedclasses/',views.joinedclasses,name='joinedclasses'),
    path('startlearning/<int:class_id>/', views.startlearning, name='startlearning'),
    path('myclassroom/', views.myclassroom, name='myclassroom'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('login', views.handlelogin, name='handlelogin'),
    path('logout', views.handlelogout, name='handlelogout')

]
