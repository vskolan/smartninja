class Otac(object):
    def __init__(self, ime, prezime):
        self.ime= ime
        self.prezime = prezime

    def predstavi_se(self):
        print "Moje ime je " + self.ime + " " +self.prezime


class Sin(Otac):
    def __init__(self, ime, prezime, igracka):
        Otac.__init__(self, ime, prezime)
        self.igracka = igracka


class Cestovno_Vozilo(object):
    def vozi(self):
        print "Vozim"

class Auto(Cestovno_Vozilo):
    def vozi_rikverc(self):
        print "Vozim rikverc"


def cestovno_vozilo_vozi():
    print "vozi"

cestovno_vozilo_vozi()

honda = Auto()
honda.vozi()
honda.vozi_rikverc()

marko = Sin(ime="MArko",prezime="Markic", igracka="autic")
marko.predstavi_se()
print marko.igracka

Marin = Otac(ime="Marin", prezime="Markic")
print Marin.predstavi_se()