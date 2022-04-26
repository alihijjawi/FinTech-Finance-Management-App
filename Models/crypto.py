#crypto class
#will have id as well as name
#since the price changes, the price will not be saved in the db
from ..app import db
class Crypto(db.Model):
    __tablename__ ="crypto"
    user_id=db.Column(db.Integer())
    crypto_name=db.Column(db.Sting(50))
    amount= db.Column(db.Integer())

    def __init__(self,user_id,crypto_name,amount):
        self.user_id=user_id
        self.crypto_name=crypto_name
        self.amount =amount
