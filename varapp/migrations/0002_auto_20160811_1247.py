# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-11 12:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('varapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.CharField(max_length=50, null=True)),
                ('updated_by', models.CharField(max_length=50, null=True)),
                ('is_active', models.IntegerField(default=1)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('source', models.CharField(max_length=255, null=True)),
                ('source_version', models.CharField(max_length=255, null=True)),
                ('annotation', models.CharField(max_length=255, null=True)),
                ('annotation_version', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'annotation',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Bam',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.CharField(max_length=50, null=True)),
                ('updated_by', models.CharField(max_length=50, null=True)),
                ('is_active', models.IntegerField(default=1)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('filename', models.CharField(max_length=255, null=True)),
                ('key', models.CharField(max_length=255, null=True)),
                ('sample', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'bam',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Bookmarks',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.CharField(max_length=50, null=True)),
                ('updated_by', models.CharField(max_length=50, null=True)),
                ('is_active', models.IntegerField(default=1)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('query', models.TextField()),
                ('description', models.CharField(max_length=255)),
                ('long_description', models.TextField(default='')),
            ],
            options={
                'db_table': 'bookmarks',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DbAccess',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.CharField(max_length=50, null=True)),
                ('updated_by', models.CharField(max_length=50, null=True)),
                ('is_active', models.IntegerField(default=1)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'db_accesses',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.CharField(max_length=50, null=True)),
                ('updated_by', models.CharField(max_length=50, null=True)),
                ('is_active', models.IntegerField(default=1)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('session_start', models.DateTimeField()),
                ('url', models.TextField()),
                ('query', models.TextField(default='')),
                ('description', models.CharField(max_length=255)),
                ('long_description', models.TextField(default='')),
                ('ip_address', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'history',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.CharField(max_length=50, null=True)),
                ('updated_by', models.CharField(max_length=50, null=True)),
                ('is_active', models.IntegerField(default=1)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('institution', models.CharField(max_length=255, null=True)),
                ('street', models.CharField(max_length=255, null=True)),
                ('city', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=30, null=True)),
                ('is_laboratory', models.IntegerField(null=True)),
                ('laboratory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='varapp.People')),
            ],
            options={
                'db_table': 'people',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.CharField(max_length=50, null=True)),
                ('updated_by', models.CharField(max_length=50, null=True)),
                ('is_active', models.IntegerField(default=1)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('preferences', models.TextField(default='')),
                ('description', models.TextField(default='')),
            ],
            options={
                'db_table': 'preferences',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.CharField(max_length=50, null=True)),
                ('updated_by', models.CharField(max_length=50, null=True)),
                ('is_active', models.IntegerField(default=1)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('rank', models.IntegerField(null=True)),
                ('can_validate_user', models.IntegerField(default=0)),
                ('can_delete_user', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'roles',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.CharField(max_length=50, null=True)),
                ('updated_by', models.CharField(max_length=50, null=True)),
                ('is_active', models.IntegerField(default=1)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=25, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('salt', models.CharField(default='', max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=25)),
                ('activation_code', models.CharField(max_length=25, null=True)),
                ('is_password_reset', models.IntegerField(null=True)),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='varapp.People')),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='varapp.Roles')),
            ],
            options={
                'db_table': 'users',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='VariantsDb',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.CharField(max_length=50, null=True)),
                ('updated_by', models.CharField(max_length=50, null=True)),
                ('is_active', models.IntegerField(default=1)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('visible_name', models.CharField(max_length=255, null=True)),
                ('filename', models.CharField(max_length=255, null=True)),
                ('location', models.TextField(default='', null=True)),
                ('hash', models.CharField(max_length=255, null=True)),
                ('description', models.TextField(default='', null=True)),
                ('size', models.BigIntegerField(null=True)),
                ('parent_db_id', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'variants_db',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('varapp.variants',),
        ),
        migrations.AlterUniqueTogether(
            name='variantsdb',
            unique_together=set([('filename', 'hash')]),
        ),
        migrations.AddField(
            model_name='preferences',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='varapp.Users'),
        ),
        migrations.AddField(
            model_name='history',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='varapp.Users'),
        ),
        migrations.AddField(
            model_name='dbaccess',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='varapp.Users'),
        ),
        migrations.AddField(
            model_name='dbaccess',
            name='variants_db',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='varapp.VariantsDb'),
        ),
        migrations.AddField(
            model_name='bookmarks',
            name='db_access',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='varapp.DbAccess'),
        ),
        migrations.AddField(
            model_name='bam',
            name='variants_db',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='varapp.VariantsDb'),
        ),
        migrations.AddField(
            model_name='annotation',
            name='variants_db',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='varapp.VariantsDb'),
        ),
        migrations.AlterUniqueTogether(
            name='dbaccess',
            unique_together=set([('user', 'variants_db')]),
        ),
    ]
