from modules.curso import Curso
from modules.departamento import Departamento
from modules.estudiante import Estudiante
from modules.profesor import Profesor
from modules.facultad import Facultad 

# Creo facultad con un depto y dir de depto inicial
facultad = Facultad("Facultad de Ingeniería", "Fisica", "Julieta") 

# Creo un departamento de física con tres profesores
profesor_1 = Profesor("Julieta", 40, 11111111)
profesor_2 = Profesor("Luciano", 34, 22222222)
profesor_3 = Profesor("Ana", 43, 33333333)
profesor_4 = Profesor("Damian", 27, 44444444)
dpto_f = Departamento("Física", profesor_1) #Julieta es la directora

# Creo dos cursos para el departamento de Física
curso_1 = Curso("Óptica", profesor_2)
curso_1.agregar_profesor(profesor_4)
curso_2 = Curso("Cuántica", profesor_3)
dpto_f.agregar_curso(curso_1)
dpto_f.agregar_curso(curso_2)

# Muestro lista de profesores de Óptica
print(curso_1.mostrar_profesorado())

# Elimino el profesor "Damian" y muestro lista
curso_1.eliminar_profesor(profesor_4)
print(curso_1.mostrar_profesorado())

# Muestro listado de cursos 
print(dpto_f.mostrar_cursos())

# Elimino el curso "Cuántica" y muestro lista
print(dpto_f.eliminar_curso(curso_2))
print(dpto_f.mostrar_cursos())

# Creo un departamento de matemática con un profesor
profesor_5 = Profesor ("Lucía", 36, 44444444)
dpto_m = Departamento("Matemática", profesor_5) #Lucía es la directora
curso_3 = Curso("Cálculo", profesor_5)

# Muestro lista de departamentos
facultad.agregar_departamento(dpto_f)
facultad.agregar_departamento(dpto_m)
print(facultad.mostrar_departamentos())


# Creo dos alumnos y los agrego a la facultad
alumno_1 = Estudiante("Yazmin", 20, 44151907)
alumno_2 = Estudiante("Federico", 22, 42111111)
facultad.agregar_estudiante(alumno_1)
facultad.agregar_estudiante(alumno_2)

#Lista de estudiantes
print(facultad.mostrar_estudiantes())

# Agrego ambos estudiantes al curso de Óptica
curso_1.agregar_alumno(alumno_1)
curso_1.agregar_alumno(alumno_2)

#Muestro listado del cuso de Óptica
print(curso_1.mostrar_alumnado())

# Elimino a "Yazmin" del curso y muestro lista
curso_1.eliminar_alumno(alumno_1)
print(curso_1.mostrar_alumnado())

# Agrego a "Federico" al curso "Cálculo" y muestro sus cursos
alumno_2.agregar_curso(curso_3)
print(alumno_2.listado_cursos())
