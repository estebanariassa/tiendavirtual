from tiendavirtual.tienda import Tienda
from tiendavirtual.ui import TiendaUI

def main():
    tienda: Tienda = Tienda("Ella es una Tienda Virtual")
    ui:TiendaUI = TiendaUI(tienda)
    ui.ejecutar()

if __name__ == "__main__":
    main()
