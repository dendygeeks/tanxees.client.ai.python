from tanxees.api.ClientStateModel import ClientStateModel
from tanxees.api.PlayerKeysModel import PlayerKeysModel
from tanxees.api.DebugDataModel import DebugDataModel

class ClientStateControllerBase(object):
    def __init__(self, clientState=None):
        if clientState is None:
            clientState = ClientStateModel(PlayerKeysModel(), DebugDataModel(None))
            
        self.__clientState = clientState

    @property
    def clientState(self):
        return self.__clientState

    def updateClientState(self, theState):
        raise NotImplementedError()
