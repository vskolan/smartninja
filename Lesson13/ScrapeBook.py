from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

csv_file = open("email_list.csv", "w")

url = "http://scrapebook22.appspot.com/"

odgovor = urlopen(url).read()

soup = BeautifulSoup(odgovor)

for link in soup.findAll("a"):
    if link.string == "See full profile":
        osobin_url = "http://scrapebook22.appspot.com" + link["href"]
        osobina_stranica = urlopen(osobin_url).read()
        osobin_soup = BeautifulSoup(osobina_stranica)
        email = osobin_soup.find("span", attrs={"class" : "email"}).string
        #imena = osobin_soup.html.body.findAll("div", attrs={"class": "col-md-8"})
        #print imena[0].h1.string
        spanovi = osobin_soup.findAll("span")
        grad = ""
        for span in spanovi:
            if span.has_key("data-city"):
                grad = span.string

        ime_html = osobin_soup.html.body.find("div", attrs={"class": "col-md-8"})
        ime = ime_html.h1.string
        print "------------------------------------------------"

        csv_file.write(ime + "," + grad + "," + email + "\n")
        #print osobin_soup.find("span", attrs={"class" : "email"}).string

csv_file.close()
#print soup.html.head.title.string