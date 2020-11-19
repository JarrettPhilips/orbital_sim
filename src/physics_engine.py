import numpy as np


G = 6.67e-11 #gravitational constant

class Physics_Engine :
    mode = None #static or dynamicly calculated motion

    def __init__(self) :
        print()

    def calculate_craft_positions(self, craft, dt) :
        print('Calculating Position of', craft.name)

        #calculate barycenter between body and parent
        #barycenter = (body.mass*np.linalg.norm(body.position))/(body.mass + body.parent.mass)
        #print('Barycenter:', barycenter)

        #calculate gravitational force
        r = np.linalg.norm(craft.position)
        force = -G*(craft.mass * craft.governing_body.mass)/(r*r)
        force_vector = force*(craft.position / np.linalg.norm(craft.position))
        #print('force', force_vector)

        #calculate changes in velocity
        craft.velocity = np.array([craft.velocity[0] + (force_vector[0]*dt)/craft.mass, craft.velocity[1] + (force_vector[1]*dt)/craft.mass])
        #print('velocity', body.velocity)

        #update positions
        craft.position = np.array([craft.position[0] + craft.velocity[0]*dt, craft.position[1] + craft.velocity[1]*dt])
        #print('position', body.position)

    def calculate_celestrial_positions(self, body, dt) :
        print('Calculating Position of', body.name)

        if body.parent is not None :
            #calculate barycenter between body and parent
            barycenter = (body.mass*np.linalg.norm(body.position))/(body.mass + body.parent.mass)
            #print('Barycenter:', barycenter)

            #calculate gravitational force
            r = np.linalg.norm(body.position) - barycenter
            force = -G*(body.mass * body.parent.mass)/(r*r)
            force_vector = force*(body.position / np.linalg.norm(body.position))
            #print('force', force_vector)

            #calculate changes in velocity
            body.velocity = np.array([body.velocity[0] + (force_vector[0]*dt)/body.mass, body.velocity[1] + (force_vector[1]*dt)/body.mass])
            body.parent.velocity = np.array([body.parent.velocity[0] + (force_vector[0]*dt)/body.parent.mass, body.parent.velocity[1] + (force_vector[1]*dt)/body.parent.mass])
            #print('velocity', body.velocity)

            #update positions
            body.position = np.array([body.position[0] + body.velocity[0]*dt, body.position[1] + body.velocity[1]*dt])
            body.parent.position = np.array([body.parent.position[0] + body.parent.velocity[0]*dt, body.parent.position[1] + body.parent.velocity[1]*dt])
            #print('position', body.position)

        if body.children :

            for child in body.children :
                self.calculate_celestrial_positions(child, dt)
