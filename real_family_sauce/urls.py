from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('product/<int:id>/', views.detail, name='detail'),
    path('cart/', views.cart, name="cart"),
    path('cart_item/', views.cart_item, name="cart_item"),
    path('update_cart/', views.update_cart, name="update_cart"),
    path('process_order/', views.processOrder, name="process_order"),
    path('blogs/', views.blog, name="blog"),
    path('blogs/<int:id>/', views.single_blog, name="single_blog"),
    path('contacts/', views.contacts, name="contacts"),
    path('about/', views.about, name="about"),
    path('faq/', views.faq, name="faq"),
    path('404/', views.not_found, name="404"),
    path('products/', views.products, name="products"),
    path('checkout/', views.check, name="check"),
    path('subscribe/', views.subscribe, name="subscribe"),
    path('message/', views.message, name="message"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

handler404 = 'shop.views.not_found'
