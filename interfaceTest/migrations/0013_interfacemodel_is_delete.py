# Generated by Django 2.0b1 on 2017-11-15 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interfaceTest', '0012_auto_20171114_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='interfacemodel',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]