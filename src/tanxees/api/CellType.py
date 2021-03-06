from tanxees.utils.Comparer import ComparerMixin

from six import string_types
from six import iteritems

class CellType(ComparerMixin):
    COMPARE_ATTRS = ('code', )
    
    EMPTY = "E"
    CONCRETE = "C"
    BRICKS = "B"
    TREE = "T"
    DARK_CONCRETE = "DC"
    DARK_BRICKS = "DB"
    
    __backmap__ = None
    
    def __init__(self, code):
        self.__code = code

    @property
    def code(self):
        return self.__code

    def isWall(self):
        return self.__code in (self.CONCRETE, self.BRICKS, self.DARK_CONCRETE, self.DARK_BRICKS)

    def isBrick(self):
        return self.__code in (self.BRICKS, self.DARK_BRICKS) 

    @classmethod
    def fromCode(cls, code):
        if not cls.__backmap__:
            cls.__backmap__ = {value: name for (name, value) in iteritems(vars(cls)) if name.isupper()}
        try:
            return cls.__backmap__[code]
        except KeyError:
            raise ValueError('Unknown cell type code: %s' % code)
