''' Created on Apr 28, 2015 @author: Yaser '''
import time
import pygame
import random
pygame.init()

# color = ( R , G , B )
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = ( 100, 100, 100)
nc = (251, 205, 152)
bl_color=(234,23,123)

display_width=800
display_height=600
MyGameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("Airplane")

my_clock= pygame.time.Clock()

airplane_main=pygame.image.load('mainAirplane.png')
airplane_main_width = 110
airplane_main_height = 115


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged : "+ str(count), True, black)
    MyGameDisplay.blit(text,(0,0))

def thing(thingX,thingY,thingW,thingH,thingC):
    pygame.draw.rect(MyGameDisplay, thingC, [thingX,thingY,thingW,thingH])
    
    
def car(x,y):
    MyGameDisplay.blit(airplane_main,(x,y))
    
def crash():
    message_display('CRASHED')
    time.sleep(1) # 2 sec
    game_loop()

def gameIntro():
    intro=True
    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.KEYDOWN:
                intro= False
            
            if event.type == pygame.QUIT:
                close_game()
            
        MyGameDisplay.fill(white)
        message_display('Start')
        message_display('Press Any Key to Start', 50, (display_width/2, display_height/2 + 100))
        
        pygame.draw.rect(MyGameDisplay, green, (150,450,100,50))
        pygame.draw.rect(MyGameDisplay, red, (550,450,100,50))
        pygame.display.update()
        my_clock.tick(2)
        
def text_objects(text,text_d):
    text_surface = text_d.render(text, True, black)
    return text_surface, text_surface.get_rect()
         
def message_display(text,textSize=115,Pos=((display_width/2),(display_height/2))):
    text_d = pygame.font.Font("freesansbold.ttf",textSize)
    TextSurf,TextRect = text_objects(text,text_d)
    TextRect.center = (Pos)
    MyGameDisplay.blit(TextSurf,TextRect)
    
    pygame.display.update()
    
    
   
def close_game():
    pygame.quit()
    quit()



def game_loop():
    fps=60
    crashed = False
    gameExit = False
    pl_x=((display_width - airplane_main_width) * 0.5 )
    pl_y=(display_height - airplane_main_height )
    
    x_change = 0
    y_change = 0
    change = 5
    # new thing parameter
    thing_x = random.randrange(0,display_width)
    thing_y = -600
    thing_speed= 5
    thing_width=100
    thing_height=100
    
    dodged=0
    
    while not gameExit:
        
        
        for event in pygame.event.get():
            # extra key options
            if event.type == pygame.QUIT:
                close_game()
            # x-axix
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -change
                if event.key == pygame.K_RIGHT:
                    x_change = change
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change=0    
            
            # Y-axis            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -change
                if event.key == pygame.K_DOWN:
                    y_change = change
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change=0  
                    
        # display things in MyGameDisplay
        #display screen and fill it with color
        MyGameDisplay.fill(nc)
        # plane new x and y
        pl_y += y_change        
        pl_x += x_change 
        # display plane       
        car(pl_x, pl_y)
        
        things_dodged(dodged)
        
        # display thing 
        thing(thing_x, thing_y, thing_width, thing_height, bl_color)
        # change the position of the thing 
        thing_y += thing_speed
        
        
        # game logic : 
        
        if pl_x > display_width - airplane_main_width or pl_x < 0 :
            #crashed = True
            crash()
            
        if pl_y > display_height - airplane_main_height or pl_y < 0:
            #crashed = True
            crash()
        #if crashed:
            #crash()
            #crashed=False
            #pl_x=((display_width - airplane_main_width) * 0.5 )
            #pl_y=(display_height - airplane_main_height )
            
            #gameExit = True
            #pl_x=((display_width - airplane_main_width) * 0.5 )
            #pl_y=((display_height - airplane_main_height ) * 0.5)
         
        if thing_y > display_height:
            thing_y = -thing_height
            thing_x = random.randrange(0,display_width-thing_width) 
            dodged +=1
            thing_speed +=1
            thing_width += (dodged * 2)   
        
        if pl_y < thing_y + thing_height:
            if pl_x > thing_x and pl_x < thing_x+thing_width or pl_x+airplane_main_width>thing_x  and pl_x+airplane_main_width<thing_x+thing_width:
                crash()
                    
          
        pygame.display.update()
        my_clock.tick(fps)
        
        #crashed= False
 

 
gameIntro() 
game_loop()
    






