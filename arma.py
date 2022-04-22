
class Arma():

    def __init__(self):
        self._nombre = None
        self._daño = None

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def daño(self):
        return self._daño

class Pistola(Arma):

    def __init__(self):
        super().__init__()
        self._nombre = "pistola laser"
        self._daño = 1

class Cañon(Arma):

    def __init__(self):
        super().__init__()
        self._nombre = "cañon de protones"
        self._daño = 2

class Granada(Arma):

    def __init__(self):
        super().__init__()
        self._nombre = "granada antimateria"
        self._daño = 3