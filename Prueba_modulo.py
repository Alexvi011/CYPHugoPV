import Modulos

Modulos.mi_print("Hola")
print("-----------------------")
#from modulos import *  (Pone el nombre de todos los paquetes)
from Modulos import mi_print, otro_print, sumar , restar
import time #Pausa el tiempo en el que tarda en ejecutarce
import sys
from asciistuff import Banner
mi_print("Hola de nuevo")
print("-----------------------")
otro_print("Otro print usado")
print("-----------------------")
print(sumar(4,5))
print(restar(10,7))
print("-----------------------")
for i in range (10,0,-1):
    print(i , "...")
    time.sleep(1)
print("BOOOOM PERRRAS!!!!!")
print("BOOM es lo que buscas?")
print(Banner("CORRE PERRA CORRE!!!!"))
print("-----------------------")

#print(dir(sys))
print(sys.platform)
#http://patorjk.com/software/taag/#p=testall&f=Ribbit3&t=Type%20Something%20    genera banners

#Nombre de escuela en dorado, fes en azul y mi nombre en verde instalar pip y buscar color text
