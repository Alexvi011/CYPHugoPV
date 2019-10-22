MAY=(-100000)
MEN=100000
N=int(input("Ingresa un numero entero: "))
I=1
while(I<=N):
    NUM=int(input("Ingresa otro numero entero: "))
    if(NUM>MAY):
        MAY=NUM
    if(NUM<MEN):
        MEN=NUM
    I+=1
print(f"El numero mayor es:{MAY}\nEl numero menor es:{MEN}")

