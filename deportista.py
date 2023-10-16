class Deportista():

    def __init__(self,deporte,anosPracticando):
        self._deporte = deporte
        self._anosPracticando=anosPracticando

    def getDeporte(self):
        return self._deporte

    def getAñosPracticando(self):
        return self._anosPracticando