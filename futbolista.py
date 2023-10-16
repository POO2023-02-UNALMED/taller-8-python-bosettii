from deportista import Deportista
from persona import Persona

class Futbolista(Deportista,Persona):
    listaFutbolista = []

    def __init__(self,nombre,edad,altura,sexo,anosPracticando,golesMarcados,tarjetasRojas,piernaHabil):
        Persona.super(nombre,edad,altura,sexo)
        Deportista.super(anosPracticando)
        self._deporte = "Futbol"
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._pernaHabil = piernaHabil
        Futbolista.listaFutbolista.add(self)

    def getGolesMarcados(self):
        return self._golesMarcados

    def getTarjetasRojas(self):
        return self._tarjetasRojas
    
    def getPiernaHabil(self):
        return self._pernaHabil

    def __str__(self):
        return "Mi nombre es "+ Persona.nombre + " + soy profesional en el deporte " + Deportista.deporte + " Tengo "+Persona.edad+" años de edad y llevo " + Deportista.añosParticipando + " años en el deporte"

