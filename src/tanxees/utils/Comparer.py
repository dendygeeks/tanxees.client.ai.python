class ComparerMixin(object):
    COMPARE_ATTRS = ()
    def __eq__(self, other):
        if isinstance(other, type(self)):
            for attr in self.COMPARE_ATTRS:
                try:
                    myAttr = getattr(self, attr)
                    otherAttr = getattr(other, attr)
                except AttributeError:
                    return False
                if myAttr != otherAttr:
                    return False
            return True
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, type(self)):
            return not self.__eq__(other)
        return NotImplemented
