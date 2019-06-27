# Generated by Django 2.2.1 on 2019-06-24 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discounteditem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discounteditem',
            name='isAvailable',
            field=models.BooleanField(default=False, verbose_name='Item Availability'),
        ),
        migrations.AlterField(
            model_name='discounteditem',
            name='itemNature',
            field=models.CharField(blank=True, default='Agricultural Item', help_text='Insecticide Or Pesticide?', max_length=32, verbose_name='Item Nature'),
        ),
        migrations.AlterField(
            model_name='discounteditem',
            name='itemTitle',
            field=models.CharField(max_length=64, verbose_name='Item Name'),
        ),
    ]