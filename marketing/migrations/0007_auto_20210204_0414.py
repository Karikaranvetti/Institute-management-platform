# Generated by Django 3.1.5 on 2021-02-04 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0006_auto_20210204_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='facebook',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='linkedin',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='twitter',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
