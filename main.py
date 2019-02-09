from flask import Flask , render_template , request
from botAPI import *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/botresponse' , methods = ['POST'])
def botResponse():
    print(request.form["utext"])
    botMessage = botResponseReciever(request.form["utext"])
    return  botMessage

if __name__ == '__main__':
    app.run(debug= True)