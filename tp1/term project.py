#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
002_display_fps.py

Open a Pygame window and display framerate.
Program terminates by pressing the ESCAPE-Key.
 
works with python2.7 and python3.4 

URL    : http://thepythongamebook.com/en:part2:pygame:step002
Author : horst.jens@spielend-programmieren.at
License: GPL, see http://www.gnu.org/licenses/gpl.html
"""

import pygame

class Marcher(object):
    marchers = []
    def __init__(self, x, y):
        Marcher.marchers.append((x, y))
        print(Marcher.marchers)
        self.x = x
        self.y = y
    
# Initialize Pygame.
def main(width = 640, height = 480):
    pygame.init()
    screen = pygame.display.set_mode((width,height))
    background = pygame.Surface(screen.get_size())
    white = (255,255,255)
    darkGreen = (75,175,75)

    def drawFootBallField(background, width, height):
        # Create empty pygame surface.
        # Fill the background white color.
        background.fill(darkGreen) 
        currYard = 25
        pastFifty = 1
        numberOfLines = 11
        yardChange = 5
        for i in range(1, numberOfLines + 1):
            lineGap = width // (numberOfLines + 1)
            pygame.draw.line(background, white, (i*lineGap,0), 
                            ((i*lineGap,height)))
            yardFontSize = 25
            font = pygame.font.SysFont('Calibri', yardFontSize, True, False)
            text = font.render(str(currYard),True, white)
            textMargin = 10
            textYMargin = 80
            background.blit(text, [i*lineGap-textMargin, height-textYMargin])
            if (pastFifty == 1): currYard += yardChange
            else: currYard -= yardChange 
            if (currYard == 50): pastFifty = -1
        # Convert Surface object to make blitting faster.
        background = background.convert()
        # Copy background to screen (position (0, 0) is upper left corner).
        screen.blit(background, (0,0))
        
    def drawMarcher(x, y):
        march = pygame.Surface((50,50))
        pygame.draw.circle(march, (255,255,255), (25,25), 25)
        march = march.convert()
        march.set_colorkey((0,0,0))
        march = march.convert_alpha()
        screen.blit(march, (x-25,y-25))
        
    drawFootBallField(background, width, height)
    # Create Pygame clock object.  
    clock = pygame.time.Clock()

    mainloop = True

    while mainloop:        
        for event in pygame.event.get():
            # User presses QUIT-button.
            if event.type == pygame.QUIT:
                mainloop = False 
            elif event.type == pygame.KEYDOWN:
                # User presses ESCAPE-Key
                if event.key == pygame.K_ESCAPE:
                    mainloop = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (marcherX, marcherY) = pygame.mouse.get_pos()
                marcher = Marcher(marcherX, marcherY)
                drawMarcher(marcherX, marcherY)
        #Update Pygame display.
        pygame.display.flip()

    # Finish Pygame.  
    pygame.quit()

main()