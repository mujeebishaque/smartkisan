from django.contrib import admin
from headlines import models
# Register your models here.
class HeadlineAdmin(admin.ModelAdmin):
    list_display = ['headline', 'datePosted']
    list_filter = ['datePosted']

    search_fields = ['headline']

admin.site.register(models.Headline, HeadlineAdmin)