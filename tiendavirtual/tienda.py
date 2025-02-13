from itertools import product
class Producto:
    def __init__(self, nombre, precio):
        self.nombre: str = nombre
        self.precio: int = precio

    def mostrar_info(self) -> str:
        return f"El nombre del producto es: {self.nombre} y el precio {self.precio}"

p1: Producto = Producto("Tuki", 99)
print(p1.mostrar_info())

class Cliente:
    def __init__(self, nombre, carrito):
        self.nombre: str = nombre
        self.carrito: list[Producto] = []

    def agregar_producto(self, producto: Producto):
        self.carrito.append(producto)

    def mostrar_carrito(self) -> str:
        productos_str: str = ""
        for producto in self.carrito:
            productos_str += producto.mostrar_info() + "\n"
        return productos_str

    def calcular_total(self):
        total: float = 0
        for producto in self.carrito:
            total += producto.precio
        return total

class Tienda:
    def __init__(self, nombre, productos):
        self.nombre: str = nombre
        self.productos: list[Producto] = []

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def mostrar_producto(self):
        productos_str: str = ""
        for producto in self.productos:
            productos_str += producto.mostrar_info() + "\n"
        return productos_str
