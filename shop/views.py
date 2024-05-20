from django.conf import settings
from django.shortcuts import get_object_or_404, render
from .models import *
from django.core.paginator import Paginator
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.http import JsonResponse
import json
from .utils import *
from .cart import Cart
from django.contrib import messages


# Create your views here.
def index(request):
    product_objects = Products.objects.order_by('-id')[:6]
    details = Home.objects.first()
    testimanials = Testimonial.objects.all()
    blogs = Blog.objects.order_by('-date')[:3]
    most_viewed_blog = get_most_viewed_blog_post()
    sub_img = Subscription_image.objects.first()

#search code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)
    else:
        product_objects = Products.objects.order_by('-id')[:6]

#paginator code
    paginator = Paginator(product_objects, 8)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)
    nums = "a" * product_objects.paginator.num_pages

    return render(request, 'shop/index.html',{
        'product_objects': product_objects, 'nums':nums, 'details': details, 'test':testimanials, 'blogs':blogs, 'most':most_viewed_blog, 'sub':sub_img
    })
 
def detail(request, id):
    product_object = Products.objects.get(id=id)
    return render(request, 'shop/detail.html', {"product_object": product_object,})


def cart(request):
    data = Cart(request)
    context = { 'cart': data}
    return render(request, 'shop/cart.html',context)
    

def processOrder(request):
    cart = Cart(request)
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('Name')
        r_email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        company = request.POST.get('company')

        # Get order items and total order
        order_items = json.loads(request.POST.get('order_items'))
        total_order = request.POST.get('total_order')

        from_email = settings.EMAIL_HOST_USER
        
        html_content = render_to_string('shop/email_template.html', {'name':name, 'items': order_items, 'total':total_order})
        text = strip_tags(html_content)
        email = EmailMultiAlternatives(
            'Order Request',
            text,
            from_email,
            [r_email]
        )
        email.attach_alternative(html_content, 'text/html')
        email.send()

        order = Order_request.objects.create(
            customer=name,
            email=r_email,
            phone=phone,
            total=total_order,
            items=json.dumps(order_items),  # Convert to JSON string
            order_total=total_order
        )
        cart.clear()
        messages.success(request, 'Order request created successifully!!')
        response =  JsonResponse({'cart': 'order complete'})
        return response

def cart_item(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        prod = get_object_or_404(Products, id=product_id)
        cart.add(product=prod, qty = product_qty)
        cartqty = cart.__len__()
        response =  JsonResponse({'cart':cartqty})
        return response
    
def update_cart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'add':
        product_id = int(request.POST.get('productid'))
        #product_qty = int(request.POST.get('productqty'))
        prod = get_object_or_404(Products, id=product_id)
        cart.add_cart(product=prod)
        i = cart.get_total_price()
        cartqty = cart.__len__()
        response =  JsonResponse({'price':str(i), 'items': str(cartqty)})
       
    elif request.POST.get('action') == 'remove':
        product_id = int(request.POST.get('productid'))
        prod = get_object_or_404(Products, id=product_id)
        cart.delete_cart(product=prod)
        qt = cart.get_qty(product=prod)
        cartqty = cart.__len__()
        i = cart.get_total_price()
        response =  JsonResponse({'price':str(i), 'items': str(cartqty), 'qty': qt})
    elif request.POST.get('action') == 'delete':
        product_id = int(request.POST.get('productid'))
        prod = get_object_or_404(Products, id=product_id)
        cart.delete_item(product=prod)
        cartqty = cart.__len__()
        i = cart.get_total_price()
        response =  JsonResponse({'price':str(i), 'items': str(cartqty)})
    return response

def blog(request):
    blogs = Blog.objects.order_by('-id')
    details = Blogs_page.objects.first()
    sub_img = Subscription_image.objects.first()
    paginator = Paginator(blogs, 6)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    nums = "a" * blogs.paginator.num_pages
    return render(request, 'shop/blog.html', {'blogs':blogs, 'nums':nums, 'details':details, 'sub':sub_img})

def single_blog(request, id):
    blog = Blog.objects.get(id=id)
    blog.views += 1
    blog.save()
    return render(request, 'shop/single-blog.html', {'blog':blog})

def contacts(request):
    details = Contact.objects.first()
    return render(request, 'shop/contacts.html', {'details':details})

def about(request):
    about = About.objects.first()
    testimanials = Testimonial.objects.all()
    sub_img = Subscription_image.objects.first()
    team = Team.objects.order_by("-id")
    partners = Partner.objects.order_by("-id")
    return render(request, 'shop/about.html', {'about': about, 'test':testimanials, 'sub':sub_img, 'team':team, 'partners':partners})

def products(request):
    product_objects = Products.objects.order_by('-id')
    categories = get_product_categories()
    details = Product_page.objects.first()

    #search code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)
    else:
        product_objects = Products.objects.order_by('-id')

    #paginator
    paginator = Paginator(product_objects, 8)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)
    nums = "a" * product_objects.paginator.num_pages
    return render(request, 'shop/products.html', {
        'product_objects': product_objects, 'nums':nums, 'categories': categories, 'details':details
    })
   

def not_found(request, exception):
    return render(request, 'shop/404.html') 

def check(request):
    return render(request, 'shop/check.html')

def subscribe(request):
    if request.POST.get("action") == "post":
        s_email = request.POST.get("email")
        html_content = render_to_string('shop/email_template_subscribe.html')
        text = strip_tags(html_content)
        email = EmailMultiAlternatives(
            'Subscription',
            text,
            settings.EMAIL_HOST_USER,
            [s_email]
        )
        email.attach_alternative(html_content, 'text/html')
        email.send()
        subscriber = Subscriber.objects.create(
            email = s_email
        )
        messages.success(request, 'you have successfully subscribed with us!!')
        return JsonResponse({'message':'success'})

def message(request):
    if request.POST.get("action") == "post":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        me = Message.objects.create(
            name=name,
            email=email,
            message=message
        )
        messages.success(request, 'message sent successifully!!')
        return JsonResponse({'message':'success'})