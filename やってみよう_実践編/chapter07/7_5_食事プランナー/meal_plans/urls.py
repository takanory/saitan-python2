"""meal_plansのURLパターンの定義"""

from django.urls import path

from . import views

app_name = 'meal_plans'
urlpatterns = [
    # ホームページ
    path('', views.index, name='index'),
    # すべての献立を表示するページ
    path('meals/', views.meals, name='meals'),
    # 個別の献立詳細ページ
    path('meal/<int:meal_id>/', views.meal, name='meal'),
]