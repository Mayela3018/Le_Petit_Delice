from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto

def home(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/home.html', {'productos': productos})


def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'tienda/detalle_producto.html', {'producto': producto})


# ---------- CARRITO ----------
def _get_cart(request):
    return request.session.get('carrito', {})

def _save_cart(request, cart):
    request.session['carrito'] = cart
    request.session.modified = True

def agregar_al_carrito(request, producto_id):
    cart = _get_cart(request)
    pid = str(producto_id)

    cart[pid] = cart.get(pid, 0) + 1

    _save_cart(request, cart)
    return redirect('tienda:carrito')

def ver_carrito(request):
    cart = _get_cart(request)
    items = []
    total = 0

    for pid, cantidad in cart.items():
        producto = get_object_or_404(Producto, pk=int(pid))
        subtotal = producto.precio * cantidad
        total += subtotal

        items.append({
            'producto': producto,
            'cantidad': cantidad,
            'subtotal': subtotal,
        })

    return render(request, 'tienda/carrito.html', {
        'items': items,
        'total': total,
    })
