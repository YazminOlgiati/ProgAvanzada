from modules.persona import Persona

# Profesor hereda de Persona
class Profesor(Persona):
    
    # super() permite invocar y conservar un método o atributo de una clase padre 
    # desde una clase hija sin tener que nombrarla explícitamente.
    def __init__(self, nombre, edad, dni):
        super().__init__(nombre, edad, dni) 
        self.cursos = []
       
    def __repr__(self): # __repr__() devuelve una cadena como representación del objeto
        return self.nombre
