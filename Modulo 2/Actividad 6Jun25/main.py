import operaciones

def calculadora():
    opcion = int(input("Ingresa solo el número asignado a una operación: \n1. suma \n2. resta \n3.multiplicación \n4.división"))
    a=int(input("Ingresa un número: "))
    b=int(input("Ingresa otro número: "))


    if opcion ==1:
        resultado = operaciones.sumar(a, b)
        print(f"El resultado es: {resultado}")
    elif opcion == 2:
        resultado = operaciones.restar(a, b)
        print(f"El resultado es: {resultado}")
    elif opcion == 3:
        resultado = operaciones.multiplicar(a, b)
        print(f"El resultado es: {resultado}")
    elif opcion == 4:
        if b == 0:
            print("No se puede dividir por 0")
        else:
            resultado = operaciones.dividir(a, b)
        print(f"El resultado es: {resultado}")
    else:
        print("opción inválida")


calculadora()