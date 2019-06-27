from django.db import models

# Create your models here.

class Rate(models.Model):
    
    itemName = models.CharField('Item', max_length=128)
    itemRate = models.PositiveIntegerField('Rate', default=0)
    quantity = models.PositiveIntegerField('Total Quantity', default=0)

    datePosted = models.DateTimeField('Date Posted', auto_now_add=True)

    def __str__(self):
        return self.itemName