from django.shortcuts import render

def index(request):
    """ピザ屋のホームページ"""
    return render(request, 'pizzas/index.html')
