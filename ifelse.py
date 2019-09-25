edad= int(input("Dame tu edad:"))
INE = bool(int(input("Tienes INE (0 NO / 1 SI):")))
if edad>=18 and INE==True:
    print("Eres mayor de edad")
    print("Puedes entrar al bar")
    print("Fin del programa")
else:
    print("Eres menor de edad o no tienes tu INE")
    print("Puedes ir a jugar Fortnite rata")
    print("Fin del programa")

