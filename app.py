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

#api to get all crypto currencies from db
@app.route('/cryptocurrencies',methods=['GET'])
def getAllCryptos():
    pass
#api to get all stocks from db
@app.route('/stocks',methods=['GET'])
def getAllStocks():
    pass
#api to get specific crypto curr
@app.route('/cryptocurrencies/<crypto>',methods=['GET','POST'])
def getCrypto(crypto):
    pass

#api to get specific stock
@app.route('/stockc/<stock>',methods=['GET','POST'])
def getStock(stock):
    pass

#api to sell specific crypto, expects user token/id as well as amount to sell
#will update amount of money the user has in the bank on sell
@app.route('/sellcrypto/<crypto>',methods=['GET','POST'])
def sellCrypto(crypto):
    pass
#api to sell specific sotck, expects user token/id as well as amount to sell
#will update amount of money the user has in the bank on sell
@app.route('/sellstock/<stock>',methods=['GET','POST'])
def sellStock(stock):
    pass

#api to buy specific crypto currency, expects user token/id as well as amount to buy
#will update amount of money/crypto the user has in the bank on buy
@app.route('/buycrypto/<crypto>',methods=['GET','POST'])
def buyCrypto(crypto):
    pass
#api to buy specific crypto currency, expects user token/id as well as amount to buy
#will update amount of money/scrypto the user has in the bank on buy
@app.route('/buystock/<stock>',methods=['GET','POST'])
def sellStock(stock):
    pass
#this api returns everything owned by the user that is stored in the bank
@app.route('getbank',methods=['get'])
def getbank():
    pass





if __name__ == "__main__":
    app.run(debug=True)
