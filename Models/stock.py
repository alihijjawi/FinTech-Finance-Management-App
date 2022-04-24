#stock class
#will have id as well as name
#since the price changes, the price will not be saved in the db
class Stock:
    id = None
    name=None

    def __init__(self,id,name):
        self.name=name
        self.id=id
