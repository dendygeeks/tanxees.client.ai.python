from tanxees.utils.Comparer import ComparerMixin

class Appearance(ComparerMixin):
    COMPARE_ATTRS = ('id', )
    
    GREEN = 'green'
    YELLOW = 'yellow'
    GRAY = 'gray'
    
    def __init__(self, id):
        self.__id = id

    @property
    def id(self):
        return self.__id

    @classmethod
    def fromId(cls, id):
        if isinstance(id, basestring):
            for name, value in vars(cls).iteritems(): 
                if value == id and name.isupper():
                    return cls(value)
        raise ValueError('Unknown appearance id: %s' % id)
