# Generated by Django 2.0b1 on 2017-11-15 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interfaceTest', '0013_interfacemodel_is_delete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interfacemodel',
            name='method',
            field=models.CharField(choices=[('POST', 'POST请求'), ('GET', 'GET请求')], max_length=20),
        ),
        migrations.AlterField(
            model_name='interfacemodel',
            name='system_belong',
            field=models.IntegerField(choices=[(1, '麦芽APP'), (2, '麦芽后台'), (3, '征信平台'), (4, '反欺诈平台'), (5, '贷后系统')]),
        ),
    ]