from .FlagModel import FlagModel
from .CellModel import CellModel
from .PlayerModel import PlayerModel

class GameModel(object):
    def __init__(self, fieldWidth, fieldHeight, isOver, flag, field, cellSize):
        self.__fieldWidth = fieldWidth
        self.__fieldHeight = fieldHeight
        self.__cellSize = cellSize
        
        self.isOver = isOver
        self.flag = flag
        self.field = field

        self.__players = {}

    @property
    def fieldWidth(self):
        return self.__fieldWidth

    @property
    def fieldHeight(self):
        return self.__fieldHeight

    @property
    def cellSize(self):
        return self.__cellSize

    @property
    def players(self):
        return self.__players

    def findPlayerId(self, player):
        for key, value in self.__players.items():
            if value == player:
                return key
        return None

    def findPlayerIdByTank(self, unit):
        for key, value in self.__players.items():
            if value.unit == unit:
                return key
        return None

    def findMissileOwner(self, missile):
        for player in self.__players.values():
            if player.ownsMissle(missile):
                return player
        return None

    @classmethod
    def handleJson(cls, data):
        field = []
        for line in zip(*[iter(data['field'])] * data['fieldWidth']):
            field.append([CellModel.handleJson(cell) for cell in line])

        game = cls(data['fieldWidth'], data['fieldHeight'], data['isOver'],
                    None, #FlagModel.handleJson(data['flag']), ## flag disabled so far
                    field, data['cellSize'])
        game.__players = {name: PlayerModel.handleJson(value) for (name, value) in data['players'].items()}
        return game
