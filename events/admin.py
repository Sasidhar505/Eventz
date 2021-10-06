from django.contrib import admin
from . models import *
# Register your models here.
class Eventadmin(admin.ModelAdmin):
    list_display = ('title','date','location')
    list_filter = ( 'location','date')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Event , Eventadmin)  
admin.site.register(Location)
admin.site.register(Participant)
admin.site.register(Schedule)