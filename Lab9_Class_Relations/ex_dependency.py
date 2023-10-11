class Customer:
    def __init__(self,id,name):
        self.id = id
        self.name = name

    def customer_info(self):
        print(f'Cus ID: {self.id} Cus name : {self.name}')

class Cart: # ตะกร้าสินค้า
    def __init__(self,Customer):
        self.cart_customer = Customer
        self.list_product = list()

    def cart_info(self):
        # display owner of cart
        print(f'Owner Cart ID: {self.cart_customer.id}'
              f'Owner name : {self.cart_customer.name}')
        # display product in cart
        print('List of products: ')
        for x in self.list_product:
            x.product_info()

        # display totle price
        total = 0
        for x in self.list_product:
            total += x.price
        print(f'Totle price: {total}')

    def add_product(self,Product):
        self.list_product.append(Product)


class Product:
    def __init__(self,id,product_name,price):
        self.id = id
        self.product_name = product_name
        self.price = price

    def product_info(self):
        print(f'Pro ID: {self.id} Pro name: {self.product_name}'
              f'Price: {self.price}')
# create object
# customer
c = Customer("C001","Bank")
c.customer_info()

#product
p1 = Product("P001","Coffee",50.0)
p2 = Product("P002","Ice Tea",35.5)
p3 = Product("P003","Ice Chocolate",40.0)

# cart
cart1 = Cart(c)
# add product to cart
cart1.add_product(p1)
cart1.add_product(p2)
cart1.add_product(p3)


cart1.cart_info()


