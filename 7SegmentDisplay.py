import pygame 



window_w, window_h = 800, 600
white = (255, 255, 255)
red = (255, 0, 0)



screen = pygame.display.set_mode((window_w, window_h))
pygame.display.set_caption("Led Display")
clock = pygame.time.Clock()

# Segments which need to be activated to display the number, in order oif segments(a, b, c, d, e, f, g)

ledList = {
    "0" : (1, 1, 1, 1, 1, 1, 0),
    "1" : (0, 1, 1, 0, 0, 0, 0),
    "2" : (1, 1, 0, 1, 1, 0, 1),
    "3" : (1, 1, 1, 1, 0, 0, 1),
    "4" : (0, 1, 1, 0, 0, 1, 1),
    "5" : (1, 0, 1, 1, 0, 1, 1),
    "6" : (1, 0, 1, 1, 1, 1, 1),
    "7" : (1, 1, 1, 0, 0, 0, 0),
    "8" : (1, 1, 1, 1, 1, 1, 1),
    "9" : (1, 1, 1, 0, 0, 1, 1)

}
# reference point to draw each number (i think its the most top left pixel of the number)
referencePoint_0 = (100, 240)
referencePoint_1 = (330, 240)
referencePoint_2 = (560, 240)


def drawNumber(number, color, pos):

    target = ledList[number]


    if pos == 0:
        cPoint = referencePoint_0
    elif pos == 1:
        cPoint = referencePoint_1
    else:
        cPoint = referencePoint_2

    # draw each segment(7 in total)
    if target[0] == 1:
        drawRecth(cPoint[0]+30, cPoint[1], color) # a 
    if target[1] == 1:
        drawRectv(cPoint[0]+90, cPoint[1]+30, color) # b    
    if target[2] == 1:
        drawRectv(cPoint[0]+90, cPoint[1]+120, color) # e
    if target[3] == 1:
        drawRecth(cPoint[0]+30, cPoint[1]+180, color) # d
    if target[4] == 1:
        drawRectv(cPoint[0], cPoint[1]+120, color) # c
    if target[5] == 1:
        drawRectv(cPoint[0], cPoint[1]+30, color) # f
    if target[6] == 1:
        drawRecth(cPoint[0]+30, cPoint[1]+90, color) # g


# draw a vertical segment
def drawRectv(posx, posy, color):
    pygame.draw.rect(screen, color, (posx, posy, 20, 50))

    pygame.draw.line(screen, color, (posx+5, posy), (posx+10, posy-10), width=9)
    pygame.draw.line(screen, color, (posx+15, posy), (posx+10, posy-10), width=9)
    pygame.draw.rect(screen, color, (posx+8, posy-5, 5, 5))

    pygame.draw.line(screen, color, (posx+5, posy+50), (posx+10, posy+60), width=9)
    pygame.draw.line(screen, color, (posx+15, posy+50), (posx+10, posy+60), width=9)
    pygame.draw.rect(screen, color, (posx+8, posy+50, 5, 5))

    pygame.display.update()
#draw a horizontal segment
def drawRecth(posx, posy, color):
    pygame.draw.rect(screen, color, (posx, posy, 50, 20))

    pygame.draw.line(screen, color, (posx, posy+5), (posx-10, posy+10), width=9)
    pygame.draw.line(screen, color, (posx, posy+15), (posx-10, posy+10), width=9)
    pygame.draw.rect(screen, color, (posx-5, posy+8, 5, 5))

    pygame.draw.line(screen, color, (posx+50, posy+5), (posx+60, posy+10), width=9)
    pygame.draw.line(screen, color, (posx+50, posy+15), (posx+60, posy+10), width=9)
    pygame.draw.rect(screen, color, (posx+50, posy+8, 5, 5))

    pygame.display.update()

userInput = 369          # 3 digit number to show in screen
formated_user_input = ("{:03d}".format(userInput))

finished = False
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    
    for i in range(3):
        info = str(formated_user_input[i])
        drawNumber(info, white, i)

    pygame.display.update()
    clock.tick_busy_loop(20)

