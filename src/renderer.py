import pygame
import numpy as np

class Renderer :
    SCALE = 0.000001 #multiplier, <1 for making things smaller
    FRAME_RESOLUTION = [0,0]

    screen = None

    def __init__(self, X_RES, Y_RES, SCALE) :
        pygame.init()
        self.FRAME_RESOLUTION = [X_RES, Y_RES]
        self.SCALE = SCALE
        self.screen = pygame.display.set_mode(self.FRAME_RESOLUTION)
        self.screen.fill((0, 0, 0))
        pygame.display.update()

    def produce_frame(self, body) :
        if body.parent is not None :
            x_pixel = (body.parent.position[0] + body.position[0])*self.SCALE + self.FRAME_RESOLUTION[0]/2
            y_pixel = (body.parent.position[1] + body.position[1])*self.SCALE + self.FRAME_RESOLUTION[1]/2
        else :
            x_pixel = body.position[0]*self.SCALE + self.FRAME_RESOLUTION[0]/2
            y_pixel = body.position[1]*self.SCALE + self.FRAME_RESOLUTION[1]/2

        print('Rendering', body.name, 'at\t\t', '{:>4}'.format(x_pixel), '{:>4}'.format(y_pixel))
        pygame.draw.circle(self.screen, (255, 255, 255), (x_pixel, y_pixel), body.radius*self.SCALE, 3)

        if body.children :
            for child in body.children :
                self.produce_frame(child)

        pygame.display.update()

    def render_craft(self, list_of_craft) :
        if list_of_craft :
            for craft in list_of_craft :
                x_pixel = (craft.governing_body.position[0] + craft.position[0])*self.SCALE + self.FRAME_RESOLUTION[0]/2
                y_pixel = (craft.governing_body.position[1] + craft.position[1])*self.SCALE + self.FRAME_RESOLUTION[1]/2
                print('Rendering', craft.name, 'at\t\t', '{:>4}'.format(x_pixel), '{:>4}'.format(y_pixel))
                pygame.draw.circle(self.screen, (0, 255, 0), (x_pixel, y_pixel), 1, 3)
