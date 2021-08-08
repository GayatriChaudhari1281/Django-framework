from django.contrib import admin

# Register your models here.
from demoapp.models import Book
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display=['PNR_NO','title','author']

admin.site.register(Book,BookAdmin)
