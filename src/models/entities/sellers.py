class Car():
    def __init__(self, id,name=None):
        self.id = id
        self.name = name

    def to_JSON(self): 
        return {"id": self.id,
        "name": self.name
        }        