from django.conf.urls import url
from django.contrib import admin
from .views import (
	post_list,
	post_create,
	post_detail,
	post_delete,
	post_update,
	)

urlpatterns=[

	url(r'^$',post_list,name="list"),
	url(r'^create/$',post_create,name="post_create"),
	url(r'^(?P<slug>[\w-]+)/$',post_detail,name="details"),
	url(r'^(?P<slug>[\w-]+)/edit/$',post_update,name="post_update"),
	url(r'^(?P<slug>[\w-]+)/delete/$',post_delete,name="post_delete"),

 
]