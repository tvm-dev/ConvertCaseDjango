from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.convertCase, name='convertCase'),
    path('home', views.home, name='home'),
    path('tests', views.tests, name='tests'),
    path('privacy-policy', views.privacy, name='privacy'),
    path('terms', views.terms, name='terms'),

    
    
]