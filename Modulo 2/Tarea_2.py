class AnalizadorFinanciero:
    # Calcula el total de ingresos en una lista de transacciones
    def calcular_total_ingresos(self, transacciones):
        #for ingreso in transacciones:
        #    total += ingreso
        return sum(transacciones)

    # Filtra y retorna solo los ingresos mayores a un umbral dado
    def filtrar_ingresos_altos(self, transacciones, umbral):
        #for ingreso in transacciones:
        #    if ingreso > umbral:
        #        ingresos_altos.append(ingreso)
        return [ingreso for ingreso in transacciones if ingreso > umbral]

    # Agrupa ingresos en un diccionario por categorías
    def agrupar_por_categoria(self, transacciones,categorias):
        agrupado = {}
        for categoria, ingreso in zip(categorias,transacciones):
            if categoria in agrupado:
                agrupado[categoria].append(ingreso)
            else:
                agrupado[categoria] = [ingreso]
        return agrupado

# Crear una instancia del analizador
analizador = AnalizadorFinanciero()

# Datos
transacciones = [100, 250, 400, 590, 340, 201, 1500]
categorias = ['salario', 'venta', 'salario', 'regalo', 'venta', 'venta', 'regalo']
umbral = 50

# Total de ingresos
total= analizador.calcular_total_ingresos(transacciones)
print(f"Total de ingresos: {total}")

#Filtrar los ingresos altos
ing_altos=analizador.filtrar_ingresos_altos(transacciones, umbral)
print(f"Total de ingresos mayores al umbral de {umbral}: {ing_altos}")

#Agrupar por categoría
agrupados = analizador.agrupar_por_categoria(transacciones, categorias)
print("Ingresos agrupados por categoría:")
for categoria, ingresos in agrupados.items():
    print(f"  {categoria}: {ingresos}")

