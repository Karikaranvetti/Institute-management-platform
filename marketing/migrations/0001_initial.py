# Generated by Django 3.1.5 on 2021-02-02 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(max_length=200, null=True)),
                ('titel', models.CharField(max_length=200, null=True)),
                ('info', models.CharField(max_length=500, null=True)),
                ('pic', models.ImageField(blank=True, default='defoult.jpg', null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('detiles', models.CharField(max_length=200, null=True)),
                ('img', models.ImageField(blank=True, default='defoult.jpg', null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('detiles', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('role', models.CharField(max_length=200, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='defoult.jpg', null=True, upload_to='pics')),
            ],
        ),
    ]
