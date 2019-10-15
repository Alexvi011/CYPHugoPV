Otra=bool(int(input("Hay mas alumnos(0 NO, 1 Si): ")))
suma=0.0
cont=0
while(Otra==True):
    cal=float(input("Calificacion: "))
    cont+=1
    suma+=cal
    Otra=bool(int(input("Hay mas alumnos(0 NO, 1 Si): ")))
print("Suma: ",suma)
print("Promedio",suma/cont)
print("Fin del programa")

