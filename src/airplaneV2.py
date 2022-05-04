''' Created on Apr 29, 2015  @author: Yaser '''

import pygame as pg
pg.init()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = ( 100, 100, 100)
nc = (251, 205, 152)
display_width=800
display_height=600
MyGameDisplay = pg.display.set_mode((display_width,display_height))
pg.display.set_caption("Airplane")
my_clock= pg.time.Clock()
MyGameDisplay.fill(black)

pixArr = pg.PixelArray(MyGameDisplay)

for i in range(20):
    for j in range(20):
        print(i,j)
        pixArr[i][j]=green
        
pixArr[30][50] = blue

pg.draw.line(MyGameDisplay, grey, (0,100), (display_width,display_height), 5)

pg.draw.rect(MyGameDisplay,red, (200,200, 300,100), 10)
pg.draw.rect(MyGameDisplay,red, (400,400, 300,100))

pg.draw.circle(MyGameDisplay, nc, (500,100), 20)
pg.draw.circle(MyGameDisplay, nc, (500,150), 20, 5)

pg.draw.polygon(MyGameDisplay, green, ((50,50),(75,100),(150,350),(100,400),(600,200),(400,400)), 5)


gameLoop =True
while gameLoop:
    
    for event in pg.event.get():
        
        if event.type == pg.QUIT:
            pg.quit()
            quit()
            
        pg.display.update()
        