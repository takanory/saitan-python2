from django.shortcuts import render

from .models import Pizza

def index(request):
    """ピザ屋のホームページ"""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """すべてのピザを表示するページ"""
    pizzas = Pizza.objects.all()
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    """個々のピザの情報を表示するページ"""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()

    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/pizza.html', context)