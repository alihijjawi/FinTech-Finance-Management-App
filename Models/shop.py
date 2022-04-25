#shop class
#will have itemid and name and price
class Stock:
    itemid = None
    name = None
    price = None

    def __init__(self,itemid,name,price):
        self.itemid=itemid
        self.name=name
        self.price=price
