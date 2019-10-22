MED=0
CHI=0
GRA=0
N=int(input("Ingresa el numero de ventas: "))
I=1
while(I<=N):
    V=float(input("Ingresa el valor de la venta: "))
    if(V<=200):
        CHI+=1
    elif(V<400):
        MED+=1
    else:
        GRA+=1
    I+=1
print(f"El numero de ventas grandes fue:{GRA} \nEl numero de ventas medianas fue:{MED}\nEl numero de ventas chicas fue:{CHI}")
