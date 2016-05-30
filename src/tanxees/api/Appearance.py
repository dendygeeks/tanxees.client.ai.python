from tanxees.utils.Comparer import ComparerMixin

from six import string_types
from six import iteritems

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
        if isinstance(id, string_types):
            for name, value in iteritems(vars(cls)): 
                if value == id and name.isupper():
                    return cls(value)
        raise ValueError('Unknown appearance id: %s' % id)
