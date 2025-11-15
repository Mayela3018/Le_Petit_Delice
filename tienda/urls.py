from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path('', views.home, name='home'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('carrito/', views.ver_carrito, name='carrito'),
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
]
