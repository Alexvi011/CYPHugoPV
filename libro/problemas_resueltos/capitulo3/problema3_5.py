SUMOTR=0
SUMPOS=0
CUEPOS=0
N=int(input("Ingresa un numero: "))
I=1
while(I<=N):
    NUM=int(input("Ingresa un numero entero: "))
    if (NUM>0):
        SUMPOS+=NUM
        CUEPOS+=1
    else:
        SUMOTR+=NUM
    I=I+1
PROGEN=(SUMPOS+SUMOTR)/N
PROPOS=(SUMPOS/CUEPOS)
print(f"Los numeros positivos fueron:{CUEPOS}\nEl promedio de numeros positivos fue:{PROPOS}\nEl promedio general de los numeros fue:{PROGEN}")
