#calcula el area y perimetro de un rectangulo usando un clase
import os #importo clase del sistema
class rectangulo: #creo la clase
    def __init__(self, ancho, alto): #creo metodo inicial
        self.ancho=ancho
        self.alto=alto
    def area(self): #creo el método area
        area=self.ancho*self.alto
        return area

    def perimetro(self): #creo metodo perimetro
        perimetro=(self.ancho*2)+(self.alto*2)
        return perimetro
os.system("cls")
lado=float(input("Ingrese el valor del lado: "))
largo=float(input("Ingrese el valor del largo: "))

r1=rectangulo(lado, largo) #llamo a la clase
area=r1.area() #asigno el valor que calcula el metodo a variables
perimetro=r1.perimetro()
print("El area es: ", area)
print("El perimetro es: ", perimetro)

    
