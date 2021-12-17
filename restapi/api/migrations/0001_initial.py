# Generated by Django 3.2.9 on 2021-12-17 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oksi', models.CharField(blank=True, max_length=100)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=150, unique=True)),
            ],
        ),
    ]
