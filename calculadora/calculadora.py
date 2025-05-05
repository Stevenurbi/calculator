def calcular(dato1, dato2, operacion):
    if operacion == "+":
        return dato1 + dato2
    elif operacion == "-":
        return dato1 - dato2
    elif operacion == "*":
        return dato1 * dato2
    elif operacion == "/":
        if dato2 == 0:
            return "No se puede dividir"
        else:
            return dato1 / dato2
    else:
        return "Operación no válida, ingrese el símbolo correcto."

while True:
    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        operacion = input("Ingrese la operación (+, -, *, /): ")

        resultado = calcular(num1, num2, operacion)
        print("Resultado:", resultado)
    except ValueError:
        print("Error: Ingrese un número válido.")

    