from sqlLibreria import *
from prettytable import PrettyTable
conexion, cursor = conectar_bd("sistemaVentas.db")


def opcionClientes1(listaClientes):
    clienteNombre = ""
    while clienteNombre != "R":
        clienteNombre = input("(R para regresar) - Digite el nombre del cliente: ").strip()
        if clienteNombre.isdigit():
            if clienteNombre == "R":
                pass
            else:
                print("No puede ingresar numeros")
        elif not clienteNombre.isalpha():
            print("Solo puede ingresar valores alfabeticos")
        else:
                clienteCodigo = ""
                while clienteCodigo != "R" and clienteNombre != "R":
                        clienteCodigo = input("(R para regresar) - Digite el codigo del cliente: ").strip()
                        if clienteCodigo.isdigit() and clienteCodigo != "R":
                            for b in listaClientes:
                                if int(clienteCodigo) in b:
                                    print("El codigo del cliente ya esta registrado")
                                    codigoRegistrado = True
                                    break
                                else:
                                    codigoRegistrado = False
                            if not codigoRegistrado:
                                listaClientes.append([clienteNombre, int(clienteCodigo)])
                                parametros = [clienteNombre, int(clienteCodigo)]
                                
                                sentencia = """INSERT INTO Clientes(Nombre, ID)
                                                VALUES(?,?)"""
                                cursor.execute(sentencia, parametros)
                                conexion.commit()
                                
                                print("El cliente ha sido añadido correctamente")
                                break
                        else:
                            if not clienteCodigo.isdigit() and clienteCodigo != "R":
                                print("Debe ingresar solo digitos")

def opcionClientes2(listaClientes):
    if len(listaClientes) == 0:
        print("No hay clientes registrados")
    else:
        

        sentencia = """SELECT * FROM Clientes"""

        cursor.execute(sentencia)

        clientes = cursor.fetchall()

        tablaClientes = PrettyTable(["Nombre", "ID"])

        for nombre, id in clientes:
            tablaClientes.add_row([nombre, id])

        print(tablaClientes)

        

def opcionClientes3(listaClientes, listaVentas):
    if len(listaClientes) == 0:
            print("No hay clientes en la lista")
    else:
        opcionActualizar = ""
        while opcionActualizar != "R":
            opcionActualizar = input("""
|OPCIONES ACTUALIZAR|
R- Retroceder
1- Nombre
2- Codigo
Digite una opcion: """).strip()
            while opcionActualizar != "R" and opcionActualizar != "1" and opcionActualizar != "2":
                opcionActualizar = input("Digite una opcion disponible: ").strip()
            if opcionActualizar == "1":
                clienteCodigoViejo = ""
                while clienteCodigoViejo != "R":
                    clienteCodigoViejo = input("(R para regresar) - Digite el codigo del cliente: ").strip()
                    if not clienteCodigoViejo.isdigit() and clienteCodigoViejo != "R":
                        print("Solo puede ingresar digitos")
                    else:
                        if clienteCodigoViejo != "R":
                            clienteCodigoViejo = int(clienteCodigoViejo)
                            for i in listaClientes:
                                if clienteCodigoViejo in i:
                                    codigoViejoRegistrado = True
                                    break
                                else:
                                    if i == listaClientes[-1]:
                                        print(i, listaClientes, clienteCodigoViejo)
                                        print("El codigo del cliente no esta registrado")
                                        codigoViejoRegistrado = False
                            if codigoViejoRegistrado:
                                clienteNombreNuevo = ""
                                while clienteNombreNuevo != "R":
                                    clienteNombreNuevo = input("(R para regresar) - Digite el nombre nuevo: ").strip()
                                    if not clienteNombreNuevo.isalpha() and clienteNombreNuevo != "R":
                                        print("Solo puede ingresar valores alfabeticos")
                                    else:
                                        if clienteNombreNuevo != "R":
                                            for b in listaClientes:
                                                    if clienteCodigoViejo in b:
                                                                sentencia = """UPDATE Clientes
                                                                                SET Nombre = ?
                                                                                WHERE ID = ?"""
                                                                parametros = [clienteNombreNuevo, clienteCodigoViejo]
                                                                cursor.execute(sentencia, parametros)
                                                                conexion.commit()
                                                                
                                                                print("Nombre cambiado correctamente")
                                                                clienteNombreNuevo = "R"
                                                                break
            elif opcionActualizar == "2":
                clienteCodigoViejo = ""
                while clienteCodigoViejo != "R":
                    clienteCodigoViejo = input("(R para regresar) - Digite el codigo del cliente: ").strip()
                    if not clienteCodigoViejo.isdigit() and clienteCodigoViejo != "R":
                        print("Solo puede ingresar digitos")
                    else:
                        if clienteCodigoViejo != "R":
                            clienteCodigoViejo = int(clienteCodigoViejo)
                            for i in listaClientes:
                                if clienteCodigoViejo in i:
                                    codigoViejoRegistrado = True
                                    break
                                else:
                                    if i == listaClientes[-1]:
                                        print("El codigo del cliente no esta registrado")
                                        codigoViejoRegistrado = False
                            if codigoViejoRegistrado:
                                clienteCodigoNuevo = ""
                                while clienteCodigoNuevo != "R":
                                    clienteCodigoNuevo = input("(R para regresar) - Digite el codigo nuevo: ").strip()
                                    if not clienteCodigoNuevo.isdigit() and clienteCodigoNuevo != "R":
                                        print("Solo puede ingresar digitos")
                                    else:
                                        if clienteCodigoNuevo != "R":
                                            clienteCodigoNuevo = int(clienteCodigoNuevo)
                                            for i in listaClientes:
                                                if clienteCodigoNuevo in i:
                                                    codigoNuevoRegistrado = True
                                                    print("Ese codigo ya esta registrado")
                                                    break
                                                else:
                                                    codigoNuevoRegistrado = False
                                            if not codigoNuevoRegistrado:
                                                for b in listaClientes:
                                                    if clienteCodigoViejo in b:
                                                        for venta in listaVentas:
                                                            if venta[1] == clienteCodigoViejo:
                                                                sentencia = """UPDATE Ventas
                                                                                SET ID_Cliente = ?
                                                                                WHERE ID_Cliente = ?"""
                                                                parametros = [clienteCodigoNuevo, clienteCodigoViejo]
                                                                cursor.execute(sentencia, parametros)
                                                                conexion.commit()
                                                                indice = listaVentas.index(venta)
                                                                venta = list(venta)
                                                                venta[1] = clienteCodigoNuevo
                                                                venta = tuple(venta)
                                                                listaVentas[indice] = venta
                                                                b[1] = clienteCodigoNuevo
                                                            if venta == listaVentas[-1]:
                                                                
                                                                sentencia = """UPDATE Clientes
                                                                                SET ID = ?
                                                                                WHERE ID = ?"""
                                                                parametros = [clienteCodigoNuevo, clienteCodigoViejo]
                                                                cursor.execute(sentencia, parametros)
                                                                conexion.commit()
                                                                b[1] = clienteCodigoNuevo
                                                                print("Codigo cambiado correctamente")
                                                                clienteCodigoNuevo = "R"
                                                                break

                                                
def opcionClientes4(listaClientes, listaVentas):
    if len(listaClientes) == 0:
        print("No hay clientes registrados")
    else:
                codigoBorrar = ""
                while codigoBorrar != "R":
                    if len(listaClientes) == 0:
                        print("\nNo quedan clientes en la lista")
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
                                for i in listaClientes:
                                    if codigoBorrar == i[1]:
                                        if len(listaVentas) > 0:
                                            for venta in listaVentas:
                                                if i[1] == venta[1]:
                                                    print("No se puede borrar el cliente porque ya se encuentra en una venta")
                                                    enVenta = True
                                                    break
                                                else:
                                                    if venta == listaVentas[-1] and not enVenta:
                                                        del(listaClientes[listaClientes.index(i)])
                                                        sentencia = """DELETE FROM Clientes
                                                                        WHERE ID = ?"""
                                                        parametros = [codigoBorrar]
                                                        cursor.execute(sentencia, parametros)
                                                        conexion.commit()
                                                        print("Se ha borrado el codigo con su respectivo nombre correctamente")
                                                        borrado = True
                                        else:
                                            if codigoBorrar == i[1]:
                                                del(listaClientes[listaClientes.index(i)])
                                                sentencia = """DELETE FROM Clientes
                                                                WHERE ID = ?"""
                                                parametros = [codigoBorrar]
                                                cursor.execute(sentencia, parametros)
                                                conexion.commit()
                                                print("Se ha borrado el codigo con su respectivo nombre correctamente")
                                                break
                                            else:
                                                if i == listaClientes[-1]:
                                                    print("El codigo no se encuentra registrado")

                                    else:
                                        if i == listaClientes[-1] and not borrado and not enVenta:
                                            print("El codigo no se encuentra registrado")

def opcionClientes5(listaClientes):
    if len(listaClientes) == 0:
        print("No hay clientes registrados")
    else:
                codigoBuscar = ""
                while codigoBuscar != "R":
                    codigoBuscar = input("(R para regresar) - Digite el codigo que desea buscar: ").strip()
                    if not codigoBuscar.isdigit() and codigoBuscar != "R":
                        print("Debe ingresar solo digitos")
                    else:
                        if codigoBuscar != "R":
                            codigoBuscar = int(codigoBuscar)
                            for i in listaClientes:
                                if codigoBuscar in i:
                                    sentencia = """SELECT * FROM Clientes
                                                    WHERE ID = ?"""
                                    parametros = [codigoBuscar]
                                    cursor.execute(sentencia, parametros)
                                    cliente = cursor.fetchall()
                                    tablaCliente = PrettyTable(["Nombre", "ID"])
                                    for nombre, id in cliente:
                                        tablaCliente.add_row([nombre, id])
                                    print(tablaCliente)
                                    break
                                else:
                                    if i == listaClientes[-1]:
                                        print("El cliente no esta registrado")
