from tanxees.utils.Comparer import ComparerMixin

class UnitModel(ComparerMixin):
    COMPARE_ATTRS = ('sizeX', 'sizeY', 'posX', 'posY', 'angle')
    
    def __init__(self, sizeX, sizeY, posX, posY, angle):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.posX = posX
        self.posY = posY
        self.angle = angle

    @classmethod
    def handleJson(cls, data):
        return cls(data['sizeX'], data['sizeY'], data['posX'], data['posY'], data['angle'])
