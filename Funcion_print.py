# print tiene 4 formas de uso
"""
1.- Con comas
2.- Consigno '+'
3.- Con la funcion format()
4.- Es con una variante de format()
"""
# Con comas,concatenar agregando
# Un espacio y haciendo casting de tipo
edad = 10
nombre= "Alex"
estatura = 1.60
print(edad , estatura , nombre)
# con '+' hace lo mismo pero no
# Realiza el casting automático
# no agrega espacio
print( str(edad) + str(estatura) + nombre )

# Funcion format()

print("Nombre: {} Edad: {} ".format(nombre,edad))

# La forma cuatro es con una variante format() simplificada

print(f"Nombre: \"{nombre}\" \nEdad: \t{edad}" )

# caracter de escape \
# \n salto de linea
# \t tabular
# print y el argumento end sirve para evitar el salto de linea 

print("Solo hay diez tipos de personas, las que saben binario y las que no ",end=" ")
print("otra linea")
