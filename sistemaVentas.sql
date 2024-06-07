CREATE TABLE Clientes(
ID INTEGER UNIQUE PRIMARY KEY,
Nombre TEXT NOT NULL
);

CREATE TABLE Libros(
ISBN INTEGER UNIQUE PRIMARY KEY,
Nombre TEXT NOT NULL,
Precio NUMERIC NOT NULL,
Cantidad INTEGER NOT NULL
);

CREATE TABLE Ventas(
ID_Venta TEXT UNIQUE PRIMARY KEY,
ID_Cliente INTEGER NOT NULL,
ISBN INTEGER NOT NULL,
Cant_Vendida INTEGER CHECK (Cant_Vendida > 0) NOT NULL,
Total_Vendido NUMERIC NOT NULL,
FOREIGN KEY (ID_Cliente) REFERENCES Clientes(ID),
FOREIGN KEY (ISBN) REFERENCES Libros(ISBN)
);

INSERT INTO Clientes(ID, Nombre)
VALUES(3100, "Juan");

INSERT INTO Clientes(ID, Nombre)
VALUES(3101, "Maria");

INSERT INTO Clientes(ID, Nombre)
VALUES(3102, "Pedro");

INSERT INTO Clientes(ID, Nombre)
VALUES( 3103, "Laura");


INSERT INTO Libros(ISBN, Nombre, Precio, Cantidad)
VALUES(12552, "Iliada", 5300, 25);

INSERT INTO Libros(ISBN, Nombre, Precio, Cantidad)
VALUES(12553, "Platero", 2500, 16);

INSERT INTO Libros(ISBN, Nombre, Precio, Cantidad)
VALUES(12554, "Cien", 3600, 35);


INSERT INTO Ventas(ID_Venta, ID_Cliente, ISBN, Cant_Vendida, Total_Vendido)
VALUES("V-1020", 3100, 12552, 4, 21200);

INSERT INTO Ventas(ID_Venta, ID_Cliente, ISBN, Cant_Vendida, Total_Vendido)
VALUES("V-1025", 3103, 12553, 2, 5000);

INSERT INTO Ventas(ID_Venta, ID_Cliente, ISBN, Cant_Vendida, Total_Vendido)
VALUES("V-1030", 3100, 12554, 3, 10800);

INSERT INTO Ventas(ID_Venta, ID_Cliente, ISBN, Cant_Vendida, Total_Vendido)
VALUES("V-1035", 3101, 12553, 9, 22500);