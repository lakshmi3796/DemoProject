from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *
admin.site.unregister(Group)

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'text', 'created_date',)

admin.site.register(Post, PostAdmin)

# admin.site.register(DemoUser)