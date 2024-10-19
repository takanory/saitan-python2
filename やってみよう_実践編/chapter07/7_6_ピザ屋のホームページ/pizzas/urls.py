"""Defines URL patterns for pizzas."""

from django.urls import path

from . import views

app_name = 'pizzas'
urlpatterns = [
    # ホームページ
    path('', views.index, name='index'),
]