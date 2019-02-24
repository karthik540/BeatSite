from flask import Flask , render_template , request
from botAPI import *
from image_url_fetcher import *
import json , requests, pprint
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/browse/<int:page_no>')
def browse(page_no):
    album_list = []
    page_limit = 4                  #Page Limit Setting Variable
    
    url_request = 'http://api.musixmatch.com/ws/1.1/chart.tracks.get?apikey=3d136bab70652b62413441c2a2880831&chart_name=top&page=' + str(page_no) + '&page_size=' + str(page_limit) + '&country=us&f_has_lyrics=1'
    r = requests.get(url_request)
    json_data = json.loads(r.text)

    for track in json_data['message']['body']['track_list']:
        url = fetch_url(str(track['track']['album_name']) , str(track['track']['artist_name']))
        single_album_list = {
            'album_name' : track['track']['album_name'] , 
            'artist_name' : track['track']['artist_name'],
            'image_url': url
        }
        album_list.append(single_album_list)

    pprint.pprint(album_list)
    return render_template('browse.html' , data = {'album_list' : album_list , 'page_no' : page_no})


@app.route('/botresponse' , methods = ['POST'])
def botResponse():
    print(request.form["utext"])
    botMessage = botResponseReciever(request.form["utext"])
    
    return  botMessage

if __name__ == '__main__':
    app.run(debug= True)