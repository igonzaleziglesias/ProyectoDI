import gi

from Aplicacion import Main
from Aplicacion.BaseDatos import SQLiteMetodos

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class GridWindow(Gtk.Window):


    def __init__(self):
        """Inicializa la Gestion de Productos.
        """

        Gtk.Window.__init__(self, title=" Gestión Productos")
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.set_border_width(2)
        self.set_default_size(150, 200)
        self.set_resizable(False)
        self.connect("destroy", Gtk.main_quit)

        self.gridProductos = Gtk.Grid()
        self.gridProductos.set_column_homogeneous(True)
        self.gridProductos.set_row_homogeneous(True)



        self.Añadir = Gtk.Button("Añadir")
        self.Añadir.connect("clicked", self.on_Añadir_clicked)
        self.Volver = Gtk.Button("Volver")
        self.Volver.connect("clicked", self.on_Volver_clicked)
        self.caja = Gtk.Box(spacing=2)
        self.caja.set_orientation(Gtk.Orientation.HORIZONTAL)
        self.caja.set_margin_left(2)
        self.caja.set_margin_right(2)
        self.set_border_width(2)
        self.add(self.gridProductos)


        self.labelDni = Gtk.Label("Dni Cliente:", halign=Gtk.Align.START)
        self.entryDni = Gtk.ListStore(str)
        self.cargar_dni_cliente()
        self.comboAñadir = Gtk.ComboBox.new_with_model(self.entryDni)
        self.comboAñadir.connect("changed", self.on_comboAñadir_changed)
        self.renderer_text = Gtk.CellRendererText()
        self.comboAñadir.pack_start(self.renderer_text, True)
        self.comboAñadir.add_attribute(self.renderer_text, "text", 0)
        self.labelId = Gtk.Label("Id:", halign=Gtk.Align.START)
        self.entryId = Gtk.Entry()
        self.labelNombre = Gtk.Label("Nombre:", halign=Gtk.Align.START)
        self.entryNombre = Gtk.Entry()
        self.labelCantidad = Gtk.Label("Cantidad:", halign=Gtk.Align.START)
        self.entryCantidad = Gtk.Entry()
        self.labelPrecio = Gtk.Label("Precio(Euros):", halign=Gtk.Align.START)
        self.entryPrecio = Gtk.Entry()
        self.cargarInterface()

    def cargarInterface(self):
        # AÑADIR A GRID
        self.gridProductos.add(self.labelDni)
        self.gridProductos.attach_next_to(self.comboAñadir, self.labelDni, Gtk.PositionType.RIGHT, 1, 1)
        self.gridProductos.attach_next_to(self.labelId, self.labelDni, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridProductos.attach_next_to(self.entryId, self.labelId, Gtk.PositionType.RIGHT, 1, 1)
        self.gridProductos.attach_next_to(self.labelNombre, self.labelId, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridProductos.attach_next_to(self.entryNombre, self.labelNombre, Gtk.PositionType.RIGHT, 1, 1)
        self.gridProductos.attach_next_to(self.labelCantidad, self.labelNombre, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridProductos.attach_next_to(self.entryCantidad, self.labelCantidad, Gtk.PositionType.RIGHT, 1, 1)
        self.gridProductos.attach_next_to(self.labelPrecio, self.labelCantidad, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridProductos.attach_next_to(self.entryPrecio, self.labelPrecio, Gtk.PositionType.RIGHT, 1, 1)
        self.gridProductos.attach_next_to(self.Añadir, self.labelPrecio, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridProductos.attach_next_to(self.Volver, self.Añadir, Gtk.PositionType.RIGHT, 1, 1)

    def cargar_dni_cliente(self):
        """Metodo que carga los dni de los clientes existentes en los comboBox de modificar y eliminar.

        :param: No recibe ningún parámetro.
        :return: No devuelve ningún parámetro.
        """
        self.entryDni.clear()
        datos = SQLiteMetodos.selectDniClientes()

        for clientes in datos:
            self.entryDni.append([clientes[0]])

    def on_comboAñadir_changed(self, combo):
        """Metodo que recoge la señal "chaged" del comboBox y selecciona el actual valor en el indice.

            :param combo: GtkComboBox
            :return: No devuelve ningún parámetro.
        """

        tree_iter = combo.get_active_iter()
        if tree_iter != None:
            model = combo.get_model()
            dni = model[tree_iter][0]
            self.aux = dni

    def on_Añadir_clicked(self, button):
        """Metodo que recoge la señal "clicked" del boton y añada un nuevo producto asignado a un cliente.

            :param button: GtkButton.
            :return: No devuelve ningún parámetro.
        """

        try:
            id = int(self.entryId.get_text())
            dni = self.aux
            nombre = self.entryNombre.get_text()
            precio = float(self.entryPrecio.get_text())
            cantidad = int(self.entryCantidad.get_text())
            SQLiteMetodos.insertProductos(id, dni, nombre, precio, cantidad)
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Producto añadido correctamente")
            dialog.run()
            dialog.destroy()
        except ValueError as verr:
            print("Introduzca valores correctos")
        except Exception as ex:
            print("Error")

    def on_Volver_clicked(self, widget):
        """Vuelve al menu.

            :param widget: Widget
            :return: Ninguno.
        """
        Main.GridWindow().show_all()
        self.set_visible(False)
