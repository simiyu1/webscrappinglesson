from  urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://treehouse-projects.github.io/horse-land/index.html')
soup = BeautifulSoup(html.read(), 'html.parser')

my_divs = soup.find_all('div', {"class": "featured"})

# for one_div in my_divs:
#     print(one_div.prettify())
for link in soup.find_all("a"):
    print(link.get("href"))