from django.apps import apps
from django.contrib import admin

from .models import *

# Register your models here.
admin.site.site_header = "REAL FAMILY SAUCE"
admin.site.site_title = "PRODUCT"


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','price','category','description')
    search_fields = ('title','category')
    list_editable = ('price','category',)


admin.site.register(Products,ProductAdmin)
admin.site.register(Order_request)
admin.site.register(Blog)
admin.site.register(About)
admin.site.register(Footer)
admin.site.register(Team)
admin.site.register(Home)
admin.site.register(Testimonial)
admin.site.register(Subscriber)
admin.site.register(Contact)
admin.site.register(Message)
admin.site.register(Product_page)
admin.site.register(Blogs_page)
admin.site.register(Subscription_image)