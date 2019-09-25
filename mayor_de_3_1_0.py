A=int(input("Dame tu primer numero:"))
B=int(input("Dame tu segundo numero:"))
C=int(input("Dame tu tercer numero:"))
if A!=B and A!=B and B!=C:
    if A>B and A>C:
        print(A,"es el mayor")
    elif B>A and B>C:
        print(B,"es el mayor")
    if C>A and C>B:
        print(C,"es el mayor") 
