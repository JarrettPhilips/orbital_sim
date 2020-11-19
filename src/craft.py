import numpy as np

class Craft :

    name = None
    mass = 0 #kg
    orientation = 0 #bearing (0-359)
    velocity = np.array([0,0])

    governing_body = None

    position = np.array([0,0])

    def __init__(self) :
        print()

    def burn(self, orientation, deltaV) :
        print()

    def check_for_transfer(self) :
        print()

    def transfer_governing_body(self) :
        print()
