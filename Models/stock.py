from ..app import db
class Stock(db.Model):
    __tablename__ = "stocks"
    entry = db.Column(db.Integer(),primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer())
    stock_name = db.Column(db.String(50))
    amount = db.Column(db.Integer())
    def __init__(self, user_id, stock_name, amount):
        self.user_id = user_id
        self.stock_name = stock_name
        self.amount = amount