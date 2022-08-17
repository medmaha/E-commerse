
    
request =  {'maha': 'touray'}

product = [
    {'id': 1,'name':'iphone', 'price': 17.08,},
    {'id': 2,'name':'samsung', 'price': 28.08,}
]

database = []


class Basket():
    def __init__(self, request):
        self.session = request
        self.mine = 'll'

        basket = {}
        if 'session_key' not in self.session:
            basket = self.session['session_key'] = {}

        self.basket = basket   

    def add(self, product, qty):
        product_id = product['id']

        if product_id not in self.basket:
            self.basket[product_id] = {'price': product['price'], 'qty': qty}


    def __iter__(self):
        product_ids = self.basket.keys()
    
        print(product_ids)

        basket = self.basket.copy()

        for product in product_ids:
            basket[product]['product'] = product
            
        for item in basket.values():
            item['total_price'] = item['price'] * (item['qty'])
            yield item    

    def __len__(self):
        """
        Get the basket data and count the qty of items
        """
        return sum(item['qty'] for item in self.basket.values())

    def save(self):
        database.append(self.basket)


product_1 = Basket(request)
product_1.add(product[0], 2)

# product_2 = Basket(request)
# product_2.add(product[1], 4)

for item in product_1:
    product = item
    
a = {'id': 1,'name':'iphone', 'price': 17.08,}
print(a)
del a['id']
print(a)