from .GameModel import GameModel

class TheStateModel(object):
    def __init__(self, game, activePlayerId):
        self.__game = game
        self.__activePlayerId = activePlayerId

    @property
    def game(self):
        return self.__game

    @property
    def activePlayerId(self):
        return self.__activePlayerId

    @classmethod
    def handleJson(cls, data):
        return cls(GameModel.handleJson(data['game']), data['activePlayerId'])
