import urllib.request
from urllib.parse import quote_plus
import json
"""
with urllib.request.urlopen("http://api.musixmatch.com/ws/1.1/track.search?q_artist="+s+"&page_size=3&page=1&s_track_rating=desc&q_track="+y+"&apikey=d9f9da53de4a90b828fcf767cbfccffe") as url:
    s = url.read()
    j_obj = json.loads(s)
def genre():
    if not j_obj['message']['body']['track_list'][0]['track']['primary_genres']['music_genre_list'][0]['music_genre']['music_genre_name']:
        print('Not a vaid track')
    else:
        print (j_obj['message']['body']['track_list'][0]['track']['primary_genres']['music_genre_list'][0]['music_genre']['music_genre_name'])
def get():
    if not j_obj['message']['body']['track_list'][0]['track']['primary_genres']['music_genre_list'][0]['music_genre']['music_genre_name']:
        print('Not a vaid track')
    else:
        print (j_obj['message']['body']['track_list'][0]['track']['album_name'])
"""
def getvideo():
    l = quote_plus(str(input("Enter the song name :")))
    with urllib.request.urlopen("https://www.googleapis.com/youtube/v3/search?part=id&q="+l+"&type=video&key=AIzaSyBtN6nKC7Jaai3hIWlumCQgrtkBZcmWq4U") as url:
        p = url.read()
        j_objs = json.loads(p)
        link = j_objs['items'][0]['id']['videoId']
        return link
"""get()
x = j_obj['message']['body']['track_list'][0]['track']['primary_genres']['music_genre_list'][0]['music_genre']['music_genre_name']
genrelist = []
genrelist.append(x)
l = genrelist
import csv

out = open('abl.csv', 'a')
for row in l:
    for column in row:
        out.write('%s' % column)
    out.write('\n')
out.close()
print('File transfer is done from list to csv')"""
