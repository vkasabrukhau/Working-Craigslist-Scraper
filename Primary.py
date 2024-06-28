from bs4 import BeautifulSoup
import requests
import pandas as pd


def CraigslistConnection(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.text, "html.parser")

    results = soup.find_all('li', {'class': 'cl-static-search-result'})
    informationList = []
    for product in results:
        product = {
            'product_title': product.find('div', {'class': 'title'}).text,
            'details': product.find('div', {'class': 'price'}).text,
            'location': '' if product.find('div', {'class': 'location'}) == None else product.find('div', {'class': 'location'}).text.strip(),
            'link': product.find('a')['href']
        }
        informationList.append(product)

    craigslistDF = pd.DataFrame(informationList)
    print(craigslistDF)
    return craigslistDF


CraigslistConnection("https://hartford.craigslist.org/search/sya#search=1")
CraigslistConnection("https://hartford.craigslist.org/search/syp#search=1")
