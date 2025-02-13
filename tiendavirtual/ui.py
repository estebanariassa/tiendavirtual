from click import prompt
from rich.console import  Console
from rich.prompt import Prompt

from tiendavirtual.tienda import Tienda


class TiendaUI:

    def __init__(self, tienda: Tienda):
        self.tienda: Tienda = tienda
        self.consola: Console = Console()


    def mostrar_menu(self):
        self.consola.print("\n[bold blue]Ella es una Tienda Virtual[/bold blue]\n")
        self.consola.print("1. Agregar producto a tienda")
        self.consola.print("2. Mostrar productos de la tienda")
        self.consola.print("3. Agregar producto a carrito")
        self.consola.print("4. Mostrar carrito de compras")
        self.consola.print("5. Calcular el total de la compra",)
        self.consola.print("6. salir")

        opcion = Prompt.ask("\n Seleccione una opcion", choices= ["1","2","3","4","5","6"])

        return opcion



    def ejecutar(self):
        while True:
            opcion = self.mostrar_menu()
            match opcion:
                case "1":
                    pass
                case "2":
                    pass
                case "3":
                    pass
                case "4":
                    pass
                case "5":
                    pass
                case "6":

                    break
