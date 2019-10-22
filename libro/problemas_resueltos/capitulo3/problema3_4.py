NOM=0
print("Siterminaste de ingresar sueldo ingresa -1")
SUE=float(input("Ingresa tu sueldo: "))
while(SUE!=-1):
    if(SUE<1000):
        NSUE=SUE*1.15
    else:
        NSUE=SUE*1.12
    NOM+=NSUE
    print(NSUE)
    SUE=float(input("Ingresa otro sueldo: "))
print(f"La nomina es de:${NOM}")
    

