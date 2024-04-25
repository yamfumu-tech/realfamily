from .cart import Cart
from .models import Footer

def cart(request):
    return {'cart': Cart(request)}

def footer(request):
    footer = Footer.objects.first()  # Fetch the first footer object
    return {'footer': footer}