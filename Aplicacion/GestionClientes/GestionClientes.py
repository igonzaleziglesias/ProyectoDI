import gi
from Aplicacion import Main
from Aplicacion.BaseDatos import SQLiteMetodos

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class GridWindow(Gtk.Window):

    def __init__(self):
        """
        Inicializa Gestion de Clientes
        """


        # Interfaz Principal
        Gtk.Window.__init__(self, title="Gestion de Clientes")
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.set_border_width(2)
        self.set_default_size(400, 200)
        self.set_resizable(False)
        self.connect("destroy", Gtk.main_quit)

        self.notebook = Gtk.Notebook()
        self.add(self.notebook)


        """AÑADIR"""
        self.Volver = Gtk.Button("Volver")
        self.Volver.connect("clicked", self.on_Volver_clicked)
        self.gridAñadir = Gtk.Grid()
        self.gridAñadir.set_column_homogeneous(True)
        self.gridAñadir.set_row_homogeneous(True)


        self.labelDni = Gtk.Label("Dni:", halign=Gtk.Align.START)
        self.entryDni = Gtk.Entry()
        self.labelNombre = Gtk.Label("Nombre:", halign=Gtk.Align.START)
        self.entryNombre = Gtk.Entry()
        self.labelApellidos = Gtk.Label("Apellidos:", halign=Gtk.Align.START)
        self.entryApellidos = Gtk.Entry()
        self.labelSexo = Gtk.Label("Sexo:", halign=Gtk.Align.START)
        self.boxSexo = Gtk.Box(spacing=2)
        self.boxSexo.set_orientation(Gtk.Orientation.HORIZONTAL)
        self.Hombre = Gtk.RadioButton.new_with_label_from_widget(None, "Hombre")
        self.Hombre.connect("toggled", self.on_button_toggled, "1")
        self.Mujer = Gtk.RadioButton.new_from_widget(self.Hombre)
        self.Mujer.set_label("Mujer")
        self.Mujer.connect("toggled", self.on_button_toggled, "2")
        self.boxSexo.add(self.Hombre)
        self.boxSexo.add(self.Mujer)
        self.labelDireccion = Gtk.Label("Direccion:", halign=Gtk.Align.START)
        self.entryDireccion = Gtk.Entry()
        self.labelTelefono = Gtk.Label("Telefono:", halign=Gtk.Align.START)
        self.entryTelefono = Gtk.Entry()
        self.Añadir = Gtk.Button("Añadir")
        self.Añadir.connect("clicked", self.on_Añadir_clicked)

        # AÑADIR AL GRID
        self.gridAñadir.add(self.labelDni)
        self.gridAñadir.attach_next_to(self.entryDni, self.labelDni, Gtk.PositionType.RIGHT, 1, 1)
        self.gridAñadir.attach_next_to(self.labelNombre, self.labelDni, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridAñadir.attach_next_to(self.entryNombre, self.labelNombre, Gtk.PositionType.RIGHT, 1, 1)
        self.gridAñadir.attach_next_to(self.labelApellidos, self.labelNombre, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridAñadir.attach_next_to(self.entryApellidos, self.labelApellidos, Gtk.PositionType.RIGHT, 1, 1)
        self.gridAñadir.attach_next_to(self.labelDireccion, self.labelApellidos, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridAñadir.attach_next_to(self.entryDireccion, self.labelDireccion, Gtk.PositionType.RIGHT, 1, 1)
        self.gridAñadir.attach_next_to(self.labelTelefono, self.labelDireccion, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridAñadir.attach_next_to(self.entryTelefono, self.labelTelefono, Gtk.PositionType.RIGHT, 1, 1)
        self.gridAñadir.attach_next_to(self.labelSexo, self.labelTelefono, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridAñadir.attach_next_to(self.boxSexo, self.labelSexo, Gtk.PositionType.RIGHT, 1, 1)
        self.gridAñadir.attach_next_to(self.Añadir, self.labelSexo, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridAñadir.attach_next_to(self.Volver, self.Añadir, Gtk.PositionType.RIGHT, 1, 1)




        """MODIFICAR"""
        self.Volver2 = Gtk.Button("Volver")
        self.Volver2.connect("clicked", self.on_Volver_clicked)
        self.gridModificar = Gtk.Grid()
        self.gridModificar.set_column_homogeneous(True)
        self.gridModificar.set_row_homogeneous(True)

        self.labelDni2 = Gtk.Label("Dni:", halign=Gtk.Align.START)
        self.entryDni2 = Gtk.ListStore(str)
        self.combo_Modificar_Dni = Gtk.ComboBox.new_with_model(self.entryDni2)
        self.comboAux = self.combo_Modificar_Dni.connect("changed", self.on_comboModificar_changed)
        self.renderer_text = Gtk.CellRendererText()
        self.labelNombre2 = Gtk.Label("Nombre:", halign=Gtk.Align.START)
        self.entryNombre2 = Gtk.Entry()
        self.combo_Modificar_Dni.pack_start(self.renderer_text, True)
        self.combo_Modificar_Dni.add_attribute(self.renderer_text, "text", 0)
        self.labelApellidos2 = Gtk.Label("Apellidos:", halign=Gtk.Align.START)
        self.entryApellidos2 = Gtk.Entry()
        self.labelDireccion2 = Gtk.Label("Direccion:", halign=Gtk.Align.START)
        self.entryDireccion2 = Gtk.Entry()
        self.labelTelefono2 = Gtk.Label("Telefono:", halign=Gtk.Align.START)
        self.entryTelefono2 = Gtk.Entry()
        self.labelSexo2 = Gtk.Label("Sexo:", halign=Gtk.Align.START)
        self.boxSexo2 = Gtk.Box(spacing=2)
        self.boxSexo2.set_orientation(Gtk.Orientation.HORIZONTAL)
        self.Hombre2 = Gtk.RadioButton.new_with_label_from_widget(None, "Hombre")
        self.Hombre2.connect("toggled", self.on_button_toggled2, "1")
        self.Mujer2 = Gtk.RadioButton.new_from_widget(self.Hombre2)
        self.Mujer2.set_label("Mujer")
        self.Mujer2.connect("toggled", self.on_button_toggled2, "2")
        self.boxSexo2.add(self.Hombre2)
        self.boxSexo2.add(self.Mujer2)
        self.Modificar = Gtk.Button("Modificar")
        self.Modificar.connect("clicked", self.on_Modificar_clicked)


        # AÑADIR AL GRID
        self.gridModificar.add(self.labelDni2)
        self.gridModificar.attach_next_to(self.combo_Modificar_Dni, self.labelDni2, Gtk.PositionType.RIGHT, 1, 1)
        self.gridModificar.attach_next_to(self.labelNombre2, self.labelDni2, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridModificar.attach_next_to(self.entryNombre2, self.labelNombre2, Gtk.PositionType.RIGHT, 1, 1)
        self.gridModificar.attach_next_to(self.labelApellidos2, self.labelNombre2, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridModificar.attach_next_to(self.entryApellidos2, self.labelApellidos2, Gtk.PositionType.RIGHT, 1, 1)
        self.gridModificar.attach_next_to(self.labelDireccion2, self.labelApellidos2, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridModificar.attach_next_to(self.entryDireccion2, self.labelDireccion2, Gtk.PositionType.RIGHT, 1, 1)
        self.gridModificar.attach_next_to(self.labelTelefono2, self.labelDireccion2, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridModificar.attach_next_to(self.entryTelefono2, self.labelTelefono2, Gtk.PositionType.RIGHT, 1, 1)
        self.gridModificar.attach_next_to(self.labelSexo2, self.labelTelefono2, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridModificar.attach_next_to(self.boxSexo2, self.labelSexo2, Gtk.PositionType.RIGHT, 1, 1)
        self.gridModificar.attach_next_to(self.Modificar, self.labelSexo2, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridModificar.attach_next_to(self.Volver2, self.Modificar, Gtk.PositionType.RIGHT, 1, 1)


        """ELIMINAR"""
        self.buttonVolver3 = Gtk.Button("Volver")
        self.buttonVolver3.connect("clicked", self.on_Volver_clicked)
        self.gridEliminar = Gtk.Grid()
        self.gridEliminar.set_column_homogeneous(True)
        self.gridEliminar.set_row_homogeneous(False)


        self.labelDni3 = Gtk.Label("Dni:", halign=Gtk.Align.START)
        self.entryDni3 = Gtk.ListStore(str)
        self.combo_Eliminar = Gtk.ComboBox.new_with_model(self.entryDni3)

        self.comboAuxiliar = self.combo_Eliminar.connect("changed", self.on_comboEliminar_changed)
        self.renderer_text = Gtk.CellRendererText()
        self.combo_Eliminar.pack_start(self.renderer_text, True)
        self.combo_Eliminar.add_attribute(self.renderer_text, "text", 0)

        self.Eliminar = Gtk.Button("Eliminar")
        self.Eliminar.connect("clicked", self.on_Eliminar_clicked)

        # AÑADIR AL GRID
        self.gridEliminar.add(self.labelDni3)
        self.gridEliminar.attach_next_to(self.combo_Eliminar, self.labelDni3, Gtk.PositionType.RIGHT, 1, 1)
        self.gridEliminar.attach_next_to(self.Eliminar, self.labelDni3, Gtk.PositionType.BOTTOM, 1, 1)
        self.gridEliminar.attach_next_to(self.buttonVolver3, self.Eliminar, Gtk.PositionType.RIGHT, 1, 1)




        """AÑADIMOS AL NOTEBOOK"""
        self.cargar_dni_cliente()
        self.notebook.append_page(self.gridAñadir, Gtk.Label('Añadir'))
        self.notebook.append_page(self.gridModificar, Gtk.Label('Modificar'))
        self.notebook.append_page(self.gridEliminar, Gtk.Label('Eliminar'))

        # Validacion DNI
        self.TABLA_NIF = 'TRWAGMYFPDXBNJZSQVHLCKE'

        self.CLAVES_CIF = 'PQS' + 'ABEH' + 'CDFGJRUVNW'
        self.CLAVES_NIF1 = 'LKM'  # Son especiales, se validan
        # como CIFs
        self.CLAVES_NIF2 = 'XYZ'
        self.CLAVES_NIF = self.CLAVES_NIF1 + self.CLAVES_NIF2

    # Señal del RadioButton Insertar
    def on_button_toggled(self, button, name):
        """Metodo que recoge la seña del RadioButton.

                :param button: Button
                :param name: Name
                :return: No devuelve ningún parámetro.
        """
        if button.get_active():
            state = "on"
        else:
            state = "off"

    # Señal del RadioButton Modificar
    def on_button_toggled2(self, button, name):
        """Merodo que recoge la seña del RadioButton.

                :param button: Button
                :param name: Name
                :return: No devuelve ningún parámetro.
        """
        if button.get_active():
            state = "on"
        else:
            state = "off"

    def on_Añadir_clicked(self, widget):
        """Añade un nuevo cliente dados sus datos.

            :param widget: Widget
            :return: No devuelve ningún parámetro.
        """
        dni = self.entryDni.get_text()
        validacion = self.validarDni(dni)

        if (self.Hombre.get_active()):
            sexo = "H"
        else:
            sexo = "M"

        direccion = self.entryDireccion.get_text()
        telefono = self.entryTelefono.get_text()
        nombre = self.entryNombre.get_text()
        apellidos = self.entryApellidos.get_text()
        vaidacionTelf = self.validarTlf(telefono)

        if (validacion and vaidacionTelf):
            SQLiteMetodos.insertClientes(dni, nombre, apellidos, sexo, direccion, telefono)
            self.cargar_dni_cliente()
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Cliente Añadido Correctamente")
            dialog.run()
            dialog.destroy()

        elif (validacion == False):
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK, "Introduce un dni válido")
            dialog.run()
            dialog.destroy()

        else:
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK, "Introduce un teléfono válido")
            dialog.run()
            dialog.destroy()


    def validarDni(self, valor):
        """ Indica si un Dni es valid.

            :param dni: Str Dni de la persona.
            :return boolean: true o false en función del resultado
        """
        resultado = False
        if len(valor) == 9:
            try:
                if valor[0] in self.CLAVES_NIF1:
                    resultado = self.validarCIF(valor)
                else:
                    num = None
                    if valor[0] in self.CLAVES_NIF2:
                        pos = self.CLAVES_NIF2.find(valor[0])
                        sNum = str(pos) + valor[1:-1]
                        num = int(sNum)
                    elif valor[0].isdigit():
                        num = int(valor[:-1])
                    if num != None and self.TABLA_NIF[num % 23] == valor[-1]:
                        resultado = True
            except:
                print("Error en dni")
                pass
        return resultado

    def validarTlf(self, valor):
        """Indica si un tlf es valido.

            :param telf: Str Dni de la persona.
            :return boolean: True o False en función del resultado.
        """
        resultado = False
        if len(valor) == 9:
            try:
                if valor.isnumeric():
                    resultado = True
                else:
                    resultado = False
            except:
                print("Error en numero de telefono")
                pass
        return resultado

    def on_Modificar_clicked(self, widget):
        """Merodo para modificar los datos de un cliente.

             :param widget: Widget
             :return: No devuelve ningún parámetro.
        """
        dni = self.comboAux
        nombre = self.entryNombre2.get_text()
        apellidos = self.entryApellidos2.get_text()
        if (self.Hombre2.get_active()):
            sexo = "H"
        else:
            sexo = "M"

        direccion = self.entryDireccion2.get_text()
        telefono = self.entryTelefono2.get_text()
        vaidacionTelf = self.validarTlf(telefono)

        if (vaidacionTelf):
            SQLiteMetodos.updateClientes(dni, nombre, apellidos, sexo, direccion, telefono)
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Cliente Modificado Correctamente")
            dialog.run()
            dialog.destroy()

        else:
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK, "Introduce un nuevo teléfono válido")
            dialog.run()
            dialog.destroy()



    def cargar_dni_cliente(self):
        """Carga los Dni de la base de datos en los comboBox de modificar y eliminar.

            :param: No recibe ningún parámetro.
            :return: No devuelve ningún parámetro.
        """
        self.entryDni3.clear()
        self.entryDni2.clear()
        datos = SQLiteMetodos.selectDniClientes()

        for clientes in datos:
            self.entryDni2.append([clientes[0]])
            self.entryDni3.append([clientes[0]])

    def on_Volver_clicked(self, widget):
        """Vuelve al menu.

            :param widget: Widget
            :return: No devuelve ningún parámetro.
        """
        Main.GridWindow().show_all()
        self.set_visible(False)


    def on_Eliminar_clicked(self, widget):
        """Elemina un cliente.

            :param widget: Widget
            :return: No devuelve ningún parámetro.
        """
        SQLiteMetodos.deleteClientes(self.comboAuxiliar)
        self.cargar_dni_cliente()
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Cliente Eliminado Correctamente")
        dialog.run()
        dialog.destroy()

    def on_comboModificar_changed(self, combo):
        """Recoge la señal del combo cambiado para cargar los datos del cliente a modificar.

            :param combo: GtkCombo
            :return: No devuelve ningún parámetro.

        """
        tree_iter = combo.get_active_iter()
        if tree_iter != None:
            model = combo.get_model()
            dniCliente = model[tree_iter][0]
            self.comboAux = dniCliente

            datos = SQLiteMetodos.selectClientesPorDni(dniCliente)
            for clientes in datos:
                self.entryNombre2.set_text(clientes[1])
                self.entryApellidos2.set_text(clientes[2])
                self.entryDireccion2.set_text(clientes[4])
                self.entryTelefono2.set_text(clientes[5])

    def on_comboEliminar_changed(self, combo):
        """Recoge la señal del combo cambiado para cargar los datos del cliente a eliminar.

            :param combo: GtkCombo
            :return: none
        """
        tree_iter = combo.get_active_iter()
        if tree_iter != None:
            model = combo.get_model()
            dniCliente2 = model[tree_iter][0]
            self.comboAuxiliar = dniCliente2