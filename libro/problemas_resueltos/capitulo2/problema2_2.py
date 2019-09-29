P=int(input("Introduce tu valor P: "))
Q=int(input("Introduce tu valor Q: "))
EXP= (P**3)+(Q**4)-(2*P**2)
if EXP<680:
    print(f"Los valores P:{P}, y Q:{Q} satisfacen la expresion")
else:
    print(f"Los valores P:{P}, y Q:{Q} no satisfacen la expresion")
print("Fin del programa")
