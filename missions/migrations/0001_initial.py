# Generated by Django 5.1.3 on 2024-11-17 16:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('spy_cat_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('notes', models.TextField()),
                ('isComplete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('isComplete', models.BooleanField(default=False)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spy_cat_app.spycat')),
                ('targets', models.ManyToManyField(to='missions.target')),
            ],
        ),
    ]