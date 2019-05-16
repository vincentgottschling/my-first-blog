class Tier(object):
    def __init__(self,name):
        self.name=name

class Pferd(Tier):
    def __init__(self,geschlecht,name):
        self._geschlecht=geschlecht
        self.hunger=True
        Tier.__init__(self,name)
    def fressen(self):
        return("satt")

    def traben(self):
        return("trabe")

lotte=Pferd("w","Lotte")
#jana=Pferd("Jana","w")
print(lotte._geschlecht)

