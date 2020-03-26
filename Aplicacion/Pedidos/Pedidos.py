import gi
import os

from Aplicacion import Main
from Aplicacion.BaseDatos import SQLiteMetodos
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
import webbrowser as wb

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class GridWindow(Gtk.Window):


    def __init__(self):
        """
        Inicializa la ventana de Pedidos.

        """
        # Interfaz Principal
        Gtk.Window.__init__(self, title="Pedidos")
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.set_border_width(10)
        self.set_default_size(300, 300)
        self.set_resizable(False)
        self.connect("destroy", Gtk.main_quit)


        self.Caja = Gtk.Box(spacing=20)
        self.Caja.set_orientation(Gtk.Orientation.VERTICAL)
        self.add(self.Caja)

        #TABLA CLIENTES
        self.columClientes = ["Dni", "Nombre", "Apellidos", "Sexo", "Direccion", "Telefono"]
        self.modelClientes = Gtk.ListStore(str, str, str, str, str, str)
        self.clientes = []
        self.vista = Gtk.TreeView(model=self.modelClientes)
        self.vista.get_selection().connect("changed", self.on_changed)
        self.labelClientes = Gtk.Label("Clientes")

        #TABLA PRODUCTOS
        self.columProductos = ["Id", "Dni", "Nombre", "Precio", "Cantidad"]
        self.modelProductos = Gtk.ListStore(int, str, str, str, int)
        self.productos = []
        self.vistaProductos = Gtk.TreeView(model=self.modelProductos)
        self.vistaProductos.get_selection().connect("changed", self.on_changed2)
        self.auxiliar = True
        self.labelProductos = Gtk.Label("Productos")
        self.Caja.add(self.labelClientes)
        self.Caja.add(self.vista)
        self.Caja.add(self.labelProductos)
        self.Caja.add(self.vistaProductos)
        self.boxAux = Gtk.Box(spacing=2)
        self.boxAux.set_orientation(Gtk.Orientation.HORIZONTAL)
        self.Caja.add(self.boxAux)
        self.Volver = Gtk.Button(label="Volver")
        self.Volver.connect("clicked", self.on_Volver_clicked)
        self.boxAux.pack_start(self.Volver, True, True, 0)
        self.Factura = Gtk.Button(label="Factura")
        self.Factura.connect("clicked", self.on_Factura_clicked)
        self.boxAux.pack_start(self.Factura, True, True, 0)
        self.Lista = Gtk.Button(label="Listar los Clientes")
        self.Lista.connect("clicked", self.on_Lista_clicked)
        self.boxAux.pack_start(self.Lista, True, True, 0)


        clientes = SQLiteMetodos.selectClientes()
        for cliente in clientes:
            self.clientes.append(
                [cliente[0], cliente[1], cliente[2], cliente[3], cliente[4], cliente[5]])
        for elemento in self.clientes:
            self.modelClientes.append(elemento)
        for i in range(len(self.columClientes)):
            celda = Gtk.CellRendererText()
            self.columna = Gtk.TreeViewColumn(self.columClientes[i], celda, text=i)
            self.vista.append_column(self.columna)
        self.show_all()


    def on_changed(self, selection):
        """Método que captura la señal del TreeView y carga los productos del cliente.

            :param selection: la seleccion en el TreeView.
            :return: Ninguno.

        """
        (self.model, self.iter) = selection.get_selected()
        self.productos.clear()
        productos = SQLiteMetodos.selectProductos(self.model[self.iter][0])
        for producto in productos:
            self.productos.append(
                [producto[0], producto[1], producto[2], str(producto[3]) + " €/ud", producto[4]])
        self.modelProductos.clear()
        for elemento in self.productos:
            self.modelProductos.append(elemento)
        if (self.auxiliar):
            for i in range(len(self.columProductos)):
                celda = Gtk.CellRendererText()
                self.columnaP = Gtk.TreeViewColumn(self.columProductos[i], celda, text=i)
                self.vistaProductos.append_column(self.columnaP)
                self.auxiliar = False

    def on_changed2(self, selection):
        """Método comodin.

            :param selection: la seleccion en el TreeView.
            :return: Ninguno.

        """
    def on_Volver_clicked(self, widget):
        """Metodo que vuelve al menu.

                :param widget: Widget Botón.
                :return: No devuelve ningún parámetro.
        """
        Main.GridWindow().show_all()
        self.set_visible(False)

    #CREAR LISTA DE CLIENTES
    def on_Lista_clicked(self, widget):
        """Metodo que crea un pdf de la lista de clientes.

            :param widget: Widget butón.
            :return: No devuelve ningún parámetro.
        """
        data = []
        data.append(["Dni", "Nombre", "Apellidos", "Sexo", "Direccion", "Telefono"])
        clientes = SQLiteMetodos.selectClientes()
        for cliente in clientes:
            data.append([cliente[0], cliente[1], cliente[2], cliente[3], cliente[4], cliente[5]])

        # Creacion pdf
        fileName = 'listaClientes.pdf'
        current_work_directory = os.getcwd()
        print("Current work directory: {}".format(current_work_directory))
        abs_work_directory = os.path.abspath(current_work_directory)
        print(os.pathsep)
        print()
        pdf = SimpleDocTemplate(current_work_directory + "/" + fileName, pagesize=letter)

        table = Table(data)
        elementos = []
        elementos.append(table)

        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkred),
            ('BACKGROUND', (0, 1), (-1, -1), colors.lightblue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Courier-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ])
        table.setStyle(style)
        # Colores
        rowNumb = len(data)
        for i in range(1, rowNumb):
            bc = colors.lightpink
            ts = TableStyle([('BACKGROUND', (0, i), (-1, i), bc)])
            table.setStyle(ts)

        #Bordes
        ts2 = TableStyle(
            [
                ('BOX', (0, 0), (-1, -1), 2, colors.black),
                ('LINEBEFORE', (0, 0), (-1, rowNumb), 2, colors.black),
                ('LINEABOVE', (0, 0), (-1, rowNumb), 2, colors.black)
            ]
        )
        table.setStyle(ts2)
        pdf.build(elementos)
        wb.open_new(current_work_directory + "/" + fileName)

    #CREAR FACTURA
    def on_Factura_clicked(self, widget):
        """Metodo que crea una factura.

           :param widget: Widget botón.
           :return: Ninguno.
        """

        current_work_directory = os.getcwd()  # Return a string representing the current working directory.
        dataC = []
        clientes = SQLiteMetodos.selectClientesPorDni(self.model[self.iter][0])
        for cliente in clientes:
            dataC.append(['Datos Cliente ', '', '', '', ''])
            dataC.append(['Dni: ', cliente[0], '', '', ''])
            dataC.append(['Nombre: ', cliente[1], '', '', ''])
            dataC.append(['Apellidos: ', cliente[2], '', '', ''])
            dataC.append(['Sexo: ', cliente[3], '', '', ''])
            dataC.append(['Direccion: ', cliente[4], '', '', ''])
            dataC.append(['Teléfono: ', cliente[5], '', '', ''])
            dataC.append(['', '', '', '', ''])

            precioFinal = 0.0
            dataP = []
            productos = SQLiteMetodos.selectProductos(self.model[self.iter][0])

        try:
            dataP.append(["Id Producto", "Nombre", "Precio", "Cantidad"])
            for producto in productos:
                dataP.append([producto[0], producto[2], str(producto[3]) + " €/ud", producto[4]])
                precioFinal = precioFinal + (producto[3] * producto[4
                ])

            dataP.append(['', '', 'TOTAL:', str(precioFinal) + " €"])
            rowNumb = len(dataP)

            # GENERAR PDF
            fileName = 'Factura' + dataC[1][1] + '.pdf'
            pdf = SimpleDocTemplate(current_work_directory + "/" + fileName, pagesize=letter)


            table = Table(dataC, colWidths=80, rowHeights=30)
            table.setStyle(TableStyle([
                ('TEXTCOLOR', (0, 0), (0, -1), colors.darkred),
                ('ALIGN', (0, 0), (0, -1), 'LEFT'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ]))

            table2 = Table(dataP, colWidths=80, rowHeights=30)
            table2.getSpaceBefore()
            table2.setStyle(TableStyle([
                ('TEXTCOLOR', (0, 0), (3, 0), colors.darkred),
                ('TEXTCOLOR', (0, rowNumb - 1), (3, rowNumb - 1), colors.darkred),
                ('ALIGN', (0, 0), (0, -1), 'LEFT'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('BOX', (0, 0), (-1, rowNumb - 2), 1, colors.black),
                ('INNERGRID', (0, 0), (-1, rowNumb - 2), 0.5, colors.grey)
            ]))

            elementos = []
            elementos.append(table)
            elementos.append(table2)
            pdf.build(elementos)
            wb.open_new(current_work_directory + "/" + fileName)

        except IndexError as e:
            print('No se puede generar la factura.')
