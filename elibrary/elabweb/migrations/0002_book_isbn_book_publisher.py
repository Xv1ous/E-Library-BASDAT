# Generated by Django 4.2.7 on 2023-11-21 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elabweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.IntegerField(default=1111111111111),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.CharField(default='Unknown', max_length=100),
        ),
    ]
