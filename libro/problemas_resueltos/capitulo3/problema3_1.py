I=1
NUM=0
SUMPAR=0
SUMIMP=0
CUEPAR=0
while(I<=270):
    NUM+=1
    if(((-1)**NUM)>0):
            SUMPAR+=NUM
            CUEPAR+=1
    else:
            SUMIMP+=NUM
    I+=1
print(NUM)
PROBAR=SUMPAR/CUEPAR
print(f"El promedio de los numeros pares es de:{PROBAR} \nLa suma de todos los impares es de:{SUMIMP}")
