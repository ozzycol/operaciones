import os
from termcolor import colored, cprint
# ------OPERACIONES MATEMATICAS CON FUNCIONES---------

def numeros():
    num1=int(input("\nIngrese el primer operando: "))
    num2=int(input("Ingrese el segundo operando: "))
    return num1, num2

def suma(num1, num2): #declaro la funcion con los parametros que pedi
    resultado=num1+num2 #resultado es la suma de los dos numero
    return resultado #retorno resultado

def resta(num1, num2): #declaro la funcion con los parametros que pedi
    resultado=num1-num2 #resultado es la suma de los dos numero
    return resultado #retorno resultado

def multip(num1, num2): #declaro la funcion con los parametros que pedi
    resultado=num1*num2 #resultado es la suma de los dos numero
    return resultado #retorno resultado

def division(num1, num2): #declaro la funcion con los parametros que pedi
    if num2==0:
        resultado="El operador2 no puede ser 0"
    else:
        resultado=num1/num2 #resultado es la suma de los dos numero
    return resultado #retorno resultado

def potencia(num1, num2):
    resultado=num1**num2
    return resultado

def modulo(num1, num2):
    if num2==0:
        resultado="El operador2 no puede ser 0"
    else:
        resultado=num1%num2 #resultado es la suma de los dos numero
    return resultado #retorno resultado

def pemtero(num1, num2):
    if num2==0:
        resultado="El operador2 no puede ser 0"
    else:
        resultado=num1//num2 #resultado es la suma de los dos numero
    return resultado #retorno resultado

def inicio(num1,num2):
    
    print("                     ---------OPERACIONES MATEMATICAS BASICAS EN PYTHON----------\n")
    print("1.- Suma")
    print("2.- Resta")
    print("3.- Multiplicación")
    print("4.- División")
    print("5.- Potenciación")
    print("6.- Modulo")
    print("7.- Parte entera \n \n")
    operacion= input("           Ingrese el numero correspondiente a la operación que desea realizar: ")
    if operacion=="1":

        print("El resultado de la operación es: ", suma(num1,num2) )
    else:
        if operacion=="2":
         print("El resultado de la operación es: ", resta(num1, num2) )
        else:
            if operacion=="3":
                print("El resultado de la operación es: ", multip(num1, num2) )
            else:
                if operacion=="4":
                    print("El resultado de la operación es: ", division(num1, num2) )
                else:
                    if operacion=="5":
                        print("El resultado de la operación es: ", potencia(num1, num2) )
                    else:
                        if operacion=="6":
                            print("El resultado de la operación es: ", modulo(num1, num2) )
                        else:
                            if operacion=="7":
                                print("El resultado de la operación es: ", pemtero(num1, num2) )
                            else:
                                cprint("\t   \t       Valor ingresado es invalido", 'red', attrs=['blink'])
                                input()
    return operacion


os.system("cls")
num1, num2=numeros()
inicio(num1,num2)







