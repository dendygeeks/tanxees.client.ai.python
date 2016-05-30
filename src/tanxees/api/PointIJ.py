from tanxees.utils.Comparer import ComparerMixin

class PointIJ(ComparerMixin):
    COMPARE_ATTRS = ('i', 'j')
    
    def __init__(self, i, j):
        self.__i = i
        self.__j = j

    @property
    def i(self):
        return self.__i

    @property
    def j(self):
        return self.__j
