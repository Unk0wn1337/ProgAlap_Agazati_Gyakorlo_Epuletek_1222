# név$város$ország$magasság(m)$emelet$épült
# Avaz Twist$Szarajevó$Bosznia-Hercegovina$272$40$200s7
class Epulet:
    def __init__(self,sor:str):
        adatok = sor.strip().split("$")
        self.nev = adatok[0]
        self.varos = adatok[1]
        self.orszag = adatok[2]
        self.magassag = float(adatok[3])
        self.emelet = int(adatok[4])
        self.epult = int(adatok[5])

    def __str__(self):
        return f"nev: {self.nev} varos: {self.varos} orszag: {self.orszag} magassag: {self.magassag} emelet: {self.emelet} epulet: {self.epult}"