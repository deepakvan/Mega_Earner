# Generated by Django 4.1 on 2022-08-06 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('androapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='email',
            field=models.CharField(default='', max_length=200),
        ),
    ]