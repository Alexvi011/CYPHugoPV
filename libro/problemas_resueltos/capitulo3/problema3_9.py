N=int(input("Ingrese un numero entero positivo: "))
I=1
SERIE=0
while(I<=N):
    SERIE+=(I)**(I)
    print(SERIE)
    I+=1
print(f"La suma de la serie es:{SERIE}")
