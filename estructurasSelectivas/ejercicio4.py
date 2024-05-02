# le pedimos a la persona que digite un color para ver si obtendra un descuento 
color=str(input("coloca un color: "))
# pedimos el valor total de la compra al cliente 
compra=int(input("coloca el valor de compra: "))
# aca decimos que si la persona digito el color rojo tendra un descuento del 15% en su compra
if color== "rojo":
    descuento=compra*0.15
    valorPagar=compra-descuento
# y aca imprimimos el resultado del valor a pagar con el descuento explicandole al cliente
    print(f"el valor de la compra es:{compra} y usted escogio el color: {color}, obtendra descuento de: {descuento}, por lo tanto el valor a pagar seria: {valorPagar}")
# aca al igual que la linea pasada decimos que si el color que digito fue verde tendra un descunto de 20% en su compra 
elif color== "verde":
    descuento=compra*0.20
    valorPagar=compra-descuento 
# volvemos a imprimir explicandole al cliente su descuento y el total a pagar 
    print(f"el valor de la compra es: {compra} y usted escogio el color: {color}, obtendra descuento de {descuento},por lo tanto el valor a pagar es {valorPagar}")
# y aca decimos que si el cliente no digita alguno de los dos colores queda sin un descuento en su compra 
else:
    print("no tienes descuento,lo sentimos")