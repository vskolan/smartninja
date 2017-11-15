from functions import suma_brojeva
from geo_igra import provjeri_pokusaj

def test_sume_brojeva():
    #assert suma_brojeva(2,3) == 5
    return "testiranje sume brojeva je OK"

def test_provjere_pokusaja():
    assert provjeri_pokusaj("Zagreb2", "Hrvatska", {"Hrvatska" : "Zagreb"}) == False
    return "test provjere pokusaja je OK"

###### Glavni dio
print test_sume_brojeva()
print test_provjere_pokusaja()
