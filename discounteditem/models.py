from django.db import models

# Create your models here.
class DiscountedItem(models.Model):
    
    itemTitle = models.CharField('Item Name', max_length=64, blank=False)
    itemNature = models.CharField('Item Nature', max_length=32, blank=True, default="Agricultural Item", help_text="Insecticide Or Pesticide?")
    itemPrice = models.PositiveIntegerField('Item Price', default=0)
    totalItems = models.PositiveIntegerField('Total Items', default=0)
    isAvailable = models.BooleanField('Item Availability', default=False)

    itemPosted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.itemTitle