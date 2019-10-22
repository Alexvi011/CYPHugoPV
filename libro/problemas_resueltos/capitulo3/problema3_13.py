ARSU=0
ARNO=0
MERSU=50000
ARCE=0
I=1
while(I<=12):
    RNO=float(input(f"Ingresa la caida de lluvia en region norte en el mes {I}: "))
    RCE=float(input(f"Ingresa la caida de lluvia en region centro en el mes {I}: "))
    RSU=float(input(f"Ingresa la caida de lluvia en region sur en el mes {I}: "))
    ARNO+=RNO
    ARCE+=RCE
    ARSU+=RSU
    if(RSU<MERSU):
        MERSU=RSU
        MES=I
    I+=1    
PRORCE=ARCE/12
print(f"Promedio Region: {PRORCE} \nMes con menor lluvia region sur:{MES}\nRegistro del mes:{MERSU}")
if(ARNO>ARCE):
      if(ARNO>ARSU):
          print("La region con mayor lluvia es la region norte")
      else:
          print("La region con mayor lluvia es la region sur")
else:
    if(ARCE>ARSU):
        print("La region con mayor lluvia es la region centro")
    else:
        print("La region con mayor lluvia es la region sur")
print("Fin del programa")
      
          
      

