from CellType import CellType
from tanxees.utils.Comparer import ComparerMixin

class CellModel(ComparerMixin):
    COMPARE_ATTRS = ('type', 'touched')
    
    def __init__(self, type):
        self.__type = type
        self.__touched = 0
    
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    @property
    def touched(self):
        return self.__touched

    @touched.setter
    def touched(self, moment):
        self.__touched = moment

    @classmethod
    def handleJson(cls, data):
        cell = cls(CellType.fromCode(data['type']))
        cell.__touched = data.get('touched', 0)
        return cell
