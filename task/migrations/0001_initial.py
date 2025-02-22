# Generated by Django 5.0.7 on 2024-07-12 13:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('point', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='sprint_created_by', to='employee.employee')),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sprint_modified_by', to='employee.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('due_date', models.DateField()),
                ('description', models.TextField(null=True)),
                ('status', models.IntegerField(choices=[(1, 'TODO'), (2, 'INPROGRESS'), (3, 'REVIEW'), (4, 'COMPLETE'), (5, 'ONHOLD'), (6, 'BACKLOG')], default=1)),
                ('type', models.IntegerField(choices=[(1, 'FEATURES'), (2, 'BUG'), (3, 'TEST'), (4, 'QA'), (5, 'DOCUMENTATION'), (6, 'OTHER')], default=1)),
                ('points', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('assigned_to', models.ManyToManyField(to='employee.employee')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='task_created_by', to='employee.employee')),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task_modified_by', to='employee.employee')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='project.project')),
                ('sprint', models.ManyToManyField(to='task.sprint')),
            ],
        ),
        migrations.CreateModel(
            name='TaskComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('file', models.FileField(blank=True, null=True, upload_to='file')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='task_comment_created', to='employee.employee')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.employee')),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task_comment_modfied', to='employee.employee')),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='task.task')),
            ],
        ),
    ]
