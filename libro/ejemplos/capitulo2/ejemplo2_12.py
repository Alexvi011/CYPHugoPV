A=int(input("Introduce un valor entero: "))
B=int(input("Introduce otro valor entero: "))
C=int(input("Introduce otro valor entero: "))
if A>B:
    if A>C:
        if B>C:
            print(f"{A},{B},{C}")
        else:
            print(f"{A},{C},{B}")
    else:
        print(f"{C},{A},{B}")
else:
    if B>C:
        if A>C:
            print(f"{B},{A},{C}")
        else:
            print(f"{B},{C},{A}")
    else:
        print(f"{C},{B},{A}")

print("Fin del programa")


