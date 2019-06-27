from django.contrib import admin
from discounteditem import models
# Register your models here.

class DiscountedItemAdmin(admin.ModelAdmin):

    list_display = ['itemTitle', 'itemPrice', 'itemNature', 'isAvailable']
    list_filter = ['isAvailable', 'itemPrice']
    search = ['itemTitle']

    class Meta:
        verbose_name = 'Discounted Items'

admin.site.register(models.DiscountedItem, DiscountedItemAdmin)