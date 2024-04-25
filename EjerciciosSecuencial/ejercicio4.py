sueldo= 5000000
Tcomisiones= 0
comisiones= 500
ventas= 0

vendedor= str(input("como se llama el vendedor:"))
ventas= int(input("cuantas ventas se realizaron:"))

Tcomisiones= ventas*comisiones
total= sueldo+Tcomisiones

print(f"el vendedor {vendedor} tiene un sueldo de {sueldo} y durante el mes obtuvo una comision de {Tcomisiones}")
