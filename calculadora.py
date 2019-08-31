import os

def realizar_operacion(operacion, num1, num2):
    if operacion == 1:
        return num1 + num2
    elif operacion == 2:
         return num1 - num2
    elif operacion == 3:
         return num1 / num2
    elif operacion == 4:
         return num1 * num2

print("<<<<<< Bienvenidos a Programa Calculadora 1.0 >>>>>>>")
while True:
    print("********************************************")
    print("<<<<<< SELECCIONE ACCION : >>>>>>>")
    print("********************************************")
    print("1- < SUMAR >")
    print("2- < RESTAR >")
    print("3- < DIVISION >")
    print("4- < MULTIPLICACION >")
    print("********************************************")

    try:
        operacion = int(input(" SELECCIONE SU NUMERO:"))
        if operacion < 1 or operacion > 4:
            print("Numero no valido")
            continue
        num1 = float(input("Tu Primer Numero :"))
        num2 = float(input("Tu Segundo Numero :"))
    except ValueError:
        print("Por favor solo numeros")
    else:

        resultado = realizar_operacion(operacion, num1,num2)
        print(resultado)
        continuar = input(" DESEAS CONTINUAR? S/N ")
        os.system("cls")

        if continuar == "s":
           continue
        if continuar == "n":
           break
