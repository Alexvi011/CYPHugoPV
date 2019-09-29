A=float(input("Introduce tu valor A: "))
B=float(input("Introduce tu valor B: "))
C=float(input("Introduce tu valor C: "))
DIS=(B**2)-(4*A*C)
if DIS>0:
    X1=((-B)+ DIS**0.5)/(2*A)
    X2=((-B)-DIS**0.5)/(2*A)
    print(f"Las raices reales son X1:{X1} Y X2:{X2}")
print("Fin del programa")

