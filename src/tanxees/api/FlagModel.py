from UnitModel import UnitModel
from tanxees.utils.Comparer import ComparerMixin

class FlagModel(UnitModel):
    COMPARE_ATTRS = ('isCrashed', 'sizeX', 'sizeY', 'posX', 'posY', 'angle')
    
    def __init__(self, sizeX, sizeY, posX, posY, angle, isCrashed):
        UnitModel.__init__(self, sizeX, sizeY, posX, posY, angle)
        self.isCrashed = isCrashed

    @classmethod
    def handleJson(cls, data):
        unit = UnitModel.handleJson(data)
        return cls(unit.sizeX, unit.sizeY, unit.posX, unit.posY, unit.angle, data['isCrashed'])
