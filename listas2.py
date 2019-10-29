#arreglos
#lectura
#escritura/asignacion
#actualizacion: insercion,eliminaion,modificacion
#ordenamiento
#busqueda

#escritura
frutas=["Zapote","Manzana","Pera","Aguacate","Durazno","Uva","Sandia"]

#lectura,el selector indice
print(frutas[2])
print("------------------")
#lectura con for
# for opcion 1
for indice in range (0,7,1):
    print(frutas[indice])
print("------------------")
#for opcion 2 -- por un iterador for each
for fr in frutas:
    print(fr)
print("------------------")
# asignacion
frutas[2]="Melon"
print(frutas)

#insercion al final
frutas.append("Naranja")
print(frutas)
print(len(frutas))
print("-----------------")
frutas.insert(2,"Limon")
print(frutas)
print(len(frutas))
print("-----------------")
frutas.insert(0,"Mamey")
print(frutas)
print("-----------------")
#eliminacion con pop
print(frutas.pop())
print(frutas)
print("-----------------")
print(frutas.pop(1))
print(frutas)
print("-----------------")
frutas.append("Limon")
frutas.append("Limon")
print(frutas)
frutas.remove("Limon")
print(frutas)
print("-----------------")
#dir(list)
#help(list.insert)
#help(list.pop)

#ordenamiento
frutas.sort()
print(frutas)
print("-----------------")
frutas.reverse()
print(frutas)
print("-----------------")

#busqueda
print(f"El Limon esta en la posicion:{frutas.index('Limon')}")
print(f"La Uva esta en la posicion:{frutas.index('Uva')}")
print(f"El Limon esta {frutas.count('Limon')} veces en la lista")
print("-----------------")
#concatenar
print(frutas)
otras_frutas=["Rambutan","Nispero","Liche","Pitahaya"]
frutas.append(otras_frutas)
print(frutas)
frutas.extend(otras_frutas)
print(frutas)
print("-----------------")
#copiar
copia=frutas
copia.append("Naranja")
print(frutas)
print(copia)
print("-----------------")
otra_copia=frutas.copy()
otra_copia.append("Fresa")
otra_copia.append("Fresa")
print(frutas)
print(copia)
