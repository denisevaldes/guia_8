from alienigena import Alienigena
from arma import Arma, Pistola, Cañon, Granada
class Juego():

    def __init__(self):
        #numero de aliens en el tablero 
        self._aliens = []

    @property
    def aliens(self):
        return self._aliens

    @aliens.setter
    def aliens(self, aliens):
        if isinstance(aliens, Alienigena):
            self._aliens.append(aliens)
        else:
            print("tipo de dato invalido")


