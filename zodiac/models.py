from django.db import models
from django.urls import reverse


class Element(models.Model):
    'Модель Стихия'
    title = models.CharField('Название', max_length=60)
    character = models.TextField('Особенности характера', blank=True)
    image = models.ImageField(upload_to='elements', blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('zodiac:element-detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Стихия'
        verbose_name_plural = 'Стихии'
        ordering = ['title']


class Zodiac(models.Model):
    'Модель гороскоп'
    title = models.CharField('Название', max_length=60)
    description = models.TextField('Описание', blank=True)
    img = models.ImageField(upload_to='image/%Y')
    element = models.ForeignKey(Element, on_delete=models.CASCADE, verbose_name='Стихия')
    date_sign = models.TextField('Дата знака', blank=True)
    slug = models.SlugField(unique=True, max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('zodiac:sign-detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Знак зодиака'
        verbose_name_plural = 'Знаки зодиака'
        ordering = ['title']
        db_table = 'zodiac_table'