#User class
#has username, password, id(will be used as primary key)
class User:
    id = None
    username=None
    pwd = None
    def __init__(self,username,pwd):
        self.username=username
        self.pwd=pwd
