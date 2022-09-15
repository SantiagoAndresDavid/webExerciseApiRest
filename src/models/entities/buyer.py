class Buyer():
    def __init__(self,id, name=None, direction=None,idCar=None,idSeller = None)-> None:
        self.id = id
        self.name = name
        self.direction = direction  
        self.idCar = idCar
        self.idSeller = idSeller

    def to_JSON(self): 
        return {'id': self.id,
        'name': self.name,
        'direction ' : self.direction,
        'idCar': self.idCar,
        'idSeller': self.idSeller
        }   