from tanxees.utils.Comparer import ComparerMixin

from six import string_types

class UnitType(ComparerMixin):
    COMPARE_ATTRS = ('id', 'sizeW', 'sizeL')
    
    def __init__(self, id, sizeW, sizeL):
        self.__id = id
        self.__sizeW = sizeW
        self.__sizeL = sizeL

    @property
    def id(self):
        return self.__id

    @property
    def sizeW(self):
        return self.__sizeW

    @property
    def sizeL(self):
        return self.__sizeL

    @classmethod
    def fromId(cls, id):
        if isinstance(id, string_types):
            for value in vars(cls).values(): 
                if isinstance(value, cls) and value.id == id:
                    return value
        raise ValueError('Unknown unit type id: %s' % id)

UnitType.SMALL = UnitType('small', 20, 27)
UnitType.MEDIUM = UnitType('medium', 34, 34)
