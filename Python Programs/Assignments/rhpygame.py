# Robert Karg - 10145986
# Assignment 4: rushhour game - (pygame version)
import pygame, random, time
from rushhour2 import CarGame

# my Gui class
class GuiGame:
    # using CarGame class from the text version to setup some variables for the class
    grid = CarGame.grid
    carList = CarGame.carNumList
    rand = random.Random()
    # colors for the cars
    COLORS = [(0, 255, 0), (0, 0, 255), (192, 192, 192,), (255, 255, 0), (102,0,204),
                    (255,0,255), (255, 128, 0), (0,255, 255), (0,153, 0), (0, 0, 153),
                    (76, 0 ,153), (255,0,127), (255,153,255)]
    rand.shuffle(COLORS) # so they are more random
    RED =(255,0,0) # for the object car
    color = 0

    # this function uses the CarGame objects tocreate rectangles representing
    # each car
    @classmethod
    def addCars(cls):
        for i in range(CarGame.numCars):
            self  = cls.carList[i]
            x = self.column * 100
            y = self.row * 100
            if self.orient == 'h':
                height = 100
                if self.carLength == 2:
                    width = 200
                else:
                    width = 300
            else:
                width = 100
                if self.carLength == 2:
                    height = 200
                else:
                    height = 300
            if self.car == 1:
                randColor = cls.RED
            else:
                randColor = cls.COLORS[cls.color]
                cls.color +=1
            self.rectangle = pygame.draw.rect(screen, randColor, (x, y, width, height))
            self.color = randColor

    # this function draws the rectangles as they change
    @classmethod
    def drawRects(cls):
        for i in range(len(cls.carList)):
            obj = cls.carList[i]
            pygame.draw.rect(screen, obj.color, obj.rectangle)

    # this function checks if the object car passed the edge of the grid
    # if so it draws a win screen
    @classmethod
    def checkWinner(cls, screen):
        if cls.carList[0].rectangle.x > WIDTH - 200:
            font = pygame.font.Font(None, 100)
            message = font.render("You Win!", True, BLACK)
            messageRect = message.get_rect(center =(WIDTH/2, HEIGHT/2))
            screen.blit(message, messageRect)
            pygame.display.update()
            time.sleep(3)
            return True
        else:
            return False


### constants ###
LINE_WIDTH = 3
RECT_WIDTH = 5
WIDTH = 600
HEIGHT = 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# setting up the game
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Rush Hour')
clock = pygame.time.Clock()
screen.fill(WHITE)

# draws the grid that will be in the background
for i in range(100, 600, 100):
    pygame.draw.line(screen, BLACK, (i, 0), (i, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (0, i), (WIDTH, i), LINE_WIDTH)
# huge rectangle around the whole screen
pygame.draw.rect(screen, BLACK, (0,0,WIDTH, HEIGHT), RECT_WIDTH)
GuiGame.addCars() # adds the cars
# to be used down below:
rectangle = None
rectangleDrag = False
won = False
# loop for the game
while not won:
    dy, dx, temp = 0, 0, 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if (event.type == pygame.MOUSEBUTTONDOWN and event.button ==1):
            for i in range(len(GuiGame.carList)):
                rectangle = GuiGame.carList[i].rectangle
                if rectangle.collidepoint(event.pos) == True:
                    rectangleDrag = True # to let the player drag the rectangles
                    mouseX, mouseY = event.pos
                    xOffset = rectangle.x - mouseX
                    yOffset = rectangle.y - mouseY
                    break
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                rectangleDrag = False
        # moves the rectangles while checking the boundaries
        # if rectangleDrag is True
        elif event.type == pygame.MOUSEMOTION:
                if rectangleDrag == True:
                    mouseX, mouseY = event.pos
                    if rectangle.height > 100:
                        temp = rectangle.y
                        rectangle.y = mouseY + yOffset
                        dy = rectangle.y - temp
                        if rectangle.y + rectangle.height > HEIGHT:
                            rectangle.y = HEIGHT - rectangle.height
                        elif rectangle.y < 0:
                            rectangle.y = 0
                        else:
                            carList = GuiGame.carList
                            for i in range(len(carList)):
                                rect2 = carList[i].rectangle
                                if rect2 == rectangle:
                                    continue
                                else:
                                    if rectangle.colliderect(rect2) == True:
                                        if dy < 0:
                                            rectangle.y = rect2.height + rect2.y
                                        elif dy > 0:
                                            rectangle.y = rect2.y - rectangle.height
                                        rectangleDrag = False

                    else:
                        temp = rectangle.x
                        rectangle.x = mouseX + xOffset
                        dx = rectangle.x - temp
                        if rectangle.x +rectangle.width > WIDTH:
                            if rectangle == GuiGame.carList[0].rectangle:
                                continue
                            rectangle.x = WIDTH - rectangle.width
                        elif rectangle.x <0:
                            rectangle.x = 0
                        else:
                            carList = GuiGame.carList
                            for i in range(len(carList)):
                                rect2 = carList[i].rectangle
                                if rect2 == rectangle:
                                    continue
                                else:
                                    if rectangle.colliderect(rect2) == True:
                                        if dx < 0:
                                            rectangle.x = rect2.width +rect2.x
                                        elif dx > 0:
                                            rectangle.x = rect2.x - rectangle.width
                                        rectangleDrag = False
    # updating the screen each time
    screen.fill(WHITE)
    for i in range(100, 600, 100):
        pygame.draw.line(screen, BLACK, (i, 0), (i, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, BLACK, (0, i), (WIDTH, i), LINE_WIDTH)
    pygame.draw.rect(screen, BLACK, (0,0,WIDTH, HEIGHT), RECT_WIDTH)
    GuiGame.drawRects()
    won = GuiGame.checkWinner(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
