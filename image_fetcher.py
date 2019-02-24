import requests
from bs4 import BeautifulSoup


def fetch_url(artistname , albumname):
    queryText = artistname + " " + albumname
    baseUrl = 'https://www.google.com/search?rlz=1C1CHBD_enIN798IN798&biw=1536&bih=471&tbm=isch&sa=1&ei=25xrXIzIC4_S8wX5gpDYDg&q='
    source_code = requests.get(baseUrl + queryText)
    source_text = source_code.text
    soup = BeautifulSoup(source_text , features="html5lib")
    tag = soup.findAll("a")
    print(tag)

fetch_url('A Star Is Born Soundtrack' , 'Lady Gaga feat. Bradley Cooper')