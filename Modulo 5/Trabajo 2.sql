-- Crea la base de datos si no existe
CREATE DATABASE IF NOT EXISTS mercato_db;

USE mercato_db;


CREATE TABLE Dim_Tiempo (
                            ID_Tiempo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                            Fecha_Completa DATE NOT NULL,
                            Dia INT NOT NULL,
                            Mes INT NOT NULL,
                            Nombre_Mes VARCHAR(20) NOT NULL,
                            Trimestre INT NOT NULL,
                            Año INT NOT NULL
);

CREATE TABLE Dim_Cliente (
                             ID_Cliente INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                             Nombre_Completo VARCHAR(255) NOT NULL,
                             Email VARCHAR(255),
                             Segmento_Cliente VARCHAR(50),
                             Ciudad VARCHAR(100),
                             Pais VARCHAR(100)
);

CREATE TABLE Dim_Producto (
                              ID_Producto INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                              SKU VARCHAR(50) NOT NULL UNIQUE,
                              Nombre_Producto VARCHAR(255) NOT NULL,
                              Descripcion TEXT,
                              Categoria VARCHAR(100),
                              Marca VARCHAR(100)
);

CREATE TABLE Dim_Tienda (
                            ID_Tienda INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                            Nombre_Tienda VARCHAR(100) NOT NULL,
                            Direccion VARCHAR(255),
                            Ciudad VARCHAR(100),
                            Region VARCHAR(100)
);


-- Tabla de Hechos para las Ventas (Fact Table)

CREATE TABLE Fact_Ventas (
                             ID_Venta INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,

                             ID_Tiempo INT UNSIGNED NOT NULL,
                             ID_Cliente INT UNSIGNED NOT NULL,
                             ID_Producto INT UNSIGNED NOT NULL,
                             ID_Tienda INT UNSIGNED NOT NULL,

                             Monto_Venta DECIMAL(12, 2) NOT NULL,
                             Cantidad_Unidades INT NOT NULL,
                             Monto_Descuento DECIMAL(12, 2) DEFAULT 0.00,

                             CONSTRAINT fk_tiempo FOREIGN KEY (ID_Tiempo) REFERENCES Dim_Tiempo(ID_Tiempo),
                             CONSTRAINT fk_cliente FOREIGN KEY (ID_Cliente) REFERENCES Dim_Cliente(ID_Cliente),
                             CONSTRAINT fk_producto FOREIGN KEY (ID_Producto) REFERENCES Dim_Producto(ID_Producto),
                             CONSTRAINT fk_tienda FOREIGN KEY (ID_Tienda) REFERENCES Dim_Tienda(ID_Tienda)
);