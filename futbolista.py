from deportista import Deportista
from persona import Persona

class Futbolista(Deportista,Persona):
    _listaFutbolista = []

    def __init__(self,nombre,edad,altura,sexo,anosPracticando,golesMarcados,tarjetasRojas,piernaHabil):
        Persona.__init__(self,nombre,edad,altura,sexo)
        Deportista.__init__(self,anosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._pernaHabil = piernaHabil
        Futbolista._listaFutbolista.append(self)

    def getGolesMarcados(self):
        return self._golesMarcados

    def getTarjetasRojas(self):
        return self._tarjetasRojas
    
    def getPiernaHabil(self):
        return self._pernaHabil

    def __str__(self):
        return f"Mi nombre es {super().getNombre()} soy profesional en el deporte {super().getDeporte()} Tengo {super().getEdad()} años de edad y llevo {super().getAñosPracticando()} años en el deporte"

