# Generated by Django 2.0.1 on 2019-07-10 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20190710_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.IntegerField(choices=[(1, '前端组'), (2, '后台组'), (3, '运维组'), (4, 'UI组'), (5, '产品经理组'), (6, '其他')], unique=True, verbose_name='名称'),
        ),
    ]
