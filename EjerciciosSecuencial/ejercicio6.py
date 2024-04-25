calificacion_de_las_actividades= 4.0
nota_del_proyecto_final= 3.0
nota_de_las_evaluaciones= 4.0

variable1=str(input("cual es el nombre del estudiante:"))
variable2=float(input("coloca la nota promedio de las actividades realizadas en calse:"))
variable3=float(input("coloca la nota del proyecto final:"))
variable4=float(input("coloca la nota promedio de las evaluciones parciales"))
 
notaFinal= (variable2*4.0)+(variable3*3.0)+(variable4*4.0)

print(f"la nota final del estudiante {variable1} es {notaFinal}")
