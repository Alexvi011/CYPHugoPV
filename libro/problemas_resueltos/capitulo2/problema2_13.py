MAT=int(input("Introduce tu matricula: "))
print("Economia=1,Computacion=2,Administracion=3,Contabilidad=4")
CARR=int(input("Introduce la carrera (1-4): ")) 
SEM=int(input("Introduce tu semestre: "))
PROM=float(input("Introduce tu promedio: "))
if CARR==1:
    if SEM>=6 and PROM>=8.8:
        print(f"Matricula:{MAT},Economia,Aceptado")
if CARR==2:
     if SEM>6 and PROM>=8.5:
        print(f"Matricula:{MAT},Computacion,Aceptado")
if CARR==3:
     if SEM>5 and PROM>=8.5:
        print(f"Matricula:{MAT},Administracion ,Aceptado")
if CARR==4:
     if SEM>5 and PROM>=8.5:
        print(f"Matricula:{MAT},Contabilidad ,Aceptado")




        





