#stock class
#will have id as well as name
#since the price changes, the price will not be saved in the db
from ..app import db
class Stock:
    __tablename__ = "stock"
    user_id = db.Column(db.Integer())
    stock_name = db.Column(db.Sting(50))
    amount = db.Column(db.Integer())

    def __init__(self, user_id, stock_name, amount):
        self.user_id = user_id
        self.stock_name = stock_name
        self.amount = amount

