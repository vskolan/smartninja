#####
# Deklariramo funkciju
####
def suma_brojeva(br1, br2):
    print "br1 " + str(br1)
    print "br2 " + str(br2)
    c = br1 + br2
    #print "Suma je:" + str(c)
    return c

#####
# Glavni program
#####
def main():
    var1 = 3
    var2 = 5

    suma = suma_brojeva(var1,var2)
    nova_suma = suma + 5;

    print nova_suma

    print suma_brojeva(4,5)
    print suma_brojeva(5,6)

######
# Kljucni dio
#####
if __name__ == "__main__":
    main()
