# Generated by Django 3.1.5 on 2021-02-04 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0009_auto_20210204_0509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='facebook',
            field=models.CharField(blank=True, default='NotFound', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='linkedin',
            field=models.CharField(blank=True, default='NotFound', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='twitter',
            field=models.CharField(blank=True, default='NotFound', max_length=200, null=True),
        ),
    ]