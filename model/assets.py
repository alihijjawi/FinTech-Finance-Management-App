#assets class
#will have username and assets of player (itemids) and amount owned
class Stock:
    username = None
    itemid = None
    amount = None

    def __init__(self,username,itemid,amount):
        self.username=username
        self.itemid=itemid
        self.amount=amount
