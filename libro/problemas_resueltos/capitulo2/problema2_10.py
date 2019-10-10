A= int(input("Introduce tu primer numero: "))
B= int(input("Introduce tu segundo numero:"))
C= int(input("Introduce tu tercer numero: "))
if A>B:
    if A>C:
        print(f"A es el mayor ")
    elif A==C:
        pritn(f"A y C son los mayores")
    else:
        print(f"C es el mayor")
elif A==B:
    if A>C:
        print(f"A y B son los mayores")
    elif A==C:
        print("A,B y C son los mayores")
    else:
        print(f"C es el mayor")
elif B>C:
    print(f"B es el mayor")
elif B==C:
    print(f"B y C son los mayores")
else:
    print("C es el mayor")
print("Fin del programa")

            
