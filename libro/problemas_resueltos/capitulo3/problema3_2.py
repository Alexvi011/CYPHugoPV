BAND=str("T")
SUMSER=0
I=2
while (I<=1800):
    SUMSER+=1
    print(I)
    if BAND==str("T"):
        BAND=str("F")
        I+=3
    else:
        BAND=str("T")
        I+=2
print(f"La suma de los terminos es:{SUMSER}")


