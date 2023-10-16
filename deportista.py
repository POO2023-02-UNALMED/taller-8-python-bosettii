class Deportista():

    def __init__(self,anosPracticando):
        self._deporte = "Futbol"
        self._anosPracticando=anosPracticando

    def getDeporte(self):
        return self._deporte

    def getAñosPracticando(self):
        return self._anosPracticando