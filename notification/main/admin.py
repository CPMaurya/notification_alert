from django.contrib import admin
from main.models import MainModel

# Register your models here.

class MainAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'first_name', 'last_name', 
        'mobile', 'notification_time']

admin.site.register(MainModel, MainAdmin)