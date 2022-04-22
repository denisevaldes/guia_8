from webbrowser import get
from alienigena import Alienigena
from juego import Juego
from arma import Arma
import random as rd 
from os import system

def imprimir_aliens(lista):

    for x in lista:
    
        print(x.x_coordenadas, x.y_coordenadas)
        print('\n')
        
def aliens(lista_aliens, num_aliens):
    
    for x in range(num_aliens):

        x = rd.randrange(10)
        y = rd.randrange(10)     
        
        alien = Alienigena(x, y)
        lista_aliens.append(alien)

    return alien

def total_aliens_created(lista_aliens):
    print(len(lista_aliens))

def main():

    lista_aliens =  []
    print("cuantos aliens quieres crear? ")
    num_aliens = int(input("ingrese la cantidad:"))
    alien = aliens(lista_aliens, num_aliens)
    
    print(lista_aliens) 
    imprimir_aliens(lista_aliens)
    alien.hit()
    print(alien.is_alive())

    for x in lista_aliens:
        
        x.teleport()
    imprimir_aliens(lista_aliens)
    total_aliens_created(lista_aliens)

if __name__ == "__main__":
    main()
    