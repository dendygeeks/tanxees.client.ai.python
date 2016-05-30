class DebugDataModel(object):
    def __init__(self, svg):
        self.__svg = svg

    def getSvg(self):
        return self.__svg

    @classmethod
    def handleJson(cls, data):
        return cls(data['svg'])

    def toJson(self):
        return self.__svg or None
