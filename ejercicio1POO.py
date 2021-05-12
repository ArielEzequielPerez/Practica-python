#Realizar un programa que conste de una clase llamada Alumno
# que tenga como atributos el nombre y la nota del alumno.
# Definir los métodos para inicializar sus atributos, imprimirlos y
# mostrar un mensaje con el resultado de la nota y si ha aprobado o no.´

class Alumno:
    #inicio atributos
    def __init__(self):
        self.nombre = input("Ingrese el nombre: ")
        self.nota = int(input("Ingrese la nota: "))

    def mostrar(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)