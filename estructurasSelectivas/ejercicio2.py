# definimos cuantas zapatillas va a comprar el cliente
cantidad_zapatillas=int(input("ingrese la cantidad de zapatillas: "))
# colocamos el valor que tienen las zapatillas 
precio_zapatilla=float(input("ingrese el precio de la zapatilla: "))
# en esta linea hacemos la operacion para saber el total de la compra
total_sin_descuento=cantidad_zapatillas*precio_zapatilla
# aca decimos que si el cliente compra mas de tres zapatillas tendra mayor descuento
if cantidad_zapatillas >=3:
    descuento=total_sin_descuento*0.20
# aca decimos que sino lleva mas de tres zapatillas obtendra menos descuento
else:
    descuento=total_sin_descuento*0.10
    total_a_pagar=total_sin_descuento-descuento
# y por ultimo imprimimos para saber el resultado de los datos digitados
print("total a pagar es:",total_a_pagar)