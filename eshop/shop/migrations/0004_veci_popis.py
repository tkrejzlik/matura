# Generated by Django 2.2a1 on 2019-04-12 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_veci'),
    ]

    operations = [
        migrations.AddField(
            model_name='veci',
            name='popis',
            field=models.CharField(default='', max_length=200),
        ),
    ]
