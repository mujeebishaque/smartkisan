from django.contrib import admin
from rates.models import Rate
# Register your models here.

class RateAdmin(admin.ModelAdmin):
    
    list_display = ['itemName', 'itemRate', 'datePosted']


admin.site.register(Rate, RateAdmin)