from django.contrib import admin

# Register your models here.

from . models import *


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",),}
    list_display=['title','date','author']
    list_filter=['title','date',]

class CommentAdmin(admin.ModelAdmin):
    list_display=['first_name','email']    

admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(comment,CommentAdmin)
