import numpy as np

class Body :
    name = None
    mass = 0 #kg
    radius = 0 #m
    parent = None
    children = []

    position = np.array([0,0])
    velocity = np.array([0,0])

    def __init__(self, name, parent, mass, radius) :
        self.name = name
        self.parent = parent
        self.mass = mass
        self.radius = radius

    def set_parent(self, parent, parent_distance) :
        self.parent = parent
        self.parent_distance = parent_distance
