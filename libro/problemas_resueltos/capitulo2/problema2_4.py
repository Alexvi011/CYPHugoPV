MAT=int(input("Introduce tu matricula: "))
CAL1=float(input("Introduce tu calificacion 1: "))
CAL2=float(input("Introduce tu calificacion 2: "))
CAL3=float(input("Introduce tu calificacion 3: "))
CAL4=float(input("Introduce tu calificacion 4: "))
CAL5=float(input("Introduce tu calificacion 5: "))
PRO=(CAL1+CAL2+CAL3+CAL4+CAL5)/5
if PRO>=6:
    print(f"Matricula:{MAT}; Promedio:{PRO}; Aprobado ")
else:
    print(f"Matricula:{MAT}; Promedio:{PRO}; Reprobado ")



