from django.contrib import admin
from distributors import models
# Register your models here.
class DistributorAdmin(admin.ModelAdmin):
    
    list_display  = ['name', 'age', 'experience', 'region', 'dealsNature']
    list_filter = ['region']

admin.site.register(models.Distributor, DistributorAdmin)