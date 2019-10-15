NOMINA=0
for i in range(1,11,1):
    SUE=float(input(f"Ingresa tu sueldo trabajador {i}: "))
    NOMINA+=SUE #NOMINA=NOMINA+SUE#
print(f"La nomina de la empresa es:${NOMINA}")        
