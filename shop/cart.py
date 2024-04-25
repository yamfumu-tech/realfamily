from decimal import Decimal
from shop.models import Products


class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('skey')
        if 'skey' not in request.session:
            cart = self.session['skey'] = {}
        self.cart = cart

    def add(self, product, qty):
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]['qty'] += 1
        else:
            self.cart[product_id] = {'price': str(product.price), 'qty': qty}

        self.save()

    def __iter__(self):
        product_id = self.cart.keys()
        products = Products.objects.filter(id__in=product_id)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product
        
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item

    def __len__(self):
        return len(self.cart)

    def add_cart(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]['qty'] += 1
        self.save()
    
    def delete_cart(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            if self.cart[product_id]['qty'] == 1:
                del self.cart[product_id] 
            elif self.cart[product_id]['qty'] > 1:
                self.cart[product_id]['qty'] -= 1
        self.save()

    def delete_item(self, product):
        product_id = str(product.id)
        del self.cart[product_id] 
        self.save()
    
    def get_qty(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            return self.cart[product_id]['qty']

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())
    
    def clear(self):
        del self.session['skey']
        self.save()
    
    def save(self):
        self.session.modified = True