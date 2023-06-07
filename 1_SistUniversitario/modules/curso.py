from modules.estudiante import Estudiante
from modules.profesor import Profesor

class Curso:
   
    def __init__(self, curso, profesor): # Sí o sí se crea un curso con un profesor
        self.profesorado = []
        #self.alumnado = []
        if isinstance(profesor, Profesor): # isinstance controla que el dato sea de tipo Profesor
            self.profesorado.append(profesor)
            self.nombre_curso = curso
        else:
            raise ValueError("El profesor que desea asignar no del tipo Profesor.")
    
    def agregar_profesor(self, profesor): 
        if isinstance(profesor, Profesor):    # Controlar que sea de tipo Profesor antes de agregar
            self.profesorado.append(profesor)
        else:
            raise TypeError("El profesor que se intenta agregar no es parte del profesorado.")

    
    def agregar_alumno(self, alumno): 
        if isinstance(alumno, Estudiante):    # Controlar que sea de tipo Estudiante antes de agregar
            self.alumnado.append(alumno)
            alumno.agregar_curso(self.nombre_curso)
        else:
            raise TypeError("El alumno que se intenta agregar no es parte del alumnado.")      


    def eliminar_alumno(self, alumno):
        if isinstance(alumno, Estudiante):  # Controlar que sea de tipo Estudiante antes de eliminar
            self.alumnado.remove(alumno)
            alumno.eliminar_curso(self.nombre_curso)


    def eliminar_profesor(self, profesor): 
        if isinstance(profesor, Profesor):    # Controlar que sea de tipo Profesor antes de eliminar
            self.profesorado.remove(Profesor(profesor))
                   
    def mostrar_profesorado(self):
        return self.profesorado
    
    def mostrar_alumnado(self): #devuelve una lista de alumnos matriculados
        return self.alumnado
    
    def __repr__(self):
        return self.nombre_curso