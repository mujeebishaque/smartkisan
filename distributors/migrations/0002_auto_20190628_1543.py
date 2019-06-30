# Generated by Django 2.2.1 on 2019-06-28 10:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('distributors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='distributor',
            name='mobileNumber',
            field=models.CharField(default=django.utils.timezone.now, max_length=15, verbose_name='Mobile Number'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='distributor',
            name='shopName',
            field=models.CharField(default=1, max_length=32, verbose_name='Shop Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='distributor',
            name='dealsNature',
            field=models.CharField(choices=[('wholesale', 'Wholesale Dealings'), ('Retailer', 'Inidividual Items Dealings'), ('Individual', 'Small Business')], max_length=128, verbose_name='Deal Nature'),
        ),
    ]