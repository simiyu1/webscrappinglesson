from urllib.request import  urlopen
from bs4 import BeautifulSoup

import csv
def get_country(country_code):
    html = urlopen('http://api.worldbank.org/v2/country/{}'
                   .format(country_code))
    soup = BeautifulSoup(html, 'xml')

    country_name = soup.find('wb:name')
    region = soup.find('wb:region')
    income_level = soup.find('wb:incomeLevel')

    print(country_name.get_text())
    print(region.get_text())
    print(income_level.get_text())

if __name__ == '__main__':

    # Create
    with open('country_iso_codes.csv', 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
    file = open('country_iso_codes.csv', 'r+')
    with file:
        writer = csv.writer(file)
        writer.writerows([['ETH','KEN']])
        file.close()

    file = open('country_iso_codes.csv', 'r')
    iso_codes = csv.reader(file, delimiter=',')
    for code in iso_codes:
        get_country(code[1])