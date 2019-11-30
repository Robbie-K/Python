import pygame

pygame.init()


def checkGrid(screen, pos):
    black = 0,0,0
    row = int(pos[0] / 100)
    col = int(pos[1]/ 100)
    return(row, col)

def drawShape(screen, pos):
    row = pos[0]
    col = pos[1]
    point = (row*100+50, col*100+50) # center of the cell
    pygame.draw.circle(screen, black, point, 40, 3)
width = 306
height = 306

grey = (220, 220, 220)
black = (0, 0, 0)
screen = pygame.display.set_mode((width, height))
screen.fill(grey)

pygame.display.set_caption('Tic Tac Toe')
pygame.draw.line(screen, black, (100,0), (100, 300), 3)
pygame.draw.line(screen, black, (200,0), (200, 300), 3)
pygame.draw.line(screen, black, (0,100), (300, 100), 3)
pygame.draw.line(screen, black, (0,200), (300, 200), 3)
pygame.display.flip()

won = False
while won == False:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            won = True
        if (ev.type == pygame.MOUSEBUTTONDOWN and ev.button ==1):
            print(ev.pos)
            print(checkGrid(screen, ev.pos))



    pygame.display.update()
