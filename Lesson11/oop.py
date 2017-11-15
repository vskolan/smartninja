class Osoba(object):
    def __init__(self, lokalno_ime, prezime, broj, rodendan, email):
        self.ime = lokalno_ime
        self.prezime = prezime
        self.broj = broj
        self.rodendan = rodendan
        self.email = email

    def predstavi_se(self):
        return "Moje ime je " + self.ime + " " + self.prezime

##### glavni program

#Objekt pero
pero = Osoba(lokalno_ime="Pero", prezime="Peric", broj="0987654321", rodendan="1.1.1970", email="pero@mail.com")
mare = Osoba(lokalno_ime="Mare", prezime="Maric", broj="0978654321", rodendan="2.1.1970", email="mare@mail.com")
joza = Osoba(lokalno_ime="Josip", prezime="Josic", broj="0958654321", rodendan="2.2.1971", email="joza@mail.com")

pero.ime = "PEtar"

#print pero.ime
#print mare.prezime
#print joza.rodendan

popis_zaposlenika = [pero, mare, joza]
for zaposlenik in popis_zaposlenika:
    print zaposlenik.predstavi_se()

