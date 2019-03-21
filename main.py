from flask import Flask , render_template , request , jsonify , sessions
from botAPI import *
from samppy import *
from image_url_fetcher import *
import json , requests, pprint
import pymysql
import urllib.request
from urllib.parse import quote_plus
import random

"""from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice")"""

import urllib.request
from urllib.parse import quote_plus

app = Flask(__name__)

@app.route('/')
def index(data = {'flag' : 0}):
    return render_template('index.html' , data = data)

@app.route('/signup' , methods = ['POST'])
def signup():
    email = request.form['email']
    name = request.form['name']
    password = request.form['password']

    connection = pymysql.connect(host = 'localhost' , user = 'root' , password = '' , db = 'BeatSite' , autocommit = True)

    cursor = connection.cursor()
    temp = random.randint(100000000 , 999999999)
    sql_query = "INSERT INTO userdetails (ID , Name , Password , Email)VALUES(%s , %s , %s , %s)"
    data = (temp , name , password , email)
    result = cursor.execute(sql_query , data)

    if result == 1:
        print('Register Successful !')
        return jsonify({'id' : temp , 'name' : name , 'email' : email , 'flag' : 1})
    else:
        print("Registration Unsuccessful !")
        return jsonify({'flag' : 0})

    

@app.route('/login' , methods = ['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    connection = pymysql.connect(host = 'localhost' , user = 'root' , password = '' , db = 'BeatSite')

    cursor = connection.cursor()
    sql_query = "SELECT * FROM  userdetails WHERE Email = %s AND Password = %s"
    data = (email , password)

    rows = cursor.execute(sql_query , data)
    result = cursor.fetchone()
    
    if rows == 1:
        return jsonify({'id' : result[0] , 'name' : result[1] , 'email' : result[3] , 'flag' : 1})
    else: 
        return jsonify({'flag' : 0})

@app.route('/browse/')
@app.route('/browse/<int:page_no>')
def browse(page_no = 1):
    album_list = []
    page_limit = 4                  #Page Limit Setting Variable
    
    url_request = 'http://api.musixmatch.com/ws/1.1/chart.tracks.get?apikey=3d136bab70652b62413441c2a2880831&chart_name=top&page=' + str(page_no) + '&page_size=' + str(page_limit) + '&country=in&f_has_lyrics=1'
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

@app.route('/videoId/<songname>' , methods = ['POST'])
def videoId(songname):
    print(songname)
    l = "https://www.googleapis.com/youtube/v3/search?part=id&q="+ str(songname) +"&type=video&key=AIzaSyBtN6nKC7Jaai3hIWlumCQgrtkBZcmWq4U"
    p = requests.get(l)
    j_objs = json.loads(p.text)
    pprint.pprint(j_objs)
    video_id = j_objs['items'][0]['id']['videoId']
    return video_id

@app.route('/album/<int:album_id>')
def album(album_id):
    track_list = []
    url_request = 'http://api.musixmatch.com/ws/1.1/album.tracks.get?apikey=3d136bab70652b62413441c2a2880831&album_id=' + str(album_id) + '&page=1&page_size=20'
    r = requests.get(url_request)
    json_data = json.loads(r.text)

    counter = 1
    for track in json_data['message']['body']['track_list']:
        songname = track['track']['track_name']
        """
        Youtube video Fetcher

        <iframe width="560" height="315" src="https://www.youtube.com/embed/GWH_k6S7YQU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

        l = "https://www.googleapis.com/youtube/v3/search?part=id&q="+ str(songname) +"&type=video&key=AIzaSyBtN6nKC7Jaai3hIWlumCQgrtkBZcmWq4U"
        p = requests.get(l)
        j_objs = json.loads(p.text)
        pprint.pprint(j_objs)
        video_id = j_objs['items'][0]['id']['videoId']
        print(video_id)

        """

        single_track = {
            'index' : counter ,
            'track_id' : track['track']['track_id'],
            'track_name' : track['track']['track_name'], 
            'track_rating' : track['track']['track_rating'],
            #'video_id' : video_id
        }
        track_list.append(single_track)
        counter = counter + 1
    for track in json_data['message']['body']['track_list']:
        url = fetch_url(str(track['track']['album_name']) , str(track['track']['artist_name']))
        if not track['track']['primary_genres']['music_genre_list']:
            genre = "Unknown"
        else:
            genre = track['track']['primary_genres']['music_genre_list'][0]['music_genre']['music_genre_name']
        album_info = {
            'album_name' : track['track']['album_name'],
            'artist_name' : track['track']['artist_name'],
            'album_url' : url ,
            'genre' : genre
        }
        break
    #pprint.pprint(json_data['message']['body']['track_list'])
    return render_template('album.html' , data = {'album_info': album_info , 'track_list' : track_list})

@app.route('/botresponse' , methods = ['POST'])
def botResponse():
    #print(request.form["utext"])
    botMessage = botResponseReciever(request.form["utext"])
    #print(botMessage)
    #speak.Speak("Hello")
    return  jsonify({'response': botMessage[0] , 'class' : botMessage[1]})

if __name__ == '__main__':
    app.run(debug= True)