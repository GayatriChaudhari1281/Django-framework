from django.contrib import admin
from blog.models import Post,Comments
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status']
    prepopulated_fields={'slug':('title',)}#to add the content of title to slug simultaneously
    list_filter=('status','author')#to show the post according to the status
    search_fields=('title','body')
    raw_id_fields=('author',)
    date_hierarchy='publish'#the word publish written in slug field
    ordering=['status','publish']#if status is same then data will sortaccording to publish date_hierarchy
    #date_hierarchy and ordering are substitute of each other
class CommentsAdmin(admin.ModelAdmin):
    list_display=('name','email','post','body','created','updated','active')
    list_filter=('active','created','updated')
    search_fields=('name','email','body')
admin.site.register(Post,PostAdmin)
admin.site.register(Comments,CommentsAdmin)
