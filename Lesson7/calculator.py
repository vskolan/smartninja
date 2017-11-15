x = int(raw_input("Upisi vrijednost za x: "))
#x = int(x_tekst)
print "Vrijednost za X je:"
print x

operacija = raw_input("Odaberite operaciju: +,-,*,/ :")
print "operacija je:"
print operacija

y_tekst = raw_input("Upisi vrijednost za y: ")
y = int(y_tekst)
print "Vrijednost za y je: "
print y

if operacija == "+":
    print "Suma je: " + str(x+y)
elif operacija == "-":
    print "Razlika je: "
    print x-y
elif operacija == "*":
    print "Umnozak je: "
    print x*y
elif operacija == "/":
    print "kvocjent je: "
    print x/y
else:
    print "Niste odabrali valjanu operaciju!!!! :("