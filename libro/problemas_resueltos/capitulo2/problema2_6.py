A=int(input("Introduce un numero y te dire si es par o impar: "))
if A==0:
    print("Nulo")
elif ((-1)**A)>0:
    print("Par")
else:
    print("Impar")
print("Fin del programa")
