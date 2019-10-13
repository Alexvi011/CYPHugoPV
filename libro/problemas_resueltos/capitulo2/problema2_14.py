TIPOENF=int(input("Introduce tu tipo de enfermedad: "))
EDAD=int(input("Introduce tu edad: "))
DIAS=int(input("Introduce los dias que estuviste internado: "))
if TIPOENF==1:
    COSTOT=DIAS*25
elif TIPOENF==2:
    COSTOT=DIAS*16
elif TIPOENF==3:
    COSTOT=DIAS*20
elif TIPOENF==4:
    COSTOT=DIAS*32
else:
    print("Opcion valida")
if EDAD>=14 and EDAD<=22:
    COSTOT=COSTOT*1.10
print(f"El costo total es de:${COSTOT}")
print("Fin del programa")


