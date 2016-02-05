from bs4 import BeautifulSoup
import csv

soup = BeautifulSoup (open("hindu-try.html"))
f = csv.writer(open("try.csv", "w"))
f.writerow(["Name", "Link"])
final_link = soup.p.a
final_link.decompose()

#links = soup.find_all('a')
f.writerow(["Name", "Years", "Position", "Party", "State", "Congress", "Link"])

trs = soup.find_all('tr')

for tr in trs:
    for link in tr.find_all('a'):
    	print(link)
        fullLink = link.get ('href')

    tds = tr.find_all("td")

    try:
        names = str(tds[0].get_text())
        years = str(tds[1].get_text())
        positions = str(tds[2].get_text())
        parties = str(tds[3].get_text())
        states = str(tds[4].get_text())
        congress = tds[5].get_text()

    except:
        print "bad tr string"
        continue

    f.writerow([names, years, positions, parties, states, congress, fullLink])
