#Una funcion es una unidad de codigo reutilizable, ademas de ser un mecanismo de organizar codigo
#Una funcion puede tomar de entrada cualquier cantidad de parametros(de cualquier tipo) de entrada y retorna un solo valor,de cualquier tipo de dato
#Puedes hacer dos cosas con una funcion 1.-Definirla, 2.-Llamarla

def sumar(x,y):
    z=x+y
    return z
def restar(x,y):
    return x-y

def mi_print(texto):
    print(f"Este es mi print: {texto}")

def multiplica(valor,veces):
    if veces==None:
        print("Debes enviar el segundo argumento de la funcion ")
    else:
        print(valor*veces)

def comanda(mesa,comensal,entrada,medio,fuerte,postre):
    print(f"Mesa: {mesa} comensal: {comensal}")
    print(f"\t Entrada: {entrada}")
    print(f"\t Segundo tiempo: {medio}")
    print(f"\t Plato fuerte: {fuerte}")
    print(f"\t Postre: {postre}")

    
def main():
    a=10
    b=5
    c=sumar(a,b)
    print(f"La suma de {a} y {b} es: {c}")
    c=restar(a,b)
    print(f"La resta de {a} y {b} es: {c}")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")


if __name__=='__main__': #¿Se mando a ejecutar(interpretar) este archivo?
    main()

mi_print("Hola puto")
multiplica(10, 3)
multiplica(10 , None)
multiplica('Hola ',3)
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")

comanda(2,1 ,"Ensalada","Sopa de rana","Filete de pompi de sirena","Flan")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")

comanda("Ensalada","Sopa de rana","Filete de pompi de sirena","Flan",2,1)
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")

comanda(entrada="Ensalada",medio="Sopa de rana",fuerte="Filete de pompi de sirena",postre="Flan",mesa=2,comensal=1)
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")

def comanda(mesa,comensal,entrada,medio,fuerte,postre="Gela de Limon"):
    print(f"Mesa: {mesa} comensal: {comensal}")
    print(f"\t Entrada: {entrada}")
    print(f"\t Segundo tiempo: {medio}")
    print(f"\t Plato fuerte: {fuerte}")
    print(f"\t Postre: {postre}")

comanda(entrada="Ensalada",medio="Sopa de rana",fuerte="Filete de pompi de sirena",mesa=2,comensal=1)
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")

def imprime_argumentos(*argumentos):
    for ele in argumentos:
        print(ele)
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    
    for index in range(len(argumentos)):
        print(argumentos[index])
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")

    print('------->',argumentos,'<-------')
    
imprime_argumentos('Hola',True,3.1416,1000,{'id':'Alexvi011','Nombre':'Alejandro'})
def comanda2(**comida):
    llaves=comida.keys()
    for elem in llaves:
        print(elem,"->",comida[elem])

    print(llaves)
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    
    print(comida)
comanda2(entrada="ensalada",medio="sopa de rana",fuerte="filete",mesa=2,comensal=1,postre="pastel")








