# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 04:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppDeployOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_tab', models.BooleanField(default=True)),
                ('account_tab', models.BooleanField(default=True)),
                ('policy_tab', models.BooleanField(default=True)),
                ('app_persist_tab', models.BooleanField(default=True)),
                ('db_persist_tab', models.BooleanField(default=True)),
                ('resources_tab', models.BooleanField(default=True)),
                ('service_tab', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='AppImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagename', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='AppName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appname', models.CharField(max_length=32)),
                ('appdetails', models.CharField(max_length=1000)),
                ('thumbnail_path', models.CharField(default=None, max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='AppRepository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apprepository', models.CharField(max_length=32)),
                ('app_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dao.AppImage')),
            ],
        ),
        migrations.CreateModel(
            name='AppType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typename', models.CharField(default=None, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='AppVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appversion', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30, null=True)),
                ('gender', models.CharField(default=None, max_length=10)),
                ('age', models.IntegerField(default=None)),
                ('position', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grouptype', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='userdetails',
            name='group_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dao.UserGroups'),
        ),
        migrations.AddField(
            model_name='appname',
            name='all_apptypes',
            field=models.ManyToManyField(blank=True, null=True, to='dao.AppType'),
        ),
        migrations.AddField(
            model_name='appname',
            name='app_repository',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dao.AppRepository'),
        ),
        migrations.AddField(
            model_name='appimage',
            name='app_version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dao.AppVersion'),
        ),
        migrations.AddField(
            model_name='appdeployoption',
            name='app_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dao.AppName'),
        ),
    ]
