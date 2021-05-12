#Desarrollar un programa que cargue los datos de un triángulo.
# Implementar una clase con los métodos para inicializar los atributos,
# imprimir el valor del lado con un tamaño mayor y  el tipo de triángulo que es (equilátero, isósceles o escaleno).

class Triangulo:
    def __init__(self):
        self.lado1 = int(input("ingrese un lado: "))
        self.lado2 = int(input("ingrese un lado: "))
        self.lado3 = int(input("ingrese un lado: "))

        def tipo(self):
            if self.lado1 == self.lado2:
                if self.lado3 == self.lado2:
                    print("es equilátero")
                else:
                   print("es isósceles")
            if self.lado1 != self.lado2 & self.lado2 != self.lado3 & self.lado3 != self.lado1:
                       print("es escáleno")

if __name__ == '__main__':
    t = Triangulo()
    t.tipo(t)

