CLAVE=int(input("Ingresa la clave de tu zona geografica: "))
NUMIN=int(input("Ingresa los minutos que duro la llamada: "))
COST=0
if CLAVE==12:
    COST=NUMIN*2
    print(f"El costo total de la llamada fue de ${COST}")
if CLAVE==15:
    COST=NUMIN*(2.2)
    print(f"El costo total de la llamada fue de ${COST}")
if CLAVE==18:
    COST=NUMIN*(4.5)
    print(f"El costo total de la llamada fue de ${COST}")
if CLAVE==19:
    COST=NUMIN*3.5
    print(f"El costo total de la llamada fue de ${COST}")
if CLAVE==23 and CLAVE==25:
    COST=NUMIN*6
    print(f"El costo total de la llamada fue de ${COST}")
if CLAVE==29:
    COST=NUMIN*5
    print(f"El costo total de la llamada fue de ${COST}")
print("Fin del programa")

