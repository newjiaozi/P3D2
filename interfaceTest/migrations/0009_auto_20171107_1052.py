# Generated by Django 2.0b1 on 2017-11-07 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interfaceTest', '0008_remove_interfacetestresult_interface'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultmodel',
            name='pass_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='resultmodel',
            name='sum_count',
            field=models.IntegerField(default=0),
        ),
    ]
