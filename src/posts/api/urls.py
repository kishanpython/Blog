from django.conf.urls import url
from django.contrib import admin
from .views import (
		PostListAPIView,
	)

urlpatterns=[

	url(r'^$',PostListAPIView.as_view(), name="list"),
	# url(r'^create/$',post_create),
	# url(r'^(?P<slug>[\w-]+)/$',post_detail,name="details"),
	# url(r'^(?P<slug>[\w-]+)/edit/$',post_update),
	# url(r'^(?P<slug>[\w-]+)/delete/$',post_delete),

 
]