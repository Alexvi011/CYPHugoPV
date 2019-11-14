nombre= "Alex Vite"
print (nombre)
print (nombre[0])
print (nombre[8])

print (nombre[-1])
print(nombre[-4])
#slicing
print (nombre[0:5:1])
#valores por defecto de slicing
print (nombre[5::1])
print(nombre[::])
print(nombre[:4:])
#slicing negativo
print(nombre[-1:-5:-1])
print(nombre[::-1])
print(nombre[-6:-10:-1])

frase="Solo existen 10 tipos de personas, las que saben binario y las que no"
#Hacer un slicing para imprmir la palabra existen
print(frase[5:13:1])
#Hacer otro para imprimir la palabra personas en orden inverso
print(frase[32:24:-1])
#Hacer slicing que imprima toda la frase en orden inverso
print(frase[::-1])

print(dir(nombre))
print("Funciones de string(str)")
print(nombre.upper())
print(f"La palabra 'existen' esta en la pos. {frase.find('existen')}")
