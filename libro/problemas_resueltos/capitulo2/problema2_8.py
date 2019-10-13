COMPRA=float(input("Introduce el valor de la compra: "))
PAGAR=0
if COMPRA<500:
    PAGAR=COMPRA
elif COMPRA<=1000:
    PAGAR=COMPRA-(COMPRA*0.5)
elif COMPRA<=7000:
    PAGAR=COMPRA-(COMPRA*0.11)
elif COMPRA<=15000:
    PAGAR=COMPRA-(COMPRA*0.18)
else:
    PAGAR=COMPRA-(COMPRA*0.25)
print(f"El total a pagar es: ${PAGAR} ")
print("Fin del programa")

    

    




