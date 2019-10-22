SERIE=0
N=int(input("Introduce un numero entero: "))
I=1
while(I<=N):
    if (-1)**(I)>0:
        SERIE-=1/I
    else:
        SERIE+=1/I
        
    I=I+1
print(f"La suma de la serie es:{SERIE}")



