# Generated by Django 3.1.7 on 2021-03-07 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listapp', '0004_auto_20210306_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='lista',
            name='nameid',
            field=models.CharField(default=0, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lista',
            name='amount',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='lista',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
