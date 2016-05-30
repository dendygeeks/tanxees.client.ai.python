import logging

from .ClientStateControllerWebSocket import ClientStateControllerWebSocket

class AIBase(object):
    URL_START = 'ws://localhost:9876/player?playerId='

    def __init__(self, playerId, controller):
        logging.basicConfig()
        self.webSocket = ClientStateControllerWebSocket(self.URL_START + playerId, controller)

    def run(self):
        self.webSocket.run()
