from django.contrib import admin
from demoapp.models import Icecream
# Register your models here.
class icecream_Admin(admin.ModelAdmin):
    list_display=['id','flavour','ingrediants','company','price','expdate']

admin.site.register(Icecream,icecream_Admin)


 #username-gayatri
 #password=Gaya@128
