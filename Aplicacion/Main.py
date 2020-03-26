import gi
from Aplicacion.GestionProductos import GestionProductos
from Aplicacion.Pedidos import Pedidos
from Aplicacion.GestionClientes import GestionClientes
from Aplicacion.BaseDatos import SQLiteMetodos

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class GridWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Proyecto D.I.")
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.set_border_width(2)
        self.set_default_size(300, 200)
        self.set_resizable(False)
        self.caja = Gtk.Box(spacing=2)
        self.caja.set_orientation(Gtk.Orientation.VERTICAL)
        self.add(self.caja)

        self.boton1 = Gtk.Button(label="Gestión de clientes")
        self.boton1.connect("clicked", self.on_button1_clicked)
        self.caja.pack_start(self.boton1, True, True, 0)

        self.boton2 = Gtk.Button(label=" Gestión Productos")
        self.boton2.connect("clicked", self.on_button2_clicked)
        self.caja.pack_start(self.boton2, True, True, 0)

        self.boton3 = Gtk.Button(label="Pedidos")
        self.boton3.connect("clicked", self.on_button3_clicked)
        self.caja.pack_start(self.boton3, True, True, 0)

        self.boton4 = Gtk.Button(label="Salir")
        self.boton4.connect("clicked", self.on_button4_clicked)
        self.caja.pack_start(self.boton4, True, True, 0)

        self.connect("destroy", Gtk.main_quit)

        # Creacion base de datos.
        SQLiteMetodos.main()
        self.show_all()

    #Gestion_De_Clientes
    def on_button1_clicked(self, widget):
        """
            Metodo de  Gestion_De_Clientes
            :param Widget: widget
            :return: Nothing
            """
        GestionClientes.GridWindow().show_all()
        self.set_visible(False)

    #Gestion de Productos
    def on_button2_clicked(self, widget):
        """
            Metodo de Gestion de Productos
            :param Widget: widget
            :return: Nothing
            """
        GestionProductos.GridWindow().show_all()
        self.set_visible(False)

    #Pedidos
    def on_button3_clicked(self, widget):
        """
            Metodo de Pedidos
            :param Widget: widget
            :return: Nothing
            """
        Pedidos.GridWindow().show_all()
        self.set_visible(False)

    # Salir
    def on_button4_clicked(self, widget):
        """
            Metodo para salir de la app
            :param Widget: widget
            :return: Nothing
            """
        exit(0)


if __name__ == "__main__":
    GridWindow()
    Gtk.main()
