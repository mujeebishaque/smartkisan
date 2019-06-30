from django.db import models

DISTRIBUTOR_TYPES = [
    ('wholesale', 'Wholesale Dealings'),
    ('Retailer', 'Inidividual Items Dealings'),
    ('Individual', 'Small Business'),
]

# Create your models here.
class Distributor(models.Model):

    name = models.CharField(max_length=128)
    age  = models.PositiveIntegerField(default=None)
    region = models.CharField('Distribution Region', default='Punjab', max_length=128)

    experience = models.PositiveIntegerField(blank=False)
    dealsNature = models.CharField('Deal Nature', max_length=128, choices = DISTRIBUTOR_TYPES)
    mobileNumber = models.CharField('Mobile Number', max_length=15)
    shopName = models.CharField('Shop Name', max_length=32)

    def __str__(self):
        return self.name 