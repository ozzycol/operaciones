import os
class rectangulo:
    def __init__(self, ancho, alto):
        self.ancho=ancho
        self.alto=alto
    def area(self):
        area=self.ancho*self.alto
        return area

    def perimetro(self):
        perimetro=(self.ancho*2)+(self.alto*2)
        return perimetro
os.system("cls")
lado=float(input("Ingrese el valor del lado: "))
largo=float(input("Ingrese el valor del largo: "))

r1=rectangulo(lado, largo)
area=r1.area()
perimetro=r1.perimetro()
print("El area es: ", area)
print("El perimetro es: ", perimetro)

    
