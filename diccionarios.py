#diccionarios {'llave':'valor'}

alumno={'num_cta':'317031522',
        'Nombre':('Alejandro','Perez','Vite'),
        'Semestre':1,
        'Promedio':0.0,
        'Materias':['CyP','Algebra','Calculo','Geometria','IntroICO'],
        'Regular':True,
        'lagrimas_por_examen':5,
        'Direccion':{
            'calle':'Rancho Sequito',
            'Colonia':'Impulsora Popular Avicola',
            'numero':'1000',
            'CP':'17570',
            'del_mun':'Nezahualcoyotl',
            'estado':{
                'ID':15,
                'nombre':'Estado de México',
                'corto':'EDOMEX',
                

                     }

                    }
        }
print(alumno['Materias'][1].upper())
print("------------------------------------------------------------------------")
alumno['lagrimas_por_examen']=10
print(alumno)
print("------------------------------------------------------------------------")
print(alumno['Direccion']['estado']['nombre'][10:].upper())
print("------------------------------------------------------------------------")
print(alumno['Nombre'])
print("------------------------------------------------------------------------")
print(alumno)
print("------------------------------------------------------------------------")
print(alumno['Nombre'][1])
print("------------------------------------------------------------------------")
print(alumno['Direccion']['CP'])
print("------------------------------------------------------------------------")
print(alumno['Direccion']['estado']['corto'])
print("------------------------------------------------------------------------")
print(alumno['Materias'][3::])
print("------------------------------------------------------------------------")
mi_lista=[['a','b'],['c',10],['d',True]]
diccionario=dict(mi_lista)
print(diccionario)
print("------------------------------------------------------------------------")

#Son mutables
alumno['cursa_ingles']=True
print(alumno)
print("------------------------------------------------------------------------")

#funcion keys()
llaves=alumno.keys()
print(llaves)
print("------------------------------------------------------------------------")
for llave in llaves:
    print("------------")
    print(llave)
    print("..............")
    print(alumno[llave])
    print("+++++++++++++++")
print("------------------------------------------------------------------------")

#funcion values
for val in alumno.values():
    print('..............')
    print(val)
    print('++++++++++++++')
print("------------------------------------------------------------------------")

#funcion items()
for elem in alumno.items():
    print('..............')
    print(elem)
    print('++++++++++++++')








    
