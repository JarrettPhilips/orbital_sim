import time
from time import sleep

import numpy as np
import pygame

import renderer
import physics_engine
import body
import craft

#celestrial objects
earth = body.Body('Earth', None, 5.972e24, 6.371e6)
'''
moon = body.Body('Moon', earth, 7.348e22, 1.737e6)
moon.position = np.array([384e6, 0])
moon.velocity = np.array([0, -1000]) #not a real life number
earth.velocity = np.array([0, -12.4]) #earth's initial velocity should be ~1.24% of the moons (ratio of mass)
earth.children = [moon]
'''

#secret_moon = body.Body('Secret Moon', earth, 0, 1.7*MILLION)
#secret_moon.position = [-384*MILLION, 0]
#space_debris = body.Body('Space Debris', moon, 0, 0.5*MILLION)
#earth.children = [moon, secret_moon]
#moon.children = [space_debris]

center_body = earth

#artifical objects
spaceboat = craft.Craft()
spaceboat.name = 'Space Boat'
spaceboat.mass = 22700
spaceboat.governing_body = earth
spaceboat.position = np.array([8.371e6, 0])
spaceboat.velocity = np.array([0, 6850]) #6850 seems relatively stable at LEO

list_of_craft = [spaceboat]


#primary simulation components
renderer = renderer.Renderer(800, 800, 0.00001)
physics_engine = physics_engine.Physics_Engine()

#main loop
running = True

#program loop runtime
i = 0
maintain_constant_step_time = True #useful for humans
step_time = 100 #ms

#simulated time
t = 0
dt = 100

while running :
    i += 1
    start_time = time.time()*1000
    print('Iteration:', i, 'Time:', t)
    t = t + dt

    #check for control input
    events = pygame.event.get()
    for event in events :
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP :
                spaceboat.simple_burn(100)
            if event.key == pygame.K_DOWN :
                spaceboat.simple_burn(-100)

    physics_engine.calculate_celestrial_positions(center_body, dt)
    physics_engine.calculate_craft_positions(spaceboat, dt)
    renderer.produce_frame(center_body)
    renderer.render_craft(list_of_craft)


    if maintain_constant_step_time :
        end_time = time.time()*1000
        time_elapsed = end_time - start_time
        if time_elapsed > step_time :
            print("step time exceeded")
        else :
            sleep((step_time-time_elapsed)/1000)
