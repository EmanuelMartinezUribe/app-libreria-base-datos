

def menuPrincipal():
    opcion = input("""
|LIBRERIA - LIBRE SOY|
R- Salir
1- CRUD Clientes
2- CRUD Libros
3- CRUD Ventas
4- Estadisticas
Digite una opcion: """).strip()
    return opcion


def menuClientes():
    opcion = input("""
|OPCIONES CLIENTES|
R- Regresar al Menu Principal
1- Ingresar Clientes
2- Listar Clientes
3- Actualizar Clientes
4- Borrar Clientes
5- Buscar Clientes
Digite una opcion: """).strip()
    return opcion

def menuLibros():
    opcion = input("""
|OPCIONES LIBROS|
R- Regresar al Menu Principal
1- Ingresar Libros
2- Listar Libros
3- Actualizar Libros
4- Borrar Libros
5- Buscar Libros
Digite una opcion: """).strip()
    return opcion

def menuVentas():
    opcion = input("""
|OPCIONES VENTAS|
R- Regresar al Menu Principal
1- Ingresar Ventas
2- Listar Ventas
3- Actualizar Ventas
4- Borrar Ventas
5- Buscar Ventas
Digite una opcion: """).strip()
    return opcion

def menuEstadisticas():
    opcion = input("""
|OPCIONES ESTADISTICAS|
R- Regresar al Menu Principal
1- Ventas de un libro por codigo
2- Libro mas y menos vendido
3- Venta total
4- Mayor compra por venta
5- Mayor volumen de venta
Digite una opcion: """).strip()
    return opcion