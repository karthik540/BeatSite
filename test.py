import json , requests

songname = "Halena"
url_request = "https://www.googleapis.com/youtube/v3/search?part=id&q="+ str(songname) +"&type=video&key=AIzaSyBtN6nKC7Jaai3hIWlumCQgrtkBZcmWq4U"
text = requests.get(url_request)
json_data = json.loads(text.text)
print(json_data)

"""import urllib.request
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

"""

asdasdasdsadsad