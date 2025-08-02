CREATE DATABASE ejercicio;
USE ejercicio;

CREATE TABLE dim_tiempo(
    id_tiempo INT PRIMARY KEY AUTO_INCREMENT,
    anio INT NOT NULL,
    trimestre INT,
    mes INT,
    nombre_mes VARCHAR(25),
    dia INT
);

#------------------------ENFOQUE OLTP (

CREATE TABLE dim_producto(
    id_producto INT PRIMARY KEY AUTO_INCREMENT,
    nombre_producto VARCHAR(25) NOT NULL,
    precio_producto DECIMAL(10,2) NOT NULL,
    categoria VARCHAR(25),
    subcategoria VARCHAR(25)
);

CREATE TABLE dim_cliente(
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nombre_cliente VARCHAR(25) NOT NULL,
    segmento VARCHAR(25),
    ciudad VARCHAR(25),
    region VARCHAR(25)
);

CREATE TABLE fac_ventas(
    id_venta INT PRIMARY KEY AUTO_INCREMENT,
    id_tiempo INT,
    id_producto INT,
    id_cliente INT,
    cantidad_ventas INT,
    monto_total DECIMAL(10,2),
    FOREIGN KEY (id_tiempo) REFERENCES dim_tiempo(id_tiempo),
    FOREIGN KEY (id_producto) REFERENCES dim_producto(id_producto),
    FOREIGN KEY (id_cliente) REFERENCES dim_cliente(id_cliente)
);

INSERT INTO dim_tiempo VALUES
(20230101, 2023, 1, 1, 'Enero', 1),
(20230102, 2023, 1, 1, 'Enero', 2),
(20230201, 2023, 1, 2, 'Febrero', 1),
(20230301, 2023, 1, 3, 'Marzo', 1);

INSERT INTO dim_producto VALUES
(1, 'Laptop Pro 15"', 'Electrónica', 'Computadores', 1200.00),
(2, 'Mouse Inalámbrico', 'Electrónica', 'Accesorios', 25.00),
(3, 'Teclado Mecánico', 'Electrónica', 'Accesorios', 80.00);

INSERT INTO dim_cliente VALUES
(101, 'Juan Pérez', 'Minorista', 'Santiago', 'Metropolitana'),
(102, 'María López', 'Corporativo', 'Valparaíso', 'Valparaíso'),
(103, 'Carlos Díaz', 'Minorista', 'Concepción', 'Biobío');

INSERT INTO fact_ventas (id_tiempo, id_producto, id_cliente, cantidad, monto_total) VALUES
(20230101, 1, 101, 2, 2400.00),
(20230102, 2, 102, 3, 75.00),
(20230201, 1, 103, 1, 1200.00),
(20230301, 3, 101, 2, 160.00);

#------------------------ENFOQUE OLAP (Análisis y Lectura)

SELECT * FROM fac_ventas;

SELECT
    t.anio,
    t.nombre_mes,
    SUM(f.monto_total) AS total_ventas
FROM fact_ventas f
JOIN dim_tiempo t ON f.id_tiempo = t.id_tiempo
GROUP BY t.anio, t.nombre_mes, t.mes
ORDER BY t.anio, t.mes;