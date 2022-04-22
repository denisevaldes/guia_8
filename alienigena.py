from arma import *
import random as rd 

class Alienigena():

    def __init__(self, coordenadax, coordenaday):
        self._x_coordenada = coordenadax
        self._y_coordenada = coordenaday
        self._vida = 3
        self._arma = []

    @property
    def x_coordenadas(self):
        return self._x_coordenada

    @property
    def y_coordenadas(self):
        return self._y_coordenada

    @property
    def vida(self):
        return self._vida

    @property
    def arma(self):
        return self._arma

    @arma.setter
    def arma(self, arma):
        if isinstance(arma, Arma):   
            self._arma.append(arma)
        else: 
            print("El dato no corresponde")

    def hit(self):
        self._vida -= 1
        #return self._vida

    def is_alive(self):
        vivo = None
        if self._vida <= 0:
            vivo = False
        else:
            vivo = True
        return vivo 

    def teleport(self):

        self._x_coordenada = rd.randrange(10)
        self._y_coordenada = rd.randrange(10)     
        


    def colisiones(self):
        pass
    