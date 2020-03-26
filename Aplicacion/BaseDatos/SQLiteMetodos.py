import sqlite3
from sqlite3 import Error


def crear_conexion():
    """Crea una conexion .

        :param: Ninguno.
        :return: Objeto Connection.
    """

    conn = None
    try:
        conn = sqlite3.connect("./base.db")
        return conn
    except Error as e:
        print(e)
    return conn


def cerrar_conexion(conn):
    """Función que cierra la base de datos.

        :param conn: Conexion de a la base.
        :return: Ninguno.
    """
    try:
        conn.close()
    except conn.DatabaseError as erroSQL:
        print("Error.")


def crearTabla(conn, crear_tabla_sql):
    """Crea una tabla.

        :param conn: Objecto Connection
        :param crear_tabla_sql: Create table statement
        :return: Ninguno.
    """
    try:
        c = conn.cursor()
        c.execute(crear_tabla_sql)
        conn.commit()
    except Error as e:
        print(e)

def selectClientes():
    """Select de los clientes.

        :param: Ninguno.
        :return: Lista de clientes.
    """
    conn = crear_conexion()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM clientes")
        datos = cursor.fetchall()
        return datos
    except conn.OperationalError as err:
        """"""
    except conn.DatabaseError as err2:
        """"""
    finally:
        cursor.close()
        cerrar_conexion(conn)

def selectClientesPorDni(dni):
    """Select de clientes por dni.

        :param dni: Dni.
        :return: Lista de datos.
    """
    conn = crear_conexion()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM clientes WHERE dni = '" + dni + "'")
        datos = cursor.fetchall()
        return datos
    except conn.OperationalError as err:
        """"""""
    except conn.DatabaseError as err2:
        """"""""
    finally:
        cursor.close()
        cerrar_conexion(conn)


def selectDniClientes():
    """Select de los dni.

        :param: Ninguno.
        :return: Lista de dni.
    """
    try:
        conn = crear_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT dni FROM clientes")
        datos = cursor.fetchall()
        return datos
    except conn.OperationalError as err:
        """"""
    except conn.DatabaseError as err2:
        """"""
    finally:
        cursor.close()
        cerrar_conexion(conn)


def selectProductos(dni):
    """Select de productos por dni.

        :param dni: Dni del cliente.
        :return: Lista con productos.
    """
    try:
        conn = crear_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE dni ='" + dni + "'")
        datos = cursor.fetchall()
        return datos
    except conn.OperationalError as err:
        """"""""
    except conn.DatabaseError as err2:
        """"""""
    finally:
        cursor.close()
        cerrar_conexion(conn)

def insertClientes(dni, nombre, apellidos, sexo, direccion, telefono):
    """Inserta una nueva fila en la tabla Clientes.

        :param dni: El Dni
        :param nombre: El nombre
        :param apellidos: Los Apellidos
        :param sexo: El Sexo del cliente
        :param direccion: La direccion
        :param telefono: El telefono
        :return: Ninguno.
    """

    if (dni != "" and nombre != "" and apellidos != "" and sexo != "" and direccion != "" and telefono != ""):
        conn = crear_conexion()
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO clientes (dni,nombre,apellidos,sexo,direccion,telefono) VALUES (?, ?, ?, ?, ?, ?)", (dni, nombre, apellidos, sexo, direccion, telefono))
            conn.commit()
        except conn.OperationalError as e:
            """"""
        except conn.DatabaseError as e2:
            print("Error, ya insertado ")
        finally:
            cursor.close()
            cerrar_conexion(conn)
    else:
        print("Faltan valores")


def insertProductos(id, dni, nombre, precio, cantidad):
    """Inserta una nueva fila en la tabla Productos.

        :param id: id int
        :param dni: Dni text
        :param nombre: nombre text
        :param precio: Precio float
        :param cantidad: Cantidad int
        :return: Ningún parámetro devuelto.
    """

    if (id != "" and dni != "" and nombre != "" and precio != "" and cantidad != ""):
        conn = crear_conexion()
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO productos(id, dni, nombre, precio, cantidad) VALUES (?, ?, ?, ?, ?)", (id, dni, nombre, precio, cantidad))
            conn.commit()
        except conn.OperationalError as e:
            """"""
        except conn.DatabaseError as e2:
            """"""
        finally:
            cursor.close()
            cerrar_conexion(conn)
    else:
        print("Faltan valores")


def deleteProductos(dni):
    """Elimina los productos por dni.

    :param dni: Dni .
    :return: Ninguno.
    """

    conn = crear_conexion()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM productos WHERE dni = '" + dni + "'")
        conn.commit()
        print("Eliminado")
    except conn.OperationalError as err:
        """"""
    except conn.DatabaseError as err2:
        """"""
    finally:
        cursor.close()
        cerrar_conexion(conn)


def updateClientes(dni, nombre, apellidos, sexo, direccion, telefono):
    """Modifica los datos de un cliente existente dado su dni.

        :param dni: Dni text
        :param nombre: Nombre text
        :param apellidos: Apellidos text
        :param sexo: Sexo text
        :param direccion: Direccion text
        :param telefono: Telefono text
        :return: Ningún parámetro es devuelto.
    """

    if (dni != "" and nombre != "" and apellidos != "" and sexo != "" and direccion != "" and telefono != ""):
        conn = crear_conexion()
        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE clientes SET nombre = ?, apellidos = ?, sexo = ?, direccion = ?, telefono = ? where dni = ?", (nombre, apellidos, sexo, direccion, telefono, dni))
            conn.commit()
        except conn.OperationalError as e:
            """"""
        except conn.DatabaseError as e2:
            """"""
        finally:
            cursor.close()
            cerrar_conexion(conn)
    else:
        print("Faltan valores")


def deleteClientes(dni):
    """Elimina un cliente dado su dni.

        :param dni: Dni del cliente a eliminar.
        :return: Ningún parámetro es devuelto.
    """
    deleteProductos(dni)
    conn = crear_conexion()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM clientes WHERE dni = '" + dni + "'")
        conn.commit()
        print("Eliminado")
    except conn.OperationalError as err:
        """"""
    except conn.DatabaseError as err2:
        """"""
    finally:
        cursor.close()
        cerrar_conexion(conn)




def main():
    sql_crear_clientes = """CREATE TABLE IF NOT EXISTS clientes(
                                     dni TEXT PRIMARY KEY, 
                                     nombre TEXT NOT NULL, 
                                     apellidos TEXT NOT NULL,
                                     sexo TEXT NOT NULL,
                                     direccion TEXT NOT NULL, 
                                     telefono TEXT NOT NULL
                                     )
    """
    sql_crear_productos = """CREATE TABLE IF NOT EXISTS productos(
                                     id integer PRIMARY KEY, 
                                     dni TEXT NOT NULL, 
                                     nombre TEXT NOT NULL, 
                                     precio float NOT NULL,
                                     cantidad integer NOT NULL
                                     )
    """


    conn = crear_conexion()

    if conn is not None:
        crearTabla(conn, sql_crear_clientes)
        crearTabla(conn, sql_crear_productos)


        """
        #insertar 1 vez si base vacia
        insertClientes('03227201W','Fernando','Torres Prieto','H','C/Venezuela nº40','634545121')
        insertClientes('41433825S','María','Perez Nuñez','M','C/Barcelona nº3','675784155')
        insertClientes('26396156E','Jaime','González Iglresias','H','C/Aragón nº18','659382415')
        insertProductos('1', '03227201W', 'Clavos', 0.10, 300)
        insertProductos('2', '03227201W', 'tornillos', 0.20, 200)
        insertProductos('3', '03227201W', 'martillos', 10.50, 2)
        """


    else:
        print("Fallo en la conexión.")
    cerrar_conexion(conn)
