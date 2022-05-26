import datetime
import finnhub
from flask import Flask, abort, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
import jwt
from flask_cors import CORS

import requests
import json

from .db_config import DB_CONFIG

finnhub_client = finnhub.Client(api_key="c9ommfaad3i8gdca97sg")
payload = {}
headers= {}

SECRET_KEY = "b'|\xe7\xbfU3`\xc4\xec\xa7\xa9zf:}\xb5\xc7\xb9\x139^3@Dv'"
CRYPTO_URL = "http://api.coincap.io/v2/assets"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONFIG
CORS(app)
db = SQLAlchemy(app)

from .model.user import User
from .model.stock import Stock
from .model.crypto import Crypto
from .model.bank import Bank

stock_name=[]
crypto_name=[]

@app.route('/login', methods=['POST']) #api to login
def getAuth():
    username = request.json["username"]
    password = request.json["pwd"]
    user = User.query.filter_by(username=username).first()
    if user is None: #username does not exists
        abort(403)
    elif password != user.pwd: #incorrect password
        abort(403)
    tkn = create_token(username)
    return jsonify(token=tkn)

@app.route('/signup', methods=['GET', 'POST']) #sign up to the database and intialize stock and crypto values to 0
def signup():
    username = request.json['username']
    password = request.json['pwd']
    notUnique = User.query.filter_by(username=username).first() # check for unique name
    if notUnique: # similar username exists
        abort(403)
    else: #create user add to db
        newUser = User(username,password)
        db.session.add(newUser)
        addedUser = User.query.filter_by(username=username).first()
        newBank = Bank(addedUser.id,0) #create bank instance add to db
        db.session.add(newBank)
        #CREATE INSTANCES OF EACH CRYPTO AND STOCKS FOR THE USER AND SET AMOUNT TO 0
        stocks=['AAPL','GOOGL','FB','TSLA']
        cryptos=['BTC','ETH','BNB']
        #stocks
        for stk in stocks:
            st = Stock(addedUser.id,stk,0)
            db.session.add(st)
        #cryptos
        for cry in cryptos:
            cryp = Crypto(addedUser.id,cry,0)
            db.session.add(cryp)
        db.session.commit()
        return "success"

#api to get the price of all the crypto we chose
@app.route('/cryptocurrencies',methods=['GET']) #api to get all crypto currencies from db
def getAllCryptos():
    cryptos = ['bitcoin', 'ethereum', 'binance-coin']
    short   = ['BTC','ETH','BNB']
    prices = {}
    for i in range(len(cryptos)):
        temp = requests.request('GET', CRYPTO_URL+'/'+cryptos[i], data=payload, headers=headers)
        temp = json.loads(temp.text.encode('utf8'))
        prices[short[i]] = temp['data']['priceUsd']
    return jsonify(prices)


@app.route('/stocks',methods=['GET']) #api to get all stocks from db
def getAllStocks():
    stocks = ['AAPL', 'GOOGL', 'FB', 'TSLA']
    prices={}
    for st in stocks:
        prices[st]=finnhub_client.quote(st)['c']
    return jsonify(prices)
#api to get the current price in USD of the chose cryptocurrency
@app.route('/cryptocurrencies/<crypto>',methods=['GET','POST']) #api to get specific crypto curr
def getCrypto(crypto):
    result = requests.request('GET',CRYPTO_URL+'/'+str(crypto),data=payload,headers=headers)
    ret = json.loads(result.text.encode('utf8'))
    return ret['data']['priceUsd']

#api to get specific stock price
@app.route('/stocks/<stock>',methods=['GET','POST'])
def getStock(stock):
    #no need to handle wrong name because the api calls will be made for specific cryptos which we know
    return jsonify({str(stock):finnhub_client.quote(stock)['c']})



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
        abort()
    else:
        user_crypto.amount = user_crypto.amount-amount
    db.session.commit()
    return "success"



#api to sell specific sotck, expects user token/id as well as amount to sell
#will update amount of money the user has in the bank on sell
@app.route('/sellstock',methods=['POST'])
def sellStock():
    user_id = request.json['id']
    stock_name = request.json['name']
    amount = request.json['amount']
    price = request.json['price']
    # update money in bank
    user_bank = Bank.query.filter_by(user_id=user_id)
    user_bank.amount = user_bank.amount + int(price) * int(amount)
    # update amount of crypto owned
    user_stock = Stock.query.filter_by(user_id=user_id, stock_name=stock_name)
    if user_stock.amount - amount < 0:
        abort()
    else:
        user_stock.amount = user_stock.amount - amount
    db.session.commit()
    return "success"

#api to buy specific crypto currency, expects user token/id as well as amount to buy
#will update amount of money/crypto the user has in the bank on buy
@app.route('/buycrypto',methods=['POST'])
def buyCrypto():
    user_id = request.json['id']
    crypto_name = request.json['name']
    amount = request.json['amount']
    price = request.json['price']
    # update money in bank
    user_bank = Bank.query.filter_by(user_id=user_id)
    if user_bank.amount-(int(price) * int(amount))<0:
        abort()
    else: 
        user_bank.amount=user_bank.amount-(int(price) * int(amount))
    # update amount of crypto owned
    user_crypto = Crypto.query.filter_by(user_id=user_id, crypto_name=crypto_name)

    user_crypto.amount = user_crypto.amount + amount

    db.session.commit()
    return "success"

#api to buy specific crypto currency, expects user token/id as well as amount to buy
#will update amount of money/scrypto the user has in the bank on buy
@app.route('/buystock',methods=['POST'])
def buyStock():
    user_id = request.json['id']
    stock_name = request.json['name']
    amount = request.json['amount']
    price = request.json['price']
    # update money in bank
    user_bank = Bank.query.filter_by(user_id=user_id)
    if user_bank.amount - (int(price) * int(amount)) < 0:
        abort()
    else: 
        user_bank.amount = user_bank.amount - (int(price) * int(amount)) < 0
    # update amount of crypto owned
    user_stock = Stock.query.filter_by(user_id=user_id, stock_name=stock_name)

    user_stock.amount = user_stock.amount + amount

    db.session.commit()
    return "success"

#this api returns money owned by the user that is stored in the bank
@app.route('/getbank',methods=['get'])
def getbank():
    user_id = request.json['id']
    user_bank= - Bank.query.filter_by(user_id=user_id)
    return jsonify({"money":user_bank.amount})

def getPrices():
    pass

def create_token(user_name):
    payload = {
    'exp': datetime.datetime.utcnow() + datetime.timedelta(days=4),
    'iat': datetime.datetime.utcnow(),
    'sub': user_name
    }
    return jwt.encode(
    payload,
    SECRET_KEY,
    algorithm='HS256'
    )

def extract_auth_token(authenticated_request):
    auth_header = authenticated_request.headers.get('Authorization')
    if auth_header:
        return auth_header.split(" ")[1]
    else:
        return None

def decode_token(token):
    payload = jwt.decode(token, SECRET_KEY, 'HS256')
    return payload['sub']
