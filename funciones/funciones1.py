#funcion sin parametro
def mensaje(): #se declara la funcion con def, nombre, parentisis y dos punto
    print("Estamos aprendiendo python")# sigue el codigo de la funcion
    print("Estamos aprendiendo instrucciones básicas")
    print("Poco a poco iremos avanzando")

mensaje() #se llama la funcion con el nombre y parentesis
mensaje()
print("ejecutando codigo fuera de función".upper())
mensaje()

#funcion sin parametros
def suma(): #declaro la funcion
    num1=5 #asigno 2 valores a las variables numb
    num2=7
    print(num1+num2) #pinto la salida

suma() #llamo la funcion para ejecutar

#funcion con parametro
num1= int( input("ingreso el primer sumando")) #pido primer y lo paso a num1 como entero
num2= int(input("ingrese el segundo sumando")) #pido valor 2 y lo paso num2 como entero
def suma1(num1, num2): #declaro la variable y le paso num1 y 2 como parametro
    resultado=num1+num2 # hago la suma y guardo en resultado
    print( "el resultado de la suma  de",num1, "y " ,num2, " el resultado es ",resultado)# pinto la suma

suma1(num1, num2)#llamo y ejecuto la función

#funcion con parametros y return

nume1= int( input("ingreso el primer sumando ".upper())) #pido nume 1 y 2, funcion upper para que se vea en mayusculas
nume2= int(input("ingrese el segundo sumando ".upper()))
def suma1(nume1, nume2): #declaro la funcion con los parametros que pedi
    resultado1=nume1+nume2 #resultado1 es la suma de los dos numero
    return resultado1 #retorno resultado1

print( "En la suma de ",nume1, "y " ,nume2, " el resultado es ",suma1(nume1, nume2)) #pinto salida y allí mismo ejecuto la función que retorna resultado1
almacena_resultado=suma1(nume1,nume2) #para comprobar creo variable y ejecuto la funcion con parametros
print(almacena_resultado) #pinto la variable


