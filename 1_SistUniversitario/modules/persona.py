#clase base abstracta
from abc import ABC, abstractmethod

#Persona desciende de ABC
class Persona(ABC):
    
    @abstractmethod
    def nombre(self):
        pass

    @abstractmethod
    def edad(self):
        pass

    @abstractmethod
    def dni(self):
        pass

    # def __init__(self, nombre, edad, dni):
    #     self.nombre_apellido = nombre
    #     self.edad = edad
    #     self.dni = dni
           
    # @abstractmethod
    # def nombre(self):
    #     return self.nombre_apellido 
    #     #pass
    
    # @abstractmethod
    # def nombre(self, nuevo_nombre):
    #     self.nombre_apellido = nuevo_nombre
    #     #pass