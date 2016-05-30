from tanxees.utils.Comparer import ComparerMixin

class Direction(ComparerMixin):
    COMPARE_ATTRS = ('angle')
    
    RIGHT = 0
    DOWN = 90
    LEFT = 180
    UP = 270

    def __init__(self, angle):
        if angle not in (self.RIGHT, self.DOWN, self.LEFT, self.UP):
            raise ValueError('Unexpected angle value: %s' % angle)
        self.__angle = angle

    @property
    def angle(self):
        return self.__angle
