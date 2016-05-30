from .UnitType import UnitType
from .Appearance import Appearance
from .MissileModel import MissileModel
from .PlayerUnitModel import PlayerUnitModel
from .DebugDataModel import DebugDataModel
from tanxees.utils.Comparer import ComparerMixin

class PlayerModel(ComparerMixin):
    COMPARE_ATTRS = ('unitType', 'appearance', 'frags', 'unit')

    def __init__(self, unitType, appearance, frags):
        self.__unitType = unitType
        self.__appearance = appearance
        self.frags = frags
        
        self.__missiles = []

        self.unit = None
        self.debugData = None

    @property
    def unitType(self):
        return self.__unitType

    @property
    def appearance(self):
        return self.__appearance

    @property
    def missiles(self):
        return self.__missiles

    def ownsMissile(self, missile):
        return missile in self.__missiles

    @classmethod
    def handleJson(cls, data):
        player = cls(UnitType.fromId(data['unitType']), Appearance.fromId(data['appearance']), data['frags'])
        player.__missiles = [MissileModel.handleJson(missile) for missile in data['missiles']]
        player.unit = PlayerUnitModel.handleJson(data['unit'])
        player.debugData = DebugDataModel.handleJson(data['debugData'])
        return player
