from django.contrib import admin
from demoapp.models import *
# Register your models here.
class PuneJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','mobno']

class BangloreJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','mobno']

class ChennaiJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','mobno']

class HydrabadJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','mobno']

admin.site.register(PuneJobs,PuneJobsAdmin)
admin.site.register(BangloreJobs,BangloreJobsAdmin)
admin.site.register(ChennaiJobs,ChennaiJobsAdmin)
admin.site.register(HydrabadJobs,HydrabadJobsAdmin)

#username- gayatri
#password -Gaya@128
