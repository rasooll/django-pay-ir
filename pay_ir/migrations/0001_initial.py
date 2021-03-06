# Generated by Django 2.1.1 on 2018-09-26 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='نام و نام خانوادگی')),
                ('amount', models.BigIntegerField(verbose_name='مبلغ')),
                ('mobile', models.CharField(blank=True, max_length=11, null=True, verbose_name='شماره موبایل')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='توضیحات')),
                ('transid', models.IntegerField(verbose_name='شماره فاکتور')),
                ('status', models.BooleanField(default=False, verbose_name='وضعیت')),
                ('card_number', models.CharField(blank=True, max_length=18, null=True, verbose_name='شماره کارت')),
                ('trace_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='شماره پیگیری')),
                ('message', models.TextField(blank=True, null=True, verbose_name='پیام')),
                ('insert_date_time', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('payment_date_time', models.DateTimeField(auto_now=True, verbose_name='زمان پرداخت')),
            ],
        ),
    ]
