class ClientStateModel(object):
    def __init__(self, keys, debugData):
        self.keys = keys
        self.debugData = debugData

    def toJson(self):
        return {'keys': self.keys.toJson(), 'debugData': self.debugData.toJson()}
