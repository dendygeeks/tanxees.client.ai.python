from tanxees.utils.Comparer import ComparerMixin

from six import string_types
from six import iteritems

class Appearance(ComparerMixin):
    COMPARE_ATTRS = ('id', )
    
    GREEN = 'green'
    YELLOW = 'yellow'
    GRAY = 'gray'
    
    __backmap__ = None

    def __init__(self, id):
        self.__id = id

    @property
    def id(self):
        return self.__id

    @classmethod
    def fromId(cls, id):
        if not cls.__backmap__:
            cls.__backmap__ = {value: name for (name, value) in iteritems(vars(cls)) if name.isupper()}
        try:
            return cls.__backmap__[id]
        except KeyError:
            raise ValueError('Unknown appearance id: %s' % id)
