from modules.persona import Persona

#Estudiante hereda de Persona
class Estudiante(Persona):
    
    def __init__(self, nombre, edad, dni):
        super().__init__(nombre, edad, dni)
        self.cursos = []
     
    def agregar_curso(self, curso): 
        self.cursos.append(curso)
                  
    def eliminar_curso(self, curso): 
        self.cursos.remove(curso)
            
    #Esto está dudoso !!
    def listado_cursos(self):
        if len(self.cursos)==0:
            print("El alumno no se encuentra matriculado a ningún curso.")
        else:
            return self.cursos

    def __repr__(self):
        return self.nombre
    