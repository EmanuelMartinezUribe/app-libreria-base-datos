from sqlLibreria import *
from prettytable import PrettyTable
from menus import *
from clientes import *
from libros import *
from ventas import *

conexion, cursor = conectar_bd("sistemaVentas.db")
sentencia = """SELECT * FROM Clientes"""
cursor.execute(sentencia)
clientesTuplas = cursor.fetchall()
clientes = []
for cliente in clientesTuplas:
    cliente = list(cliente)
    clientes.append(cliente)

sentencia = """SELECT * FROM Libros"""
cursor.execute(sentencia)
librosTuplas = cursor.fetchall()
libros = []
for libro in librosTuplas:
    libro = list(libro)
    libros.append(libro)

sentencia = """SELECT * FROM Ventas"""
cursor.execute(sentencia)
ventas = cursor.fetchall()

def opcionEstadisticas1(listaLibros, listaVentas):
    codigoLibro = ""
    while codigoLibro != "R":
        codigoLibro = input("(R para regresar) - Digite el codigo del libro: ").strip()
        if codigoLibro.isdigit() and codigoLibro != "R":
            codigoLibro = int(codigoLibro)
            terminado = False
            for libro in listaLibros:
                if codigoLibro == libro[0]:
                    cantidadVendido = 0
                    totalVendido = 0
                    for venta in listaVentas:
                        if venta[2] == libro[0]:
                            cantidadVendido += venta[3]
                            totalVendido += venta[4]
                    print(f"""----------------------
Nombre Libro: {libro[1]}
Codigo Libro: {codigoLibro}
Cantidad Vendida: {cantidadVendido}
Total Vendido: ${totalVendido}
----------------------""")
                    terminado = True

                else:
                    if libro == listaLibros[-1] and codigoLibro != "R" and terminado == False:
                        print("Ese 'Codigo Libro' no esta registrado")
        else:
            if codigoLibro != "R":
                print("Debe ingresar solo digitos")

def opcionEstadisticas2(listaLibros, listaVentas):
    if len(listaVentas) == 0:
        print("No hay ventas registradas")
    else:
        cantidadVendidaLibros = []
        for libro in listaLibros:
            cantidadVendida = 0
            for venta in listaVentas:
                if venta[2] == libro[0]:
                    cantidadVendida += venta[3]
                if venta == listaVentas[-1]:
                    cantidadVendidaLibros.append([cantidadVendida, libro[0]])
        for libro in listaLibros:
            if max(cantidadVendidaLibros)[1] == libro[0]:
                nombreMax = libro[1]
            elif min(cantidadVendidaLibros)[1] == libro[0]:
                nombreMin = libro[1]
        print()
        print("---------------------------------------------------")
        print(f"Libro mas vendido: {nombreMax}, cantidad vendida: {max(cantidadVendidaLibros)[0]}")
        print(f"Libro menos vendido: {nombreMin}, cantidad vendida: {min(cantidadVendidaLibros)[0]}")
        print("---------------------------------------------------")

def opcionEstadisticas3(listaVentas):
    if len(listaVentas) == 0:
        print("No hay ventas registradas")
    else:
        ventaTotal = 0
        for venta in listaVentas:
            ventaTotal += venta[4]
            if venta == listaVentas[-1]:
                print()
                print("-------------------------")
                print(f"Venta Total: ${ventaTotal}")
                print("-------------------------")

def opcionEstadisticas4(listaClientes, listaVentas):
    if len(listaVentas) == 0:
        print("No hay ventas registradas")
    else:
        comprasPorVentas = []
        for venta in listaVentas:
            comprasPorVentas.append([venta[4], venta[1]])
            print(venta, listaVentas)
            if venta == listaVentas[-1]:
                for cliente in listaClientes:
                    print(max(comprasPorVentas), cliente[1])
                    if max(comprasPorVentas)[1] == cliente[1]:
                        nombreCliente = cliente[0]
        print()
        print("-------------------------------------------------------")
        print(f"Cliente con mayor compra x venta: {nombreCliente} con ${max(comprasPorVentas)[0]}")
        print("-------------------------------------------------------")

def opcionEstadisticas5(listaClientes, listaVentas):
    if len(listaVentas) == 0:
        print("No hay ventas registradas")
    else:
        volumenDeVenta = []
        for cliente in listaClientes:
            totalComprado = 0
            for venta in listaVentas:
                if venta[1] == cliente[1]:
                    totalComprado += venta[4]
                if venta == listaVentas[-1]:
                    volumenDeVenta.append([totalComprado, cliente[0]])
        print()
        print("--------------------------------------------------------")
        print(f"Cliente con mayor volumen de venta: {max(volumenDeVenta)[1]}, con ${max(volumenDeVenta)[0]}")
        print("--------------------------------------------------------")



opcionPrincipal = ""
if opcionPrincipal == "R":
    desconectar_bd(conexion, cursor)
while opcionPrincipal != "R":
    opcionPrincipal = menuPrincipal()
    while opcionPrincipal != "R" and opcionPrincipal != "1" and opcionPrincipal != "2" and opcionPrincipal != "3" and opcionPrincipal != "4":
        opcionPrincipal = input("Digite una opcion disponible: ").strip()

    if opcionPrincipal == "1":
        opcionClientes = ""
        while opcionClientes != "R":
            opcionClientes = menuClientes()
            while opcionClientes != "R" and opcionClientes != "1" and opcionClientes != "2" and opcionClientes != "3" and opcionClientes != "4" and opcionClientes != "5":
                opcionClientes = input("Digite una opcion disponible: ").strip()
            if opcionClientes == "1":
                opcionClientes1(clientes)
            elif opcionClientes == "2":
                opcionClientes2(clientes)
            elif opcionClientes == "3":
                opcionClientes3(clientes, ventas)
            elif opcionClientes == "4":
                opcionClientes4(clientes, ventas)
            elif opcionClientes == "5":
                opcionClientes5(clientes)
    elif opcionPrincipal == "2":
        opcionLibros = ""
        while opcionLibros != "R":
            opcionLibros = menuLibros()
            while opcionLibros != "R" and opcionLibros != "1" and opcionLibros != "2" and opcionLibros != "3" and opcionLibros != "4" and opcionLibros != "5":
                opcionLibros = input("Digite una opcion disponible: ").strip()
            if opcionLibros == "1":
                opcionLibros1(libros)
            elif opcionLibros == "2":
                opcionLibros2(libros)
            elif opcionLibros == "3":
                opcionLibros3(libros, ventas)
            elif opcionLibros == "4":
                opcionLibros4(libros, ventas)
            elif opcionLibros == "5":
                opcionLibros5(libros)
    elif opcionPrincipal == "3":
        opcionLibros = ""
        while opcionLibros != "R":
            opcionLibros = menuVentas()
            while opcionLibros != "R" and opcionLibros != "1" and opcionLibros != "2" and opcionLibros != "3" and opcionLibros != "4" and opcionLibros != "5":
                opcionLibros = input("Digite una opcion disponible: ").strip()
            if opcionLibros == "1":
                opcionVentas1(clientes, libros, ventas)
            elif opcionLibros == "2":
                opcionVentas2(clientes, libros, ventas)
            elif opcionLibros == "3":
                opcionVentas3(clientes, libros, ventas)
            elif opcionLibros == "4":
                opcionVentas4(libros, ventas)
            elif opcionLibros == "5":
                opcionVentas5(ventas)
    elif opcionPrincipal == "4":
        opcionEstadisticas = ""
        while opcionEstadisticas != "R":
            opcionEstadisticas = menuEstadisticas()
            while opcionEstadisticas != "R" and opcionEstadisticas != "1" and opcionEstadisticas != "2" and opcionEstadisticas != "3" and opcionEstadisticas != "4" and opcionEstadisticas != "5":
                opcionEstadisticas = input("Digite una opcion disponible: ").strip()
            if opcionEstadisticas == "1":
                opcionEstadisticas1(libros, ventas)
            elif opcionEstadisticas == "2":
                opcionEstadisticas2(libros, ventas)
            elif opcionEstadisticas == "3":
                opcionEstadisticas3(ventas)
            elif opcionEstadisticas == "4":
                opcionEstadisticas4(clientes, ventas)
            elif opcionEstadisticas == "5":
                opcionEstadisticas5(clientes, ventas)