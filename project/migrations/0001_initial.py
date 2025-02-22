# Generated by Django 5.0.7 on 2024-07-12 13:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        ('employee', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('image', models.ImageField(blank=True, null=True, upload_to='project/images')),
                ('priority', models.IntegerField(choices=[(1, 'CRITICAL'), (2, 'HIGH'), (3, 'NORMAL'), (4, 'LOW')], default=4)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(1, 'ONGOING'), (2, 'COMPLETED'), (3, 'ONHOLD'), (4, 'ABORT')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('deadline', models.DateTimeField()),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.client')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_created_field', to=settings.AUTH_USER_MODEL)),
                ('employee', models.ManyToManyField(to='employee.employee')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_modified_field', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
