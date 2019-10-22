NUM=int(input("Ingresa un numero entero: "))
while(NUM!=1):
    if NUM%2==0:
        NUM/=2
    else:
        NUM=(NUM*3)+1
    print(NUM)
