from sqlLibreria import *
from prettytable import PrettyTable
conexion, cursor = conectar_bd("sistemaVentas.db")

def opcionLibros1(listaLibros):
    libroCodigo = ""
    while libroCodigo != "R":
        libroCodigo = input("(R para regresar) - Digite el codigo del libro: ").strip()
        if libroCodigo.isdigit() and libroCodigo != "R":
            for b in listaLibros:
                if int(libroCodigo) == b[0]:
                    print("El codigo del libro ya esta registrado")
                    codigoRegistrado = True
                    break
                else:
                    codigoRegistrado = False
            if not codigoRegistrado:
                libroNombre = ""
                while libroNombre != "R":
                    libroNombre = input("(R para regresar) - Digite el nombre del libro: ").strip()
                    for i in listaLibros:
                        if libroNombre in i:
                            print("El nombre del libro ya esta registrado")
                            nombreRegistrado = True
                            break
                        else:
                            nombreRegistrado = False
                    if not nombreRegistrado and libroNombre != "R":
                        precioLibro = ""
                        while precioLibro != "R":
                            precioLibro = input("(R para regresar) - Digite el precio del libro: ").strip()
                            if not precioLibro.isdigit() and precioLibro != "R":
                                print("Debe digitar solo digitos")
                            else:
                                if precioLibro != "R":
                                    precioLibro = int(precioLibro)
                                    cantidadLibro = ""
                                    while cantidadLibro != "R":
                                        cantidadLibro = input("(R para regresar) - Digite la cantidad que hay del libro: ").strip()
                                        if not cantidadLibro.isdigit() and cantidadLibro != "R":
                                            print("Debe digitar solo digitos")
                                        else:
                                            if cantidadLibro != "R":
                                                cantidadLibro = int(cantidadLibro)
                                                listaLibros.append([int(libroCodigo), libroNombre, precioLibro, cantidadLibro])
                                                parametros = [int(libroCodigo), libroNombre, precioLibro, cantidadLibro]
                                                
                                                sentencia = """INSERT INTO Libros(ISBN, Nombre, Precio, Cantidad)
                                                                VALUES(?,?,?,?)"""
                                                cursor.execute(sentencia, parametros)
                                                conexion.commit()
                                                
                                                print("Se ha añadido el libro correctamente")
                                                precioLibro = "R"
                                                libroNombre = "R"
                                                break
        else:
            if not libroCodigo.isdigit() and libroCodigo != "R":
                print("Debe ingresar solo digitos")
            
def opcionLibros2(listaLibros):
    if len(listaLibros) == 0:
        print("No hay libros registrados")
    else:
        

        sentencia = """SELECT * FROM Libros"""

        cursor.execute(sentencia)

        libros = cursor.fetchall()

        tablaLibros = PrettyTable(["ISBN", "Nombre", "Precio", "Cantidad"])

        for isbn, nombre, precio, cantidad in libros:
            tablaLibros.add_row([isbn, nombre, precio, cantidad])

        print(tablaLibros)

        

def opcionLibros3(listaLibros, listaVentas):
    if len(listaLibros) == 0:
            print("No hay libros en el catalogo")
    else:
        opcionActualizar = ""
        while opcionActualizar != "R":
            opcionActualizar = input("""
|OPCIONES ACTUALIZAR|
R- Retroceder
1- Codigo
2- Nombre
3- Precio
4- Cantidad
Digite una opcion: """).strip()
            if opcionActualizar == "1":
                libroCodigoViejo = ""
                while libroCodigoViejo != "R":
                    libroCodigoViejo = input("(R para regresar) - Digite el codigo actual: ").strip()
                    if not libroCodigoViejo.isdigit() and libroCodigoViejo != "R":
                        print("Solo puede ingresar digitos")
                    else:
                        if libroCodigoViejo != "R":
                            libroCodigoViejo = int(libroCodigoViejo)
                            for i in listaLibros:
                                if libroCodigoViejo == i[0]:
                                    codigoViejoRegistrado = True
                                    break
                                else:
                                    if i == listaLibros[-1]:
                                        print("El codigo del libro no esta registrado")
                                        codigoViejoRegistrado = False
                            if codigoViejoRegistrado:
                                libroCodigoNuevo = ""
                                while libroCodigoNuevo != "R":
                                    libroCodigoNuevo = input("(R para regresar) - Digite el codigo nuevo: ").strip()
                                    if not libroCodigoNuevo.isdigit() and libroCodigoNuevo != "R":
                                        print("Solo puede ingresar digitos")
                                    else:
                                        if libroCodigoNuevo != "R":
                                            libroCodigoNuevo = int(libroCodigoNuevo)
                                            for i in listaLibros:
                                                if libroCodigoNuevo in i:
                                                    codigoNuevoRegistrado = True
                                                    print("Ese codigo ya esta registrado")
                                                    break
                                                else:
                                                    codigoNuevoRegistrado = False
                                            if not codigoNuevoRegistrado:
                                                for b in listaLibros:
                                                    if libroCodigoViejo in b:
                                                        for venta in listaVentas:
                                                            if venta[2] == libroCodigoViejo:
                                                                sentencia = """UPDATE Ventas
                                                                                SET ISBN = ?
                                                                                WHERE ISBN = ?"""
                                                                parametros = [libroCodigoNuevo, libroCodigoViejo]
                                                                cursor.execute(sentencia, parametros)
                                                                conexion.commit()
                                                                indice = listaVentas.index(venta)
                                                                venta = list(venta)
                                                                venta[2] = libroCodigoNuevo
                                                                venta = tuple(venta)
                                                                listaVentas[indice] = venta
                                                                b[0] = libroCodigoNuevo
                                                            if venta == listaVentas[-1]:
                                                                
                                                                sentencia = """UPDATE Libros
                                                                                SET ISBN = ?
                                                                                WHERE ISBN = ?"""
                                                                parametros = [libroCodigoNuevo, libroCodigoViejo]
                                                                cursor.execute(sentencia, parametros)
                                                                conexion.commit()
                                                                b[0] = libroCodigoNuevo
                                                                print("Codigo cambiado correctamente")
                                                                libroCodigoNuevo = "R"
                                                                break
            elif opcionActualizar == "2":
                libroCodigoViejo = ""
                while libroCodigoViejo != "R":
                    libroCodigoViejo = input("(R para regresar) - Digite el codigo del libro: ").strip()
                    if libroCodigoViejo.isdigit():
                        libroCodigoViejo = int(libroCodigoViejo)
                        for i in listaLibros:
                            if libroCodigoViejo in i:
                                codigoViejoRegistrado = True
                                break
                            else:
                                if i == listaLibros[-1] and libroCodigoViejo != "R":
                                    print("El codigo del libro no esta registrado")
                                    codigoViejoRegistrado = False
                        if codigoViejoRegistrado and libroCodigoViejo != "R":
                            libroNombreNuevo = ""
                            while libroNombreNuevo != "R":
                                libroNombreNuevo = input("(R para regresar) - Digite el nombre nuevo: ").strip()
                                if libroNombreNuevo != "R":
                                    sentencia = """UPDATE Libros
                                                    SET Nombre = ?
                                                    WHERE ISBN = ?"""
                                    parametros = [libroNombreNuevo, libroCodigoViejo]
                                    cursor.execute(sentencia, parametros)
                                    conexion.commit()
                                    libroNombreNuevo = "R"
                                    print("Nombre cambiado correctamente")
                    else:
                        print("Debe ingresar solo digitos")
            elif opcionActualizar == "3":
                codigoLibro = ""
                while codigoLibro != "R":
                    cambiado = False
                    codigoLibro = input("(R para regresar) - Digite el codigo del libro: ").strip()
                    if codigoLibro.isdigit() and codigoLibro != "R":
                        codigoLibro = int(codigoLibro)
                        for i in listaLibros:
                            nuevoPrecio = ""
                            if int(codigoLibro) == i[0]:
                                while nuevoPrecio != "R":
                                    nuevoPrecio = input("(R para regresar) - Digite el nuevo precio: ").strip()
                                    if nuevoPrecio.isdigit() and nuevoPrecio != "R":
                                        nuevoPrecio = int(nuevoPrecio)
                                        sentencia = """UPDATE Libros
                                                        SET Precio = ?
                                                        WHERE ISBN = ?"""
                                        parametros = [nuevoPrecio, codigoLibro]
                                        cursor.execute(sentencia, parametros)
                                        conexion.commit()
                                        i[2] = nuevoPrecio
                                        print("Precio cambiado correctamente")
                                        cambiado = True
                                        break
                                    else:
                                        if nuevoPrecio != "R":
                                            print("Debe ingresar solo digitos")
                            else:
                                if i == listaLibros[-1] and nuevoPrecio != "R" and cambiado == False:
                                    print("Ese codigo no esta registrado")
                    else:
                        if codigoLibro != "R":
                            print("Debe ingresar solo digitos")

            elif opcionActualizar == "4":
                nombreCodigo = ""
                while nombreCodigo != "R":
                    cambiado = False
                    nombreCodigo = input("(R para regresar) - Digite el codigo del libro: ").strip()
                    if nombreCodigo.isdigit() and nombreCodigo != "R":
                        nombreCodigo = int(nombreCodigo)
                        for i in listaLibros:
                            if int(nombreCodigo) == i[0]:
                                nuevaCantidad = ""
                                while nuevaCantidad != "R":
                                    nuevaCantidad = input("(R para regresar) - Digite la nueva cantidad: ").strip()
                                    if nuevaCantidad.isdigit() and nuevaCantidad != "R":
                                        nuevaCantidad = int(nuevaCantidad)
                                        sentencia = """UPDATE Libros
                                                        SET Cantidad = ?
                                                        WHERE ISBN = ?"""
                                        parametros = [nuevaCantidad, nombreCodigo]
                                        cursor.execute(sentencia, parametros)
                                        conexion.commit()
                                        i[3] = nuevaCantidad
                                        print("Cantidad cambiada correctamente")
                                        cambiado = True
                                        break
                                    else:
                                        if nuevaCantidad != "R":
                                            print("Debe ingresar solo digitos")
                            else:
                                if i == listaLibros[-1] and nombreCodigo != "R" and cambiado == False:
                                    print("Ese codigo no esta registrado")
                    else: 
                        if nombreCodigo != "R":
                            print("Debe ingresar solo digitos")

def opcionLibros4(listaLibros, listaVentas):
    if len(listaLibros) == 0:
        print("No hay libros registrados")
    else:
                codigoBorrar = ""
                while codigoBorrar != "R":
                    if len(listaLibros) == 0:
                        print("\nNo quedan libros en la lista")
                        break
                    else:
                        codigoBorrar = input("(R para regresar) - Digite el codigo que desea borrar: ").strip()
                        if not codigoBorrar.isdigit() and codigoBorrar != "R":
                            print("Debe ingresar solo digitos")
                        else:
                            enVenta = False
                            borrado = False
                            if codigoBorrar != "R":
                                codigoBorrar = int(codigoBorrar)
                                for i in listaLibros:
                                    if codigoBorrar == i[0]:
                                        if len(listaVentas) > 0:
                                            for venta in listaVentas:
                                                if i[0] == venta[2]:
                                                    print("No se puede borrar el libro porque ya se encuentra en una venta")
                                                    enVenta = True
                                                    break
                                                else:
                                                    if venta == listaVentas[-1] and not enVenta:
                                                        del(listaLibros[listaLibros.index(i)])
                                                        sentencia = """DELETE FROM Libros
                                                                        WHERE ISBN = ?"""
                                                        parametros = [codigoBorrar]
                                                        cursor.execute(sentencia, parametros)
                                                        conexion.commit()
                                                        print("Se ha borrado el libro correctamente")
                                                        borrado = True
                                        else:
                                            if codigoBorrar in i:
                                                del(listaLibros[listaLibros.index(i)])
                                                sentencia = """DELETE FROM Libros
                                                                WHERE ISBN = ?"""
                                                parametros = [codigoBorrar]
                                                cursor.execute(sentencia, parametros)
                                                conexion.commit()
                                                print("Se ha borrado el libro correctamente")
                                                break
                                            else:
                                                if i == listaLibros[-1]:
                                                    print("El codigo no se encuentra registrado")
                                    else:
                                        if i == listaLibros[-1] and not borrado and not enVenta:
                                            print("El codigo no se encuentra registrado")
            
def opcionLibros5(listaLibros):
    if len(listaLibros) == 0:
        print("No hay libros registrados")
    else:
                codigoBuscar = ""
                while codigoBuscar != "R":
                    codigoBuscar = input("(R para regresar) - Digite el codigo que desea buscar: ").strip()
                    if not codigoBuscar.isdigit() and codigoBuscar != "R":
                        print("Debe ingresar solo digitos")
                    else:
                        if codigoBuscar != "R":
                            codigoBuscar = int(codigoBuscar)
                            for i in listaLibros:
                                if codigoBuscar in i:
                                    sentencia = """SELECT * FROM Libros
                                                    WHERE ISBN = ?"""
                                    parametros = [codigoBuscar]
                                    cursor.execute(sentencia, parametros)
                                    cliente = cursor.fetchall()
                                    tablaCliente = PrettyTable(["ISBN", "Nombre", "Precio", "Cantidad"])
                                    for isbn, nombre, precio, cantidad in cliente:
                                        tablaCliente.add_row([isbn, nombre, precio, cantidad])
                                    print(tablaCliente)
                                    break
                                else:
                                    if i == listaLibros[-1] and codigoBuscar != "R":
                                        print("El libro no esta registrado")
