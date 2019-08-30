from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display=['title','timestamp']
	list_filter = ['timestamp'] # TO FIND SOMETHING BY TIMESTAMP
	list_display_links = ['timestamp']	# USE TO CHANGE THE CLICKABLE LINK IN ADMIN POST
	list_editable = ['title'] #TO EDIT THE TITLE
	search_fields = ['title']


admin.site.register(Post,PostModelAdmin)