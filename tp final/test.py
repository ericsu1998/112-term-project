#Name: Eric Su #Andrew ID: esu1 

import pygame, os, copy

##################################################
##Marcher Class
##################################################

class Marcher(object):
    marchers = {} #all marchers in current set
    numOfMarchers = 0
    def __init__(self, x, y):
        Marcher.numOfMarchers += 1
        Marcher.marchers[Marcher.numOfMarchers] = (x,y)
        self.x = x
        self.y = y
    
    @staticmethod
    def clickedOnMarcher(x, y):
        for marcher in Marcher.marchers:
            marcherX, marcherY = Marcher.marchers[marcher]
            if (abs(marcherX - x) <= 10 and abs(marcherY - y) <= 10):#10,10 is radius of circle
                return marcher
        return None
        
##################################################
##Set Class
##################################################

class Set(object):
    allSets = []
    numberOfSets = 0
    def __init__(self, marchers):
        Set.numberOfSets += 1
        Set.allSets.append(marchers)
        self.marchers = marchers
    
    @staticmethod
    def deleteLastSet():
        if (Set.numberOfSets > 0):
            Set.numberOfSets -= 1
            Set.allSets.pop()
        
##################################################
##Button Class
##################################################

class Button(object):
    def __init__(self, screen, x, y, text, font, fontSize):
        self.x = x
        self.y = y
        self.text = text
        self.font = pygame.font.SysFont(font, fontSize, False, False)
        self.marginX = 13
        self.marginY = 13
        self.rectWidth = 100
        self.rectHeight = 50
        
    def drawText(self, screen, color):
        button = self.font.render(self.text, True, color)
        screen.blit(button, (self.x, self.y))
        
    def drawRectBorder(self, screen, color):
        marginX, marginY = 13, 13
        rectX, rectY = self.x-marginX, self.y-marginY
        rectWidth, rectHeight = 100, 50
        pygame.draw.rect(screen, color, 
                        (rectX, rectY, rectWidth,rectHeight))

    def hasClicked(self, pos):
        x,y = pos[0], pos[1]
        leftX = self.x - self.marginX
        rightX = leftX + self.rectWidth
        topY = self.y - self.marginY
        bottomY = topY + self.rectHeight
        return (x >= leftX and x <= rightX and y >= topY and y <= bottomY)

##################################################
##Main
##################################################

def march112(width = 640, height = 480):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    black = (0,0,0)
    white = (255,255,255)
    blue = (0,0,255)
    darkGreen = (75,175,75)
    currentScreen = 'homeScreen'
    createButton = Button(screen, width//2-width//20, height//5, 
                     'Create', 'Arial', 35)
    playButton = Button(screen, width//2-width//20, height//5*2, 
                     'Play', 'Arial', 35)
    helpButton = Button(screen, width//2-width//20, height//5*3, 
                     'Help', 'Arial', 35)
    newButton = Button(screen, width*3//5, height*11//12, 
                     'New', 'Arial', 35)
    deleteButton = Button(screen, width*5//6, height*11//12, 
                     'Delete', 'Arial', 35)
    runButton = Button(screen, width*5//6, height*11//12, 
                     'Run', 'Arial', 35)
    createFormationButton = Button(screen, width*5//6, height*1//12, 
                     'Form', 'Arial', 35)
    saveButton = Button(screen, width*3//5, height*11//12, 
                     'Save', 'Arial', 35)
    backButton = Button(screen, width//10, height *11//12, 
                    'Back', 'Arial', 35)
    formations = []
    formationNumber = 0
    marcherClicked = None
    
##################################################
##Home Screen 
##################################################

    def drawBackButton(surface):
        backButton.drawRectBorder(surface, darkGreen)
        backButton.drawText(surface, black)  
        
    def drawPlayButton(surface):
        playButton.drawRectBorder(surface, darkGreen)
        playButton.drawText(surface, black)        
    
    def drawCreateButton(surface):
        createButton.drawRectBorder(surface, darkGreen)
        createButton.drawText(surface, black)
    
    def drawHelpButton(surface):
        helpButton.drawRectBorder(surface, darkGreen)
        helpButton.drawText(surface, black)

    def drawButtons(surface):
        drawCreateButton(surface)
        drawPlayButton(surface)
        drawHelpButton(surface)
        
    def drawTitle(surface, text):
        titleScreen = pygame.Surface((325,30))
        titleScreen.fill(white)
        titleScreen = titleScreen.convert()
        screen.blit(titleScreen, (width//4, height//50))
        titleFont = pygame.font.SysFont('Arial', width//15, False, False)
        title = titleFont.render(text, True, black)
        titlePos = (width//4, height//50)
        screen.blit(title, titlePos)
        
    def drawHomeScreen():
        background = pygame.image.load(os.path.join("other files", 
                                                    "vanderbilt.jpg"))
        background.convert()
        drawTitle(background, 'Welcome to March 112!')
        drawButtons(background)
        screen.blit(background, (0,0))
    
    def homeScreenMousePressed(event):
        nonlocal currentScreen
        if (createButton.hasClicked(pygame.mouse.get_pos())): #go to All Sets
            currentScreen = 'allSets'
            drawAllSets(width, height)
        elif (playButton.hasClicked(pygame.mouse.get_pos())): #go to playScreen
            currentScreen = 'playScreen'
            drawPlayScreen(width, height)
        elif (helpButton.hasClicked(pygame.mouse.get_pos())): #go to helpScreen
            currentScreen = 'helpScreen'
            drawHelpScreen(width, height)
    
    def homeScreenKeyPressed(event):
        pass
        
##################################################
##Help Screen 
################################################## 

    def drawInstructions(surface):
        font = pygame.font.SysFont('Arial', 25, False, False)
        helpInstructions = 'Click to create Marchers'
        text = font.render(helpInstructions, True, black)
        surface.blit(text, (100,100))
        helpInstructions2 = 'To move a marcher, click the marcher you wish to move,'
        text2 = font.render(helpInstructions2, True, black)
        surface.blit(text2, (100,200))
        helpInstructions3 = 'then click the location you want to move the marcher to'
        text3 = font.render(helpInstructions3, True, black)
        surface.blit(text3, (100,250))

    def drawHelpScreen(width, height):
        helpScreen = pygame.Surface((width,height))
        helpScreen.fill(white)
        helpScreen = helpScreen.convert()
        drawBackButton(helpScreen)
        drawTitle(helpScreen, 'Need Help?')
        drawInstructions(helpScreen)
        screen.blit(helpScreen, (0,0))

    def helpScreenMousePressed(event):
        nonlocal currentScreen
        if (backButton.hasClicked(pygame.mouse.get_pos())): #go back to homeScreen
            currentScreen = 'homeScreen'
            drawHomeScreen() 
                   
    def helpScreenKeyPressed(event):
        pass
        
##################################################
##All Sets Screen 
################################################## 

    def drawSets(width, height):
        n = Set.numberOfSets
        rectWidth, rectHeight = width//5, height//5
        startingY = 50
        for set in range(n):
            rectX = (set%5)*rectWidth
            rectY = startingY + rectHeight * (set//5) #Limits 5 rects per Y range
            pygame.draw.rect(screen, black, 
                            (rectX, rectY, rectWidth, rectHeight), 1)
            for key in Set.allSets[set]:
                (x,y) = Set.allSets[set][key]
                drawDot(x/width*rectWidth + rectX, y/height*rectHeight + rectY, rectWidth) #shrinks dots inside rect
    
    def drawNewButton(width, height):
        newButton.drawRectBorder(screen, darkGreen)
        newButton.drawText(screen, black)     
        
    def drawDeleteButton(width, height):
        deleteButton.drawRectBorder(screen, darkGreen)
        deleteButton.drawText(screen, black)     
                   
    def drawAllSets(width, height):
        allSets = pygame.Surface((width,height))
        allSets.fill(white)
        allSets = allSets.convert()
        drawTitle(allSets, 'All Sets')
        drawSets(width, height)
        drawDeleteButton(width, height)
        drawNewButton(width, height)
        drawBackButton(allSets)
        screen.blit(allSets, (0,0))

    def allSetsMousePressed(event):
        nonlocal currentScreen
        if (newButton.hasClicked(pygame.mouse.get_pos())): #go to Set Screen
            currentScreen = 'setScreen'
            drawSetScreen(width, height) 
        elif (deleteButton.hasClicked(pygame.mouse.get_pos())): #delete last set
            Set.deleteLastSet()
            drawAllSets(width, height)
        elif (backButton.hasClicked(pygame.mouse.get_pos())): #go back to homeScreen
            currentScreen = 'homeScreen'
            drawHomeScreen()
                    
    def allSetsKeyPressed(event):
        pass
            
##################################################
##Set Screen 
################################################## 

    def drawFootBallField(width, height):
        # Create empty pygame surface.
        # Fill the background white color.
        background = pygame.Surface((width, height))
        background.fill(darkGreen) 
        currYard = 25
        pastFifty = 1
        numberOfLines = 11
        yardChange = 5
        for i in range(1, numberOfLines + 1):
            lineGap = width // (numberOfLines + 1)
            pygame.draw.line(background, white, (i*lineGap,0), #draws football field lines
                            ((i*lineGap,height))) 
            yardFontSize = 25
            font = pygame.font.SysFont('Calibri', yardFontSize, True, False)
            text = font.render(str(currYard),True, white)
            textMargin =  10
            textYMargin = 80
            background.blit(text, [i*lineGap-textMargin, height-textYMargin])
            if (pastFifty == 1): currYard += yardChange
            else: currYard -= yardChange 
            if (currYard == 50): pastFifty = -1 #makes yard decrease by 5 after 50 instead of increasing by 5
        # Convert Surface object to make blitting faster.
        background = background.convert()
        # Copy background to screen (position (0, 0) is upper left corner).
        screen.blit(background, (0,0))
        
    def drawMarchers(marchers):
        for key in marchers:
            x,y = marchers[key]
            drawMarcher(x,y)

    def drawMarcher(x, y):
        diameter = 20
        march = pygame.Surface((diameter,diameter))
        pygame.draw.circle(march, white, 
                          (diameter//2,diameter//2), diameter//2)
        march = march.convert()
        march.set_colorkey(black)
        march = march.convert_alpha()
        screen.blit(march, (x-diameter//2,y-diameter//2))   

    def drawCreateFormationButton(width, height):
        createFormationButton.drawRectBorder(screen, white)
        createFormationButton.drawText(screen, black)
        
    def drawSetScreen(width, height):
        drawFootBallField(width, height)
        drawMarchers(Marcher.marchers)
        drawCreateFormationButton(width, height)
        drawSaveButton(width, height)
        drawDeleteButton(width, height)
        
    def setScreenMousePressed(event):
        nonlocal currentScreen, marcherClicked
        if (saveButton.hasClicked(pygame.mouse.get_pos())): #save set
            marchers = copy.copy(Marcher.marchers)
            set = Set(marchers)
            currentScreen = 'allSets'
            drawAllSets(width, height)
        elif (deleteButton.hasClicked(pygame.mouse.get_pos())): #delete set
            currentScreen = 'allSets'
            drawAllSets(width, height)  
        elif (createFormationButton.hasClicked(pygame.mouse.get_pos())): #go to formations screen
            currentScreen = 'formationsScreen'
            drawFormationsScreen(width, height)  
        else:
            (x,y) = pygame.mouse.get_pos()
            marcher = Marcher.clickedOnMarcher(x,y)
            if (marcher != None): #clicked on marcher
                marcherClicked = marcher
            else:
                #did not click on marcher
                if (marcherClicked != None):
                    #moves marcher from previous location to location clicked
                    del Marcher.marchers[marcherClicked]
                    Marcher.marchers[marcherClicked] = (x,y)
                    drawSetScreen(width, height)
                else: 
                    #no marcher highlighted already
                    (marcherX, marcherY) = pygame.mouse.get_pos()
                    marcher = Marcher(marcherX, marcherY)
                    drawMarcher(marcherX, marcherY) 
                marcherClicked = None
            
    def setScreenKeyPressed(event):
        pass

##################################################
##Formations Screen 
##################################################

    def drawFormations(width, height):
        n = len(formations)
        rectWidth, rectHeight = width//5, height//5
        startingY = 50
        for formation in range(n):
            rectX = (formation%5)*rectWidth
            rectY = startingY + rectHeight * (formation//5)
            pygame.draw.rect(screen, black, 
                            (rectX, rectY, rectWidth, rectHeight), 1)
            for dot in range(len(formations[formation])):
                (x,y) = formations[formation][dot]
                drawDot(x*rectWidth + rectX, y*rectHeight + rectY, rectWidth)

    def drawFormationsScreen(width, height):
        formationsScreen = pygame.Surface((width,height))
        formationsScreen.fill(white)
        formationsScreen = formationsScreen.convert()
        drawTitle(formationsScreen, 'Formations Screen')
        drawFormations(width, height)
        drawNewButton(width, height)
        drawDeleteButton(width, height)
        drawBackButton(formationsScreen)
        screen.blit(formationsScreen, (0,0))
        
    def formationsScreenMousePressed(event):
        nonlocal formationNumber, currentScreen
        if (newButton.hasClicked(pygame.mouse.get_pos())): #creates formation and adds to formationList
            currentScreen = 'createFormation'
            formations.append([])
            formationNumber += 1
            drawCreateFormation(width, height)
        elif (deleteButton.hasClicked(pygame.mouse.get_pos())): #deletes last formation
            if (formationNumber > 0):
                formations.pop(formationNumber-1)
                formationNumber -= 1
                currentScreen = 'formationsScreen' #TODO: delete formation without drawing new screen
                drawFormationsScreen(width, height) 
        elif (backButton.hasClicked(pygame.mouse.get_pos())): #TODO: should it go back to allSets??? #goes back to setScreen 
            currentScreen = 'setScreen'
            drawSetScreen(width, height)             
        
    def formationsScreenKeyPressed(event):
        pass

##################################################
##Create Formation Screen 
##################################################

    def drawSaveButton(width, height):
        saveButton.drawRectBorder(screen, darkGreen)
        saveButton.drawText(screen, black)
        
    def drawCreateFormation(width, height):
        formations = pygame.Surface((width,height))
        formations.fill(white)
        formations = formations.convert()
        drawTitle(formations, 'Create formation')
        drawDeleteButton(width, height)
        drawSaveButton(width, height)
        screen.blit(formations, (0,0))
    
    def addDot(x, y): #TODO: maybe make dot class?
        nonlocal formationNumber
        i = formationNumber - 1
        formations[i].append((x/width,y/height))
        
    def drawDot(x, y, size):
        diameter = size//25
        dot = pygame.Surface((diameter,diameter))
        pygame.draw.circle(dot,blue, (diameter//2,diameter//2), diameter//2)
        dot = dot.convert()
        dot.set_colorkey(black)
        dot = dot.convert_alpha()
        screen.blit(dot, (x-diameter//2,y-diameter//2))      

    def createFormationMousePressed(event): #creates a dot
        nonlocal formationNumber, currentScreen
        if (saveButton.hasClicked(pygame.mouse.get_pos())): #saves formation
            currentScreen = 'formationsScreen'
            drawFormationsScreen(width, height)
        elif (deleteButton.hasClicked(pygame.mouse.get_pos())): #deletes formation
            formations.pop(formationNumber-1)
            formationNumber -= 1
            currentScreen = 'formationsScreen'
            drawFormationsScreen(width, height) 
        else:
            (dotX, dotY) = pygame.mouse.get_pos() #creates a dot in formation
            addDot(dotX, dotY)
            drawDot(dotX, dotY, width) 
                
    def createFormationKeyPressed(event):
        nonlocal formationNumber, currentScreen
        if (chr(event.key) == 's'): #saves formation
            currentScreen = 'formationsScreen'
            drawFormationsScreen(width, height)
        elif (chr(event.key) == 'd'): #deletes formation
            formations.pop(formationNumber-1)
            formationNumber -= 1
            currentScreen = 'formationsScreen'
            drawFormationsScreen(width, height) 
        elif (chr(event.key) == 'c'): #TODO: implement or not? (removes all dots) #clear formation
            pass

##################################################
##Play Screen
##################################################   
    
    def findDifferences(marchers, currSet):
        diff = {}
        for key in Set.allSets[currSet]:
            xDiff = Set.allSets[currSet][key][0] - marchers[key][0]
            yDiff = Set.allSets[currSet][key][1] - marchers[key][1]
            diff[key] = (xDiff, yDiff)
        return diff
    
    def targetReached(marchers, currSet):
        epsilon = 10**-2
        diffs = findDifferences(marchers, currSet)
        for key in Set.allSets[currSet]:
            if (abs(diffs[key][0]) > epsilon and abs(diffs[key][1]) > epsilon): #if close enough to next dot
                return False
        return True
        
    def runPlayScreen():
        if (Set.numberOfSets == 0): return
        startMarchers = copy.copy(Set.allSets[0]) #dots that will be going from set to set
        drawMarchers(startMarchers)
        diffs = dict()
        for n in range(1, Set.numberOfSets):
            for key in Set.allSets[n]:
                diffs[key] = (findDifferences(startMarchers, n)[key][0]/100, findDifferences(startMarchers, n)[key][1]/100) 
            while (not targetReached(startMarchers,n)):
                pygame.display.flip()
                pygame.time.delay(10) #allows for smooth transition
                for key in startMarchers:
                    startMarchers[key] = (startMarchers[key][0] + diffs[key][0], startMarchers[key][1] + diffs[key][1]) #increments slowly
                drawFootBallField(width, height) #TODO: do stuff without drawing new field
                drawMarchers(startMarchers)
            n+=1
        drawRunButton(width, height)
        drawBackButton(width, height)   
         
    def drawRunButton(width, height):
        runButton.drawRectBorder(screen, white)
        runButton.drawText(screen, black)
        
    def drawPlayScreen(width, height):
        playScreen = pygame.Surface((width, height))
        drawFootBallField(width, height)
        drawRunButton(width, height)
        drawBackButton(playScreen)
        screen.blit(playScreen, (0,0))
        
    def playScreenMousePressed(event):
        nonlocal currentScreen
        if (runButton.hasClicked(pygame.mouse.get_pos())):
            runPlayScreen()
        elif (backButton.hasClicked(pygame.mouse.get_pos())):  
            currentScreen = 'homeScreen'
            drawHomeScreen() 
            
    def playScreenKeyPressed(event):
        pass
        
##################################################
##Mouse and Key Events
##################################################      
        
    def mousePressed(event):
        nonlocal currentScreen
        if (currentScreen == 'homeScreen'):
            homeScreenMousePressed(event)
        elif (currentScreen == 'allSets'):
            allSetsMousePressed(event)
        elif (currentScreen == 'setScreen'):
            setScreenMousePressed(event)
        elif(currentScreen == 'formationsScreen'):
            formationsScreenMousePressed(event)
        elif (currentScreen == 'createFormation'):
            createFormationMousePressed(event)
        elif (currentScreen == 'playScreen'):
            playScreenMousePressed(event)
        elif (currentScreen == 'helpScreen'):
            helpScreenMousePressed(event)
            
    def keyPressed(event):
        nonlocal currentScreen, formationNumber
        if (currentScreen == 'homeScreen'):
            homeScreenKeyPressed(event)
        elif (currentScreen == 'allSets'):
            allSetsKeyPressed(event)
        elif (currentScreen == 'setScreen'):
            setScreenKeyPressed(event)
        elif (currentScreen == 'formationsScreen'):
            formationsScreenKeyPressed(event)
        elif (currentScreen == 'createFormation'):
            createFormationKeyPressed(event)
        elif (currentScreen == 'playScreen'):
            playScreenKeyPressed(event)
        elif (currentScreen == 'helpScreen'):
            helpScreenKeyPressed(event)
            
##################################################
##Run 
##################################################
 
    drawHomeScreen()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousePressed(event)                   
            elif event.type == pygame.KEYDOWN: 
                keyPressed(event)
                
        pygame.display.flip()

    pygame.quit()

march112()