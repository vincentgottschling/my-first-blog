def Rechteck(a,b):
    fläche=a*b
    return fläche

print(Rechteck(10,10))


def Fakultaet(zahl):
    result=1
    if zahl>1:
        result=zahl*Fakultaet(zahl-1)
    return result

print(Fakultaet(4))
