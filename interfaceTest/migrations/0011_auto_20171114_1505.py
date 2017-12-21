# Generated by Django 2.0b1 on 2017-11-14 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interfaceTest', '0010_auto_20171108_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='interfacetestresult',
            name='interfaceModel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='interfaceTest.InterfaceModel'),
        ),
        migrations.AlterField(
            model_name='interfacemodel',
            name='method',
            field=models.CharField(choices=[(1, '麦芽APP'), (2, '麦芽后台'), (3, '征信平台'), (4, '反欺诈平台'), (5, '贷后系统')], max_length=20),
        ),
        migrations.AlterField(
            model_name='interfacemodel',
            name='system_belong',
            field=models.IntegerField(choices=[('POST', 'POST请求'), ('GET', 'GET请求')]),
        ),
    ]