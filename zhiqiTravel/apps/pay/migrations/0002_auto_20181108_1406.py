# Generated by Django 2.1.2 on 2018-11-08 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsordersmaintable',
            name='order_num',
            field=models.CharField(max_length=25, verbose_name='订单号'),
        ),
        migrations.AlterField(
            model_name='orderitems',
            name='order_num',
            field=models.CharField(max_length=25, verbose_name='订单号'),
        ),
    ]
