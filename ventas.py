from sqlLibreria import *
from prettytable import PrettyTable
conexion, cursor = conectar_bd("sistemaVentas.db")

def opcionVentas1(listaClientes, listaLibros, listaVentas):
    ventaCodigoCliente = ""
    while ventaCodigoCliente != "R":
        clienteRegistrado = False
        libroRegistrado = False
        ventaCodigoCliente = input("(R para regresar) - Digite el codigo del cliente: ").strip()
        if ventaCodigoCliente.isdigit() and ventaCodigoCliente != "R":
            ventaCodigoCliente = int(ventaCodigoCliente)
            for cliente in listaClientes:
                if ventaCodigoCliente in cliente:
                    clienteRegistrado = True
                    break
                else:
                    if cliente == listaClientes[-1] and ventaCodigoCliente != "R":
                        print("El codigo no esta registrado")
        if clienteRegistrado and ventaCodigoCliente != "R":
            codigoNombreLibro = ""
            while codigoNombreLibro != "R":
                codigoNombreLibro = input("(R para regresar) - Digite el codigo libro: ").strip()
                if codigoNombreLibro.isdigit() and codigoNombreLibro != "R":
                    codigoNombreLibro = int(codigoNombreLibro)
                    for libro in listaLibros:
                        if codigoNombreLibro in libro:
                            libroRegistrado = True
                            break
                        else:
                            if libro == listaLibros[-1] and codigoNombreLibro != "R":
                                print("El codigo no esta registrado")
                if libroRegistrado and codigoNombreLibro != "R" and int(libro[3]) > 0:
                    cantidadVender = ""
                    while cantidadVender != "R":
                        cantidadVender = input("(R para regresar) - Digite la cantidad de libros a vender: ").strip()
                        if cantidadVender.isdigit() and cantidadVender != "R":
                            cantidadVender = int(cantidadVender)
                            if cantidadVender == 0:
                                print("La venta debe tener minimo 1 libro vendido")
                            else:
                                if libro[3] >= cantidadVender and cantidadVender != "R":
                                    sentencia = """UPDATE Libros
                                                    SET Cantidad = ?
                                                    WHERE ISBN = ?"""
                                    parametros = [(libro[3] - cantidadVender), codigoNombreLibro]
                                    cursor.execute(sentencia, parametros)
                                    conexion.commit()
                                    listaVentas.append(tuple([f"V-{int(listaVentas[-1][0][2::])+5}", cliente[1], libro[0], cantidadVender, libro[2] * cantidadVender]))
                                    parametros = [f"V-{int(listaVentas[-1][0][2::])}", cliente[1], libro[0], cantidadVender, libro[2] * cantidadVender]
                                    sentencia = """INSERT INTO Ventas(ID_Venta, ID_Cliente, ISBN, Cant_Vendida, Total_Vendido)
                                                    VALUES(?,?,?,?,?)"""
                                    cursor.execute(sentencia, parametros)
                                    conexion.commit()
                                    libro[3] -= cantidadVender
                                    print("Venta ingresada correctamente")
                                    cantidadVender = "R"
                                    codigoNombreLibro = "R"
                                else:
                                    print(f"Hay {libro[3]} libros disponibles en este momento para este titulo")       
                        else:
                            if cantidadVender != "R":
                                print("Debe ingresar solo digitos")
                else:
                    if libroRegistrado and cantidadVender != "R":
                        print("No hay libros disponibles en este momento para este titulo")
                        cantidadVender = "R"
                        codigoNombreLibro = "R"

def opcionVentas2(listaClientes, listaLibros, listaVentas):
        if len(listaVentas) == 0:
            print("No hay ventas registradas")
        else:
            

            sentencia = """SELECT * FROM Ventas"""

            cursor.execute(sentencia)

            ventas = cursor.fetchall()

            tablaVentas = PrettyTable(["ID_Venta", "ID_Cliente", "ISBN", "Cant_Vendida", "Total_Vendido"])

            for id_venta, id_cliente, isbn, cant_vendida, total_vendido in ventas:
                tablaVentas.add_row([id_venta, id_cliente, isbn, cant_vendida, total_vendido])

            print(tablaVentas)

            

def opcionVentas3(listaClientes, listaLibros, listaVentas):
    if len(listaVentas) == 0:
        print("No hay ventas registradas")
    else:
        codigoVenta = ""
        while codigoVenta != "R":
            codigoVentaRegistrado = False
            codigoVenta = input("(R para regresar) - Digite el 'Codigo Venta' de la venta que desea actualizar: ").strip()
            for venta in listaVentas:
                if codigoVenta in venta:
                    codigoVentaRegistrado = True
                    print()
                    print("'Codigo Venta' encontrado")
                    break
                else:
                    if venta == listaVentas[-1] and codigoVenta != "R":
                        print("Ese 'Codigo Venta' no esta registrado")
            if codigoVentaRegistrado:
                opcionActualizar = ""
                while opcionActualizar != "R":
                    opcionActualizar = input("""
|OPCIONES ACTUALIZAR|
R- Retroceder
1- Codigo del cliente
2- Codigo del libro
3- Cantidad vendida
Digite una opcion: """).strip()
                    if opcionActualizar.isdigit() and opcionActualizar != "R":
                        while opcionActualizar != "R" and opcionActualizar != "1" and opcionActualizar != "2" and opcionActualizar != "3":
                            opcionActualizar = input("Digite una opcion disponible: ").strip()
                        if opcionActualizar == "1":
                            codigoCliente = ""
                            while codigoCliente != "R":
                                codigoCliente = input("(R para regresar) - Digite el nuevo codigo del cliente: ").strip()
                                if codigoCliente.isdigit() and codigoCliente != "R":
                                    codigoCliente = int(codigoCliente)
                                    for cliente in listaClientes:
                                        if int(codigoCliente) in cliente:
                                            codigoClienteRegistrado = True
                                            break
                                        else:
                                            if cliente == listaClientes[-1]:
                                                print("Ese codigo no esta registrado")
                                                codigoClienteRegistrado = False

                                    if codigoClienteRegistrado:
                                        sentencia = """UPDATE Ventas
                                                        SET ID_Cliente = ?
                                                        WHERE ID_Venta = ?"""
                                        parametros = [codigoCliente, codigoVenta]
                                        cursor.execute(sentencia, parametros)
                                        conexion.commit()
                                        indice = listaVentas.index(venta)
                                        venta = list(venta)
                                        venta[1] = codigoCliente
                                        venta = tuple(venta)
                                        listaVentas[indice] = venta
                                        print("Codigo del cliente cambiado correctamente")
                                        break
                                else:
                                    if codigoCliente != "R":
                                        print("Debe ingresar solo digitos") 

                        elif opcionActualizar == "2":
                            codigoLibro = ""
                            while codigoLibro != "R":
                                codigoLibro = input("(R para regresar) - Digite el nuevo codigo del libro: ").strip()
                                if codigoLibro.isdigit() and codigoLibro != "R":
                                    codigoLibro = int(codigoLibro)
                                    for libro in listaLibros:
                                        if int(codigoLibro) in libro:
                                            codigoLibroRegistrado = True
                                            break
                                        else:
                                            if libro == listaLibros[-1]:
                                                print("Ese codigo no esta registrado")
                                                codigoLibroRegistrado = False
                                    if codigoLibroRegistrado:
                                        if libro[3] >= venta[3]:
                                            libroViejo = venta[2]
                                            if int(libroViejo) != libro[0]:
                                                sentencia = """UPDATE Ventas
                                                                SET ISBN = ?
                                                                WHERE ID_Venta = ?"""
                                                parametros = [codigoLibro, codigoVenta]
                                                cursor.execute(sentencia, parametros)
                                                conexion.commit()
                                                libro[3] -= venta[3]
                                                sentencia = """UPDATE Libros
                                                                SET Cantidad = ?
                                                                WHERE ISBN = ?"""
                                                listaLibros[listaLibros.index(libro)][3] = libro[3]
                                                parametros = [libro[3], libro[0]]
                                                cursor.execute(sentencia, parametros)
                                                conexion.commit()
                                                indice = listaVentas.index(venta)
                                                venta = list(venta)
                                                venta[2] = codigoLibro
                                                sentencia = """UPDATE Ventas
                                                                SET Total_Vendido = ?
                                                                WHERE ID_Venta = ?"""
                                                parametros = [(venta[3] * libro[2]), codigoVenta]
                                                cursor.execute(sentencia, parametros)
                                                conexion.commit()
                                                venta[4] = venta[3] * libro[2]
                                                venta = tuple(venta)
                                                listaVentas[indice] = venta
                                                for libro in listaLibros:
                                                    if int(libroViejo) in libro:
                                                        libro[3] += venta[3]
                                                        sentencia = """UPDATE Libros
                                                                        SET Cantidad = ?
                                                                        WHERE ISBN = ?"""
                                                        parametros = [(libro[3]), libroViejo] #AQUI ERROR
                                                        cursor.execute(sentencia, parametros)
                                                        conexion.commit()
                                                        libro[3]
                                                        print("Codigo del libro cambiado correctamente")
                                                break
                                            else:
                                                print("El codigo es el mismo que ya tiene")
                                        else:
                                            print("No es posible realizar el cambio porque la cantidad vendida no se encuentra disponible para este titulo")
                                else:
                                    if codigoLibro != "R":
                                        print("Debe ingresar solo digitos") 

                        elif opcionActualizar == "3":
                            cantidadVendida = ""
                            while cantidadVendida != "R":
                                cantidadVendida = input("(R para regresar) - Digite la nueva cantidad vendida del libro: ").strip()
                                if cantidadVendida.isdigit() and cantidadVendida != "R":
                                    cantidadVendida = int(cantidadVendida)
                                    if cantidadVendida > 0:
                                        cambiado = False
                                        for venta in listaVentas:
                                            if cambiado == False:
                                                for libro in listaLibros:
                                                    if codigoVenta in venta:
                                                        if venta[2] in libro:
                                                            if libro[3] + venta[3] < cantidadVendida:
                                                                print(f"Solo hay {libro[3]} de libros disponibles para este titulo")
                                                                cambiado = True
                                                                break
                                                            else:
                                                                sentencia = """UPDATE Ventas
                                                                                SET Cant_Vendida = ?
                                                                                WHERE ID_Venta = ?"""
                                                                parametros = [cantidadVendida, codigoVenta]
                                                                cursor.execute(sentencia, parametros)
                                                                conexion.commit()
                                                                if cantidadVendida < venta[3]:
                                                                    sentencia = """UPDATE Libros
                                                                                    SET Cantidad = ?
                                                                                    WHERE ISBN = ?"""
                                                                    parametros = [(libro[3] + (venta[3] - cantidadVendida)), libro[0]]
                                                                    cursor.execute(sentencia, parametros)
                                                                    conexion.commit()
                                                                    libro[3] = libro[3] + (venta[3] - cantidadVendida)
                                                                elif cantidadVendida > venta[3]:
                                                                    sentencia = """UPDATE Libros
                                                                                    SET Cantidad = ?
                                                                                    WHERE ISBN = ?"""
                                                                    parametros = [(libro[3] - (cantidadVendida - venta[3])), libro[0]]
                                                                    cursor.execute(sentencia, parametros)
                                                                    conexion.commit()
                                                                    libro[3] = libro[3] - (cantidadVendida - venta[3])
                                                                indice = listaVentas.index(venta)
                                                                venta = list(venta)
                                                                venta[3] = cantidadVendida
                                                                venta[4] = cantidadVendida * libro[2]
                                                                sentencia = """UPDATE Ventas
                                                                                SET Total_Vendido = ?
                                                                                WHERE ID_Venta = ?"""
                                                                parametros = [(cantidadVendida * libro[2]), codigoVenta]
                                                                cursor.execute(sentencia, parametros)
                                                                conexion.commit()
                                                                venta = tuple(venta)
                                                                listaVentas[indice] = venta
                                                                print("Cantidad vendida del libro cambiada correctamente")
                                                                cantidadVendida = "R"
                                                                cambiado = True
                                                                break
                                        else:
                                            break
                                    else:
                                        print("La cantidad vendida debe ser mayor a 0")
                                else:
                                    if cantidadVendida != "R" and not cantidadVendida.isdigit():
                                        print("Debe ingresar solo digitos")
                                    elif cantidadVendida.isdigit():
                                        cantidadVendida = int(cantidadVendida)
                                        if cantidadVendida <= 0:
                                            print("Debe ingresar un valor mayor a 0") 

def opcionVentas4(listaLibros, listaVentas):
    if len(listaVentas) == 0:
        print("No hay ventas registradas")
    else:
        codigoVenta = ""
        while codigoVenta != "R":
            if len(listaVentas) == 0:
                print("\nNo quedan ventas registradas")
                break
            else: 
                codigoVenta = input("(R para regresar) - Digite el 'Codigo Venta' de la venta que desea borrar: ").strip()
                borrado = False
                seguridad = ""
                for venta in listaVentas:
                    if codigoVenta in venta:
                        for libro in listaLibros:
                            if venta[2] == libro[0]:
                                while True:
                                    seguridad = input("¿Seguro que desea borrar? Si / No: ").strip()
                                    if seguridad == "Si":
                                        sentencia = """UPDATE Libros
                                                        SET Cantidad = ?
                                                        WHERE ISBN = ?"""
                                        libro[3] += venta[3]                                        
                                        parametros = [libro[3], libro[0]]
                                        cursor.execute(sentencia, parametros)
                                        conexion.commit()
                                        del(listaVentas[listaVentas.index(venta)])
                                        sentencia = """DELETE FROM Ventas
                                                        WHERE ID_Venta = ?"""
                                        parametros = [codigoVenta]
                                        cursor.execute(sentencia, parametros)
                                        conexion.commit()
                                        print("Venta borrada correctamente")
                                        borrado = True
                                        break
                                    elif seguridad == "No":
                                        break
                                    else:
                                        print("Digite una opcion disponible")
                    else:
                        if venta == listaVentas[-1] and codigoVenta != "R" and not borrado and seguridad == "Si":
                            print("Ese 'Codigo Venta' no esta registrado")
                        if venta == listaVentas[-1] and codigoVenta != "R" and not borrado:
                            print("Ese 'Codigo Venta' no esta registrado")

def opcionVentas5(listaVentas):
    if len(listaVentas) == 0:
        print("No hay ventas registradas")
    else:
        codigoVenta = ""
        while codigoVenta != "R":
            codigoVenta = input("(R para regresar) - Digite el 'Codigo Venta' que va a buscar: ").strip()
            for venta in listaVentas:
                if codigoVenta in venta:
                    sentencia = """SELECT * FROM Ventas
                                    WHERE ID_Venta = ?"""
                    parametros = [codigoVenta]
                    cursor.execute(sentencia, parametros)
                    venta = cursor.fetchall()
                    tablaVenta = PrettyTable(["ID_Venta", "ID_Cliente", "ISBN", "Cant_Vendida", "Total_Vendido"])
                    for id_venta, id_cliente, isbn, cant_vendida, total_vendido in venta:
                        tablaVenta.add_row([id_venta, id_cliente, isbn, cant_vendida, total_vendido])
                    print(tablaVenta)
                else:
                    if venta == listaVentas[-1] and codigoVenta != "R":
                        print("Ese 'Codigo Venta' no esta registrado")