# primero definimos las notas del estudiante 
nota1=float(input("ingresa la primera nota: "))
nota2=float(input("ingresa la segunda nota: "))
nota3=float(input("ingresa la tercera nota: "))
# despues debemos hacer una operacion matematica de suma y division para saber el promedio
promedio= (nota1 + nota2 + nota3) /3
# y aca con el uso de mayor o menor sabemos si el estudiante aprueba y sino pues reprueba
if promedio >= 70:
    print("el alumno aprueba algoritmia") 
else:
    print("el alumno desaprueba algoritmia")