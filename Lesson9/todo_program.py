print "Dobro dosli u program za upravljanje zadacima!"


popis_zadataka = {}

while True:
    zadatak = raw_input("Molimo upisite zadatak: ")
    status = raw_input('Da li je zadatak napravljen? (da/ne)')
    print "Tvoj zadatak je: " + zadatak
    #### Kljucni dio
    #vrijedi za liste
    #lista_zadataka.append(zadatak)

    #vrijedi za rjecnik
    if status == "da":
        popis_zadataka[zadatak] = "da"
    else:
        popis_zadataka[zadatak] = "ne"

    novi_zadatak = raw_input("Zelis li upisati novi zadatak? (da/ne)")

    if novi_zadatak == "ne":
        break

#print "Svi navedeni zadaci: %s" % popis_zadataka

#datoteka_zadataka = open("popis_zadatak.txt", "w+")
with open("popis_zadatak.txt", "w+") as datoteka_zadataka:

    datoteka_zadataka.write("Svi napravljeni zadaci:\n")
    print "Svi napravljeni zadaci:"
    for podatak in popis_zadataka:
        if popis_zadataka[podatak] == "da" :
            print "+ " + podatak
            datoteka_zadataka.write("+ " + podatak + "\n")

    datoteka_zadataka.write("\n")

    print "Svi NEnapravljeni zadaci:"
    datoteka_zadataka.write("Svi NEnapravljeni zadaci:\n")
    for podatak in popis_zadataka:
        if popis_zadataka[podatak] == "ne":
            print "- " + podatak
            #pisanje u datoteku
            datoteka_zadataka.write("- " + podatak + "\n")
    #for podatak in lista_zadataka:
    #    print podatak

#datoteka_zadataka.close()
print "Kraj programa!"