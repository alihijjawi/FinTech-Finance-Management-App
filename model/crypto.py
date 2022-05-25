from ..app import db
class Crypto(db.Model):
    __tablename__ ="cryptos"
    entry = db.Column(db.Integer(),primary_key=True,autoincrement=True)
    user_id=db.Column(db.Integer())
    crypto_name=db.Column(db.String(50))
    amount= db.Column(db.Integer())
    def __init__(self,user_id,crypto_name,amount):
        self.user_id=user_id
        self.crypto_name=crypto_name
        self.amount =amount