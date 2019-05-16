class Person(object):
    def __init__(self,name,vorname,geburtsdatum,gewicht):
        self.Name=name
        self.Vorname=vorname
        self.Geburtsdatum=geburtsdatum
        self.Gewicht=gewicht
    
    def Vorstellen(self):
        print("Hallo mein Name lautet "+self.Vorname+" "+self.Name+". Ich wiege "+str(self.Gewicht)+"kg und bin am "+self.Geburtsdatum+" geboren.")

    def Abnehmen(self, abgenommen):
        print("Sie wogen "+str(self.Gewicht)+"kg.")
        self.Gewicht-=abgenommen
        print("Jetzt wiegen Sie nur noch "+str(self.Gewicht)+"kg!")



vincent=Person("Gottschling","Vincent","12.09.1996",70)
vincent.Abnehmen(10)

chi=Person("Kahl","Chi","13.10.1997",55)
chi.Abnehmen(12)



