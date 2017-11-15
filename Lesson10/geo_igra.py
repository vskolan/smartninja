from random import randint
import random
def main():
    print "-------------------------------------------"
    print "Dobrodosli u igru pogadanja glavnog grada"
    popis_drzava = {"Hrvatska" : "Zagreb", "Italija" : "Rim", "Albanija" : "Tirana"}

    while True:
        nasumicni_broj = randint(0, 2)
        odabrana_drzava = popis_drzava.keys()[nasumicni_broj]

        pokusaj = raw_input("Koji je glavni grad od " + odabrana_drzava + "?: ")

        provjeri_pokusaj(pokusaj, odabrana_drzava, popis_drzava)

        ponovni_pokusaj = raw_input("Zelite li opet probati? (yes/no) ")
        if ponovni_pokusaj == "no":
            break

    print "KRAJ"
    print "____________________"


def provjeri_pokusaj(korisnikov_pokusaj, drzava, kopija_popis_drzava):
    glavni_grad = kopija_popis_drzava[drzava]

    if korisnikov_pokusaj == glavni_grad:
        print "Tocan odgovor!"
        return True
    else:
        print "Netocan odgovor!"
        return False

if __name__ == "__main__":
    main()