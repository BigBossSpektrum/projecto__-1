from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pedidos/', views.pedidos, name='pedidos'),
    path('pizza_gourmet', views.pizza_gourmet, name='gourmet')
]   