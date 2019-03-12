import urllib.request
from bs4 import BeautifulSoup

def getID(song_name):
    query = urllib.parse.quote(song_name)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    for vid in soup.find_all(attrs={'class':'yt-uix-tile-link'}):
        return 'https://www.youtube.com' + vid['href']
        break

