from flask import Flask , render_template , request
from botAPI import *
from image_url_fetcher import *
import json , requests, pprint
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/browse/')
@app.route('/browse/<int:page_no>')
def browse(page_no = 1):
    album_list = []
    page_limit = 16                  #Page Limit Setting Variable
    
    url_request = 'http://api.musixmatch.com/ws/1.1/chart.tracks.get?apikey=3d136bab70652b62413441c2a2880831&chart_name=top&page=' + str(page_no) + '&page_size=' + str(page_limit) + '&country=us&f_has_lyrics=1'
    r = requests.get(url_request)
    json_data = json.loads(r.text)
    
    for track in json_data['message']['body']['track_list']:
        url = fetch_url(str(track['track']['album_name']) , str(track['track']['artist_name']))
        single_album_list = {
            'album_id' : track['track']['album_id'],
            'album_name' : track['track']['album_name'] , 
            'artist_name' : track['track']['artist_name'],
            'image_url': url
        }
        album_list.append(single_album_list)
    pprint.pprint(album_list)
    return render_template('browse.html' , data = {'album_list' : album_list , 'page_no' : page_no})

@app.route('/album/<int:album_id>')
def album(album_id):
    track_list = []
    url_request = 'http://api.musixmatch.com/ws/1.1/album.tracks.get?apikey=3d136bab70652b62413441c2a2880831&album_id=' + str(album_id) + '&page=1&page_size=20'
    r = requests.get(url_request)
    json_data = json.loads(r.text)

    counter = 1
    for track in json_data['message']['body']['track_list']:
        single_track = {
            'index' : counter ,
            'track_id' : track['track']['track_id'],
            'track_name' : track['track']['track_name'] , 
            'track_rating' : track['track']['track_rating']
        }
        track_list.append(single_track)
        counter = counter + 1
    for track in json_data['message']['body']['track_list']:
        url = fetch_url(str(track['track']['album_name']) , str(track['track']['artist_name']))
        album_info = {
            'album_name' : track['track']['album_name'],
            'artist_name' : track['track']['artist_name'],
            'album_url' : url ,
            'genre' : track['track']['primary_genres']['music_genre_list'][0]['music_genre']['music_genre_name']
        }
        break

    return render_template('album.html' , data = {'album_info': album_info , 'track_list' : track_list})

@app.route('/botresponse' , methods = ['POST'])
def botResponse():
    print(request.form["utext"])
    botMessage = botResponseReciever(request.form["utext"])
    
    return  botMessage

if __name__ == '__main__':
    app.run(debug= True)