class Car():
    def __init__(self,id,place=None,color=None,model=None) -> None:
        self.id = id
        self.place = place
        self.color = color
        self.model = model

    def to_JSON(self): 
        return {
            'id': self.id,
            'place': self.place,
            'color': self.color,
            'model':self.model
        }         