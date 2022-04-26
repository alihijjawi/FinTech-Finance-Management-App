import datetime

from flask import Flask, abort, session , render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from flask_bcrypt import Bcrypt
from flask_cors import CORS, cross_origin
from flask_marshmallow import Marshmallow
from flask import request
from flask import jsonify
from flask_session import Session
from flask_mail import Mail, Message
import os
import jwt

app = Flask(__name__)

app.secret_key = '\xf0?a\x9a\\\xff\xd4;\x0c\xcbHi'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'Project_DB.db')
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
db = SQLAlchemy(app)
meta = MetaData()


# @app.route("/")
# def main():
#     if 'user' in session:
#         user = session['user']
#     else:
#         user = None
#     return render_template('index.html',user=user)
userstable = Table('users', meta, Column('id', Integer, primary_key=True, autoincrement=True),
                   Column('username', String ))
banktable= Table('bank', meta, Column('user_id',Integer,primary_key=True,autoincrement=False),Column("amount",Integer))


from .Models.user import User
from .Models.bank import Bank
from .Models.crypto import Crypto
from .Models.stock import Stock


@app.route('/login', methods=['GET', 'POST'])
def login():
    user = User.query.filter_by(username=request.json["username"]).first()
    if user is None:
        abort(403)
    if (request.json["pwd"]!=user.pwd):
        abort(404)
    return jsonify({"id":user.id})


#sign up to the database and intialize stock and crypto values to 0
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    name = request.json['username']
    pwd = request.json['pwd']



    if not name or not pwd:
        # name is empty or pwd is empty
        abort(400)
    # check for unique name
    not_unique = User.query.filter_by(username=name).first()
    # similar username exists
    if not_unique:
        abort(403)
    else:
        #create user add to db
        newuser = User(name,pwd)
        db.session.add(newuser)
        newu= User.query.filter_by(username=name).first()
        #create bank instance add to db
        new_bank=Bank(newu.id,0)
        db.session.add(new_bank)
        db.session.commit()
        #to DO: instantiate entries for crypto and stocks once types are decided

        return "success"



# @app.route('/logout', methods=['GET'])
# def logout():
#     if 'user' in session:
#         session.pop('user', None)
#         return redirect(url_for('main'))
#     else:
#         return redirect(url_for('main'))

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
@app.route('/stocks/<stock>',methods=['GET','POST'])
def getStock(stock):
    pass

#api to sell specific crypto, expects user token/id as well as amount to sell
#will update amount of money the user has in the bank on sell
@app.route('/sellcrypto',methods=['POST'])
def sellCrypto():
    user_id = request.json['id']
    crypto_name=request.json['name']
    amount = request.json['amount']
    price = request.json['price']
    #update money in bank
    user_bank = Bank.query.filter_by(user_id=user_id)
    user_bank.amount=user_bank.amount+int(price)*int(amount)
    #update amount of crypto owned
    user_crypto=Crypto.query.filter_by(user_id=user_id,crypto_name=crypto_name)
    if user_crypto.amount-amount<0:
        user_crypto.amount=0
    else:
        user_crypto.amount = user_crypto.amount-amount
    db.session.commit()
    return "success"



#api to sell specific sotck, expects user token/id as well as amount to sell
#will update amount of money the user has in the bank on sell
@app.route('/sellstock',methods=['POST'])
def sellStock():
    pass

#api to buy specific crypto currency, expects user token/id as well as amount to buy
#will update amount of money/crypto the user has in the bank on buy
@app.route('/buycrypto/<crypto>',methods=['POST'])
def buyCrypto(crypto):
    pass

#api to buy specific crypto currency, expects user token/id as well as amount to buy
#will update amount of money/scrypto the user has in the bank on buy
@app.route('/buystock/<stock>',methods=['POST'])
def buyStock(stock):
    pass

#this api returns everything owned by the user that is stored in the bank
@app.route('/getbank',methods=['get'])
def getbank():
    pass

def getPrices():
    pass





if __name__ == "__main__":
    app.run(debug=True)
