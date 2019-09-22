L1= float(input("Ingresa el valor del primer lado: "))
L2= float(input("Ingresa el valor del segundo lado: "))
L3= float(input("Ingresa el valor del tercer lado: "))
S=(L1+L2+L3)/2
AREA=(S*(S-L1)*(S-L2)*(S-L3))**0.5
print(f"El valor del area es: {AREA} u cuadradas")
