from django.urls import path
from zodiac import views

app_name = 'zodiac'

urlpatterns = [
    path('', views.ZodiacListView.as_view(), name='home'),
    path('sign/<slug:slug>', views.SignDetailView.as_view(), name='sign-detail'),
    path('contacts', views.ContactView.as_view(), name='contacts'),
    path('elements', views.ElementlView.as_view(), name='elements'),
    path('elements/<slug:slug>', views.ElementDetailView.as_view(), name='elements-detail'),

]
