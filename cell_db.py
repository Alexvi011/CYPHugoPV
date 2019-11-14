#cell_db-py
def leer_datos(path):
    file=open(path,'rt')
    lista_final=[]
    dic_cel={}
    datos= file.readlines()
    print(datos)
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    for ren in range(len(datos)):
        datos[ren]=datos[ren].strip().split(',')
    print(datos)
    for ren in range(1,len(datos),1):
        dic_cel={}
        for col in range(len(datos[ren])):
            dic_cel[datos[0][col].strip()]=datos[ren][col]
        lista_final.append(dic_cel)
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    #print(lista_final)
    return lista_final
def salida_formato(celular):
    print(f"Celular marca:{ celular['Marca']}")
    print(f"\t Modelo: {celular['Modelo']}")
    print(f"\t Alm: {celular['Almacenamiento']}")
    print(f"\t Vel: {celular['Velocidad']}")
    print(f"\t Ram: {celular['RAM']}")
    print(f"\t Color: {celular['Color']}")




def main():
    archivo= "Celulares.txt"
    bd=leer_datos(archivo)
    print(f"DB={bd}")
    salida_formato(bd[6])

main()
