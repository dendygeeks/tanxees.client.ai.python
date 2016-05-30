from tanxees.utils.Comparer import ComparerMixin
from UnitModel import UnitModel

class PlayerUnitModel(UnitModel):
    COMPARE_ATTRS = ('sizeX', 'sizeY', 'posX', 'posY', 'angle', 'moving')
    
    def __init__(self, sizeX, sizeY, posX, posY, angle, moving):
        UnitModel.__init__(self, sizeX, sizeY, posX, posY, angle)
        self.moving = moving

    @classmethod
    def handleJson(cls, data):
        unit = UnitModel.handleJson(data)
        return cls(unit.sizeX, unit.sizeY, unit.posX, unit.posY, unit.angle, data['moving'])
