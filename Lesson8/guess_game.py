tajni = 35
pokusaj = 0

# range(n) = 0.1,2,3,....., n-1
# for <var> in <lista, range, dict, ...>
while True:
    #print "Pokusaj broj: " +str(i+1)
    pokusaj = int(raw_input("Upisite trazeni broj: (1-50)"))

    if pokusaj == tajni:
        print "Pogodak!!!"
        break
    elif pokusaj > tajni:
        print "Probaj s manjim brojem"
    elif pokusaj < tajni:
        print "Probaj s vecim brojem"
    #else:
     #   print "Promasaj!"

print "Kraj programa!"