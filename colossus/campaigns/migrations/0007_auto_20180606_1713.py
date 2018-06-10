# Generated by Django 2.0.6 on 2018-06-06 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0006_auto_20180606_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='from_email',
            field=models.EmailField(max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='email',
            name='from_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='email',
            name='preview',
            field=models.CharField(blank=True, max_length=150, verbose_name='preview'),
        ),
    ]