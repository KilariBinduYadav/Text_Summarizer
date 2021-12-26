from bs4 import BeautifulSoup
from urllib.request import urlopen

def url_text(link):
    f = urlopen(link)
    myfile = f.read()
    soup = BeautifulSoup(myfile)
    text = ' '.join(map(lambda p:p.text,soup.find_all('p')))
    return text