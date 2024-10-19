from django.shortcuts import render

from .models import Meal

def index(request):
    """食事プランナーのホームページ"""
    return render(request, 'meal_plans/index.html')

def meals(request):
    """すべての献立を表示するページ"""
    meals = Meal.objects.all()
    context = {'meals': meals}
    return render(request, 'meal_plans/meals.html', context)

def meal(request, meal_id):
    """個別の献立を表示するページ"""
    meal = Meal.objects.get(id=meal_id)
    meal_items = meal.mealitem_set.all()

    context = {'meal': meal, 'meal_items': meal_items}
    return render(request, 'meal_plans/meal.html', context)