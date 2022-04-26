#bank class
#will hold financial info about the user (money/stocks/crypto owned) as well as
from ..app import db
class Bank(db.Model):
    __tablename__ = "bank"
    user_id=db.Column(db.Integer(),primary_key=True)
    amount=db.Column(db.Integer())
    def __init__(self,user_id,amount):
        self.user_id=user_id
        self.amount= amount