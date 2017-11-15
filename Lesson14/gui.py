import Tkinter
import random
import tkMessageBox
## Fukncionalnost pri kliku na gumb
def pogodi_pokusaj():
    if int(pokusaj.get()) == tajni_broj:
        prikazni_tekst = "TOCNO!"
    elif int(pokusaj.get()) > tajni_broj:
        prikazni_tekst = "KRIVO! Pokusaj s manjim!"
    else:
        prikazni_tekst = "KRIVO! Pokusaj s vecim!"

    tkMessageBox.showinfo("Rezultat", prikazni_tekst)

def ocisti():
    tkMessageBox.showinfo("Ocistio", "Tekst ociscen!")

tajni_broj = random.randint(1,100)
#Inicijaliziramo prozor
prozor = Tkinter.Tk()

gumbovi = Tkinter.Frame(prozor)

## Definiramo labelu
poruka = Tkinter.Label(prozor, text= "Igra pogadanja broja")
poruka.pack()

pozdrav = Tkinter.Label(prozor, text="Pogodi tajni broj")
pozdrav.pack()

#Definiramo polje za unos
pokusaj = Tkinter.Entry(prozor)
pokusaj.pack()

#definiramo gumb
gumb = Tkinter.Button(gumbovi, text="Pokusaj", command=pogodi_pokusaj)
novi_gumb = Tkinter.Button(gumbovi, text="Ocisti", command=ocisti)
gumb.pack(side=Tkinter.LEFT)
novi_gumb.pack(side=Tkinter.LEFT)

gumbovi.pack()
# Pokrecemo prozor
prozor.mainloop()