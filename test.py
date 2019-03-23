from flask import Flask, session, redirect, url_for, escape, request , render_template

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
	session['username'] = "asd"
	if 'username' in session:
		data = {
            'flag' : 1,
            'username' : "Karthik",
            'email' : "rajkarthik967@gmail.com"
        }
		return render_template('index.html' , data = data)

	data = {
		'flag' : 0
	}
	return render_template('index.html' , data = data)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug= True)
