from django.contrib import admin
from .models import Element, Zodiac


@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    list_display = ('title', 'character')


@admin.register(Zodiac)
class ZodiacAdmin(admin.ModelAdmin):
    list_display = ('title', 'element', 'date_sign', 'element', 'slug')
