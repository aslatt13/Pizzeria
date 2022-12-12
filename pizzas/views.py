from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html')

def menu(request):
    menu = Pizza.objects.all

    context = {'pizza_types':menu}
    return render(request, 'pizzas/menu.html', context)



def pizza(request, topic_id):
    p = Pizza.objects.get(id=topic_id)

    entries = Topping.objects.filter(pizza=p)
    context = {'pizza':p, 'entries':entries}

    return render(request, 'pizzas/pizza.html', context)