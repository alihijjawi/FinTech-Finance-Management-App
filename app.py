from flask import *
import mysql.connector
import functions

app = Flask(__name__)

app.secret_key = '\xf0?a\x9a\\\xff\xd4;\x0c\xcbHi'

@app.route("/")
def main():
    if 'user' in session:
        user = session['user']
    else:
        user = None
    return render_template('index.html',user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' in session:
        return redirect(url_for('main'))
    elif request.method == 'POST':
        user = request.form["userName"]
        password = request.form["password"]
        ret = functions.authenticate(user, password)
        if ret == 1:
            return render_template('login.html', error="Username does not exist!")
        elif ret == 2:
            return render_template('login.html', error="Incorrect Password!")
        else:
            session['user'] = user
        return redirect(url_for('main'))
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if 'user' in session:
        return redirect(url_for('main'))
    if request.method == 'POST':
        user = request.form["userName"]
        password = request.form["password"]
        ret = functions.register(user, password)
        if ret == 1:
            return render_template('signup.html', error="Username already exists!")
        elif ret == 0:
            session['user'] = user
            return redirect(url_for('main'))
    return render_template('signup.html')


@app.route('/logout', methods=['GET'])
def logout():
    if 'user' in session:
        session.pop('user', None)
        return redirect(url_for('main'))
    else:
        return redirect(url_for('main'))

if __name__ == "__main__":
    app.run(debug=True)
