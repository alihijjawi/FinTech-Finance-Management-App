#User class
#has username, password, id(will be used as primary key)
from ..app import db
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer(),primary_key=True,autoincrement=True)
    username=db.Column(db.String(50))
    pwd = db.Column(db.String(50))
    def __init__(self,username,pwd):
        self.username=username
        self.pwd=pwd
