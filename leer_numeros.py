archivo= open("numeros.txt","rt")
#print(dir(archivo))

numeros1=archivo.read()
print(numeros1)
print("-------------------------")

print(numeros1.split('\n'))
print("-------------------------")

lista_num=[]
for linea in numeros1.split('\n'):
    for numero in linea.split(','):
        lista_num.append(int(numero))
print(lista_num)
lista_num.sort()
print("-------------------------")
print(f"\n Lista ordenada :{lista_num}\n")
print(f"El mayor es :{lista_num[-1]} y el menor es: {lista_num[0]}")
archivo.close
print("-------------------------")

archivo=open("numeros.txt","rt")
numeros2=archivo.readlines()
print(numeros2)
archivo.close()
print("-------------------------")
#Decir cual es el mayor y cual es el menor con la lista de arriba

archivo=open("numeros.txt","rt")
numeros2=archivo.readline()
print(numeros2)
archivo.close()
