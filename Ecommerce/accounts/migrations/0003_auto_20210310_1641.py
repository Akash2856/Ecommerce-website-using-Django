# Generated by Django 3.1.3 on 2021-03-10 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='orders',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='orders',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='orders',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='orders',
            name='items_json',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='orders',
            name='name',
            field=models.CharField(default='', max_length=90),
        ),
        migrations.AlterField(
            model_name='orders',
            name='state',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='orders',
            name='zip_code',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
