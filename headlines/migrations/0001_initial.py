# Generated by Django 2.2.1 on 2019-06-23 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Headline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=128)),
                ('_datePosted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
