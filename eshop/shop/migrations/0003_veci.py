# Generated by Django 2.2a1 on 2019-04-08 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_delete_completed_survey'),
    ]

    operations = [
        migrations.CreateModel(
            name='veci',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('cena', models.CharField(default='', max_length=10)),
                ('obrazek', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
