SUE=float(input("Introduce tu salario: "))
if SUE<1000:
    NSUE=SUE*1.15
    print(f"Tu nuevo salario es: {NSUE}" )
else:
    NSUE=SUE*1.12
    print(f"Tu nuevo salario es: {NSUE}")
print("Fin del programa")
