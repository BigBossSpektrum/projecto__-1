from django.shortcuts import render
from .models import Pizza


pizza_list =[ {
    'name': 'Barbacoa Gourmet',
    'description': 'Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta).',
    'price': '10.99$',
    'discounted_price': '7.99$',
    'img': '{% static "img/pizza_1.png" %}'
},
{
    'name': 'Hawaiana',
    'description': 'Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta).',
    'price': '21.00$',
    'discounted_price': '14.99$',
},
{
    'name': 'Peperoni',
    'description': 'Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta).',
    'price': '14.99$',
    'discounted_price': '9.99$',
},
{
    'name': 'Napolitana',
    'description': 'Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta).',
    'price': '10.99$',
    'discounted_price': '7.99$',
},
{
    'name': 'Jalapeña',
    'description': 'Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta).',
    'price': '11.99$',
    'discounted_price': '8.99$',
},
]

# Create your views here.
def home(request):
    pizzas = Pizza.objects.all()
    context = {
        'pizzas': pizza_list
    }
    
    return render(request, 'applicacion_1/home.html', context)

def pedidos(request):
    return render(request, 'applicacion_1/pedidos.html', {'title': 'Pedidos'})

def pizza_gourmet(request):
    return render (request, 'applicacion_1/pizza_gourmet.html', {'title': 'Pizza Gourmet'})