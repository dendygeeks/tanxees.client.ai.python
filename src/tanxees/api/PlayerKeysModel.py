class PlayerKeysModel(object):
    def __init__(self, right=False, up=False, left=False, down=False, fire=False):
        self.__right = right
        self.__up = up
        self.__left = left
        self.__down = down
        self.__fire = fire

    @property
    def right(self):
        return self.__right

    @property
    def up(self):
        return self.__up

    @property
    def left(self):
        return self.__left

    @property
    def down(self):
        return self.__down

    @property
    def fire(self):
        return self.__fire

    def toJson(self):
        return {'right': self.__right, 'up': self.__up,
                'left': self.__left, 'down': self.__down, 'fire': self.__fire}
