import sys
import pandas as pd
from bs4 import BeautifulSoup

df = pd.read_csv(sys.argv[1], sep=';', skiprows=[0, 1, 3])

soup = BeautifulSoup(features='xml')
root = soup.new_tag('populationdata')

for index, row in df.iterrows():
    municipality = soup.new_tag('municipality')
    name = soup.new_tag('name')
    name.string = row['Tilastovuoden kunta']
    municipality.append(name)
    year = soup.new_tag('year')
    year.string = str(row['Vuosi'])
    municipality.append(year)
    total = soup.new_tag('total')
    total.string = str(row['Sukupuolet yhteensä Ikäluokat yhteensä'])
    municipality.append(total)
    males = soup.new_tag('males')
    males.string = str(row['Miehet Ikäluokat yhteensä'])
    municipality.append(males)
    females = soup.new_tag('females')
    females.string = str(row['Naiset Ikäluokat yhteensä'])
    municipality.append(females)
    root.append(municipality)

soup.append(root)

outputFile = open(sys.argv[2], 'w')
outputFile.write(soup.prettify())
outputFile.close()
