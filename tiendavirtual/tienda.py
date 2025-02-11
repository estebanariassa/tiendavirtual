from itertools import product


class Product:

    def __init__(self,name, price: float):

        self.name: str = name
        self.price: float = price


    def show_info(self)->str:
        return f"El nombre del producto es: {self.name} y el precio es {self.price}"




class Client:

    def __init__(self, name, cart):

        self.name:str = name
        self.cart: list[Product] = []

    def add_product(self, product: Product):
        self.cart.append(product)

    def show_cart(self):
        products_str: str = ""
        for product in self.cart:
            products_str: str = ""
            products_str += product.show_info() + "\n"

    def calculate_total(self):
        total: float=0
        for product in  self.cart:
            total +=    product.price



class Shop:

    def __init__(self, name, products):

        self.name: str = name
        self.products: list[Product] = products

    def add_product(self, product: Product):
        self.products.append(product)
    def show_products(self):
        products_str: str = ""
        for product in self.products:
            products_str += product.show_info() +"\n"
        return products_str