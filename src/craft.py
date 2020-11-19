import numpy as np

class Craft :
    name = None
    mass = 0 #kg
    governing_body = None

    position = np.array([0,0])
    velocity = np.array([0,0])


    def __init__(self) :
        print()

    def burn(self, velocity_unit_vector, deltaV) :
        print()

    def simple_burn(self, deltaV) : #accelerates / deaccelerates using the existing direction of travel
        print('Burning:', deltaV, 'deltaV')
        burn_vector = deltaV*(self.velocity / np.linalg.norm(self.velocity))
        self.velocity = self.velocity + burn_vector

    def check_for_transfer(self) :
        print()

    def transfer_governing_body(self) :
        print()
