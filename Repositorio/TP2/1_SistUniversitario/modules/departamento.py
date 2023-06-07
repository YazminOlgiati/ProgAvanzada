from modules.profesor import Profesor

class Departamento:
    
    def __init__(self, departamento, director):
        self.nombre = departamento
        self.cursos = []
        self.profesores = []
        self.profesores.append(director) # Debe haber un profesor por clase
        self.director = director # El profesor que se agrega es director antes de la elección del mismo


    # Controlar que el director elegido sea parte del profesorado    
    def control_director(self, director):
        if director in self.profesores:
            self.director = director
        else:
            raise ValueError("El director asignado no forma parte del profesorado.")
    
    #Agregar curso al departamento
    def agregar_curso(self, curso): 
        self.cursos.append(curso)
            
    #Eliminar curso del departamento        
    def eliminar_curso(self, curso): 
        self.cursos.remove(curso)

    #Mostrar listado de cursos
    def mostrar_cursos(self):
        return self.cursos


    # def agregar_profesor(self, profesor):
    #     if isinstance(profesor, Profesor):      # Controlar que es un objeto de tipo Profesor
    #         self.profesores.append(profesor)
    #     else:
    #         raise TypeError("El profesor que se intenta agregar no es de tipo Profesor.")
    
    # # Controlar que el profesor elegido sea parte del profesorado
    # def eliminar_profesor(self, profesor):
    #     if profesor in self.profesores:
    #         self.profesores.remove(profesor)
    
    # # Devuelve una lista de profesores
    # def mostar_profesores(self): 
    #     return self.profesores

    def __repr__(self):
        return self.nombre