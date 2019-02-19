from flask import Flask , render_template , request
from botAPI import *
import requests
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/browse')
def browse():
    url_request = 'http://api.musixmatch.com/ws/1.1/chart.tracks.get?apikey=3d136bab70652b62413441c2a2880831&chart_name=top&page=1&page_size=5&country=in&f_has_lyrics=1'
    r = requests.get(url_request)
    jsonObj = open("response.json" , "w+")
    jsonObj.write(r.text)
    jsonObj.close()
    return render_template('browse.html')


@app.route('/botresponse' , methods = ['POST'])
def botResponse():
    print(request.form["utext"])
    botMessage = botResponseReciever(request.form["utext"])
    
    return  botMessage

if __name__ == '__main__':
    app.run(debug= True)