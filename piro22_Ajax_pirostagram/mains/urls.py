from django.urls import path
from . import views

app_name = 'mains'

urlpatterns = [
    path('', views.main, name='main'),
]