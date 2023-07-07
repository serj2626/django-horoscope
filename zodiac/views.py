from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from zodiac.models import Zodiac, Element
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy


class ZodiacListView(ListView):
    'Стартовая страница/ все знаки задиака'
    model = Zodiac
    template_name = 'zodiac/home.html'
    extra_context = {'title': 'Гороскоп'}


class SignDetailView(DetailView):
    '''Знак Зодиака'''
    model = Zodiac
    template_name = 'Zodiac/detail.html'


class ContactView(View):
    '''Контакты'''

    def get(self, request):
        return render(request, 'zodiac/contacts.html')


class ElementlView(ListView):
    '''Страница со всеми Стихиями'''

    model = Element
    template_name = 'zodiac/elements.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Стихии'
        return context


class ElementDetailView(DetailView):
    '''Страница с одной стихией'''

    model = Element
    template_name = 'zodiac/elements_detail.html'
