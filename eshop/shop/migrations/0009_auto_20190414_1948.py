# Generated by Django 2.2a1 on 2019-04-14 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20190414_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veci',
            name='cena',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
