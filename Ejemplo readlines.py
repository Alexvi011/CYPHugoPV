archivo= open("numeros.txt","rt")
numeros2=archivo.readlines()
print(numeros2)
print("-----------------------------")
numeros2=[line.rstrip() for line in open('numeros.txt')]
print(numeros2)
print("-----------------------------")
lista_num=[]
for linea in numeros2:
    for numero in linea.split(','):
        lista_num.append(int(numero))
lista_num.sort()
print(f"\n Lista ordenada :{lista_num}\n")
print("-----------------------------")
print(f"El mayor es :{lista_num[-1]} y el menor es: {lista_num[0]}")
archivo.close

