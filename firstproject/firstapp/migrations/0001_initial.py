# Generated by Django 2.0.7 on 2019-11-20 17:28

from django.db import migrations, models
import firstapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, verbose_name=firstapp.models.Webpage)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_name', models.CharField(max_length=264, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Webpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=264, verbose_name=firstapp.models.Topic)),
                ('name', models.CharField(max_length=264, unique=True)),
                ('url', models.URLField(unique=True)),
            ],
        ),
    ]
