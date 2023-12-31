# Generated by Django 3.2.13 on 2023-05-28 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Название')),
                ('character', models.TextField(blank=True, verbose_name='Особенности характера')),
                ('image', models.ImageField(blank=True, null=True, upload_to='elements')),
                ('url', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Стихия',
                'verbose_name_plural': 'Стихии',
            },
        ),
        migrations.CreateModel(
            name='Zodiac',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('img', models.ImageField(upload_to='image/%Y')),
                ('date_sign', models.TextField(blank=True, verbose_name='Дата знака')),
                ('url', models.SlugField(max_length=100, unique=True)),
                ('element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zodiac.element', verbose_name='Стихия')),
            ],
            options={
                'verbose_name': 'Знак зодиака',
                'verbose_name_plural': 'Знаки зодиака',
            },
        ),
    ]
