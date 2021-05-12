##Realizar un programa que tenga una clase Persona con las siguientes características.
#        La clase tendrá como atributos el nombre y la edad de una persona.
#        Implementar los métodos necesarios para inicializar los atributos,
#        mostrar los datos e indicar si la persona es mayor de edad o no.

class Persona:
    def __init__(self):
        self.nombre = input("ingrese nombre:")
        self.edad = int(input("ingrese edad: "))

    def mostrar(self):
        print("nombre: ", self.nombre)
        print("edad: ", self.edad)
        self.esMayorEdad(self)

    def esMayorEdad(self):
        if self.edad > 18:
            print("es mayor de edad")
        else: print("no es mayor edad")
