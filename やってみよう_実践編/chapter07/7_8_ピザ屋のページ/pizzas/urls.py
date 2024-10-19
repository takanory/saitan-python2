"""Defines URL patterns for pizzas."""

from django.urls import path

from . import views

app_name = 'pizzas'
urlpatterns = [
    # ホームページ
    path('', views.index, name='index'),
    # すべてのピザを表示するページ
    path('pizzas/', views.pizzas, name='pizzas'),
    # 個々のピザの詳細ページ
    path('pizza/<int:pizza_id>/', views.pizza, name='pizza'),
]