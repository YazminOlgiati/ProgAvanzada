from modules.estudiante import Estudiante
from modules.departamento import Departamento

class Facultad:
    
    def __init__(self, nombre, departamento_1, profesor_1): # departamento y profesor iniciales
        self.nombre = nombre # Nombre de la facultad
        self.departamentos = []
        #self.alumnos = []
        depto = Departamento(departamento_1, profesor_1) # depto lo convierte en profesor
        self.departamentos.append(depto.nombre)

    def agregar_estudiante(self, alumno):
        if alumno not in self.alumnos:      # Controlar que no se haya ingresado ese alumno antes
            if isinstance(alumno, Estudiante):  # Controlar que el alumno sea de tipo Estudiante antes de agregar
                self.alumnos.append(alumno)
            else:
                raise TypeError("El alumno que se intenta agregar no es de tipo Estudiante.")
        else:
            raise TypeError("Ya se encuentra en la lista de alumnos.")

    # Controlar que el estudiante elegido sea parte del alumnado antes de eliminar
    def eliminar_estudiante(self, alumno):
        if alumno in self.alumnos:
            self.alumnos.remove(alumno)

    def mostrar_estudiantes(self):
        return self.alumnos
    
    def agregar_departamento(self, departamento):
        if isinstance(departamento, Departamento):      #Controlar que el departamento sea de tipo Departamento
            self.departamentos.append(departamento)
        else:
            raise TypeError("El departamento que se intenta agregar no es de tipo Departamento.")
        
    def mostrar_departamentos(self):
        return self.departamentos