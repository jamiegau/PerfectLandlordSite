# Generated by Django 4.1.6 on 2023-02-27 13:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=30)),
                ('slug', models.SlugField()),
                ('address', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('room', models.IntegerField(default=0)),
                ('bathroom', models.IntegerField(default=0)),
                ('furnished', models.CharField(default='', max_length=30)),
                ('airConditioning', models.CharField(default=0, max_length=30)),
                ('gym', models.CharField(default=0, max_length=30)),
                ('pool', models.CharField(default=0, max_length=30)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('landlord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date_added',),
            },
        ),
        migrations.CreateModel(
            name='SavedProperty',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.property')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('property', 'tenant')},
            },
        ),
    ]
