# Generated by Django 2.0b1 on 2017-10-27 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interfaceTest', '0002_auto_20171027_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interfacemodel',
            name='header',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
