from tanxees.utils.Comparer import ComparerMixin

class CellType(ComparerMixin):
    COMPARE_ATTRS = ('code', )
    
    EMPTY = "E"
    CONCRETE = "C"
    BRICKS = "B"
    TREE = "T"
    DARK_CONCRETE = "DC"
    DARK_BRICKS = "DB"
    
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
        if isinstance(code, basestring):
            for name, value in vars(cls).iteritems(): 
                if value == code and name.isupper():
                    return cls(value)
        raise ValueError('Unknown cell type code: %s' % code)