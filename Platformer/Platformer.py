import pygame
pygame.init()  
pygame.display.set_caption("easy platformer")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

Link = pygame.image.load('dude1.png') #load your spritesheet
Link.set_colorkey((255, 255, 255)) #this makes bright pink (255, 0, 255) transparent (sort of)



class platform:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
    def draw(self):
        pygame.draw.rect(screen, (200, 0, 100), (self.xpos, self.ypos, 100, 20))
    def collide(self,x ,y):
        if x+20>self.xpos and x<self.xpos+50 and y+16> self.ypos and y < self.ypos+20:
            return true
      
p1 = platform(100,750)
p2 = platform(200,650)
p3 = platform(300,550)
p4 = platform(400,450)
p5 = platform(600,350)
p6 = platform(700,250)
p7 = platform(800,150)
p8 = platform(300,250)
#CONSTANTS
LEFT=0
RIGHT=1
UP = 2
DOWN = 3



#player variables
xpos = 500 #xpos of player
ypos = 200 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
keys = [False, False, False, False] #this list holds whether each key has been pressed
isOnGround = False #this variable stops gravity from pulling you down more when on a platform

frameWidth = 16
frameHeight = 16
RowNum = 1 #for left animation, this will need to change for other animations
frameNum = 0
ticker = 0

controller = pygame.joystick.Joystick(0) 
controller.init()


jump = pygame.mixer.Sound('jump.wav')
music = pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(-1)


map =  [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]


while not gameover: #GAME LOOP############################################################
    clock.tick(100) #FPS
   
    #Input Section------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
      
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True

            elif event.key == pygame.K_UP:
                keys[UP]=True
                
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=True
            
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False

            elif event.key == pygame.K_UP:
                keys[UP]=False

            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=False
               
    #physics section--------------------------------------------------------------------
    #LEFT MOVEMENT
    if keys[LEFT]==True:
        vx=-3
        direction = LEFT
    
    elif keys[RIGHT]==True:
        vx=3
        direction = RIGHT
    #turn off velocity
    else:
        vx*=.99
        #JUMPING
    if keys[UP] == True and isOnGround == True: #only jump when on the ground
        vy = -8
        isOnGround = False
        direction = UP
        pygame.mixer.Sound.play(jump)
        
    xVel = controller.get_axis(0) #returns a number b/t -1 and 1
    yVel = controller.get_axis(1) #returns a number b/t -1 and 1
    

    xpos += int(xVel * 10)
    ypos += int(yVel * 10)
   

   
    #COLLISION
    
   
    #stop falling if on bottom of game screen
    if ypos > 800:
        isOnGround = True
        vy = 0
        ypos = 800 - 15
   
    #gravity
    if isOnGround == False:
        vy+=.2 #notice this grows over time, aka ACCELERATION
   

    #update player position
    xpos+=vx
    ypos+=vy
   
   
    #ANIMATION-------------------------------------------------------------------
        
    # Update Animation Information
    # Only animate when in motion
    if vx < 0: #left animation
        RowNum = 1
        # Ticker is a spedometer. We don't want Link animating as fast as the
        # processor can process! Update Animation Frame each time ticker goes over
        ticker+=1
        if ticker%10==0: #only change frames every 10 ticks
          frameNum+=1
           #If we are over the number of frames in our sprite, reset to 0.
           #In this particular case, there are 10 frames (0 through 9)
        if frameNum>3: 
           frameNum = 0
           
    if vx > 0: #left animation
        RowNum = 0
        # Ticker is a spedometer. We don't want Link animating as fast as the
        # processor can process! Update Animation Frame each time ticker goes over
        ticker+=1
        if ticker%10==0: #only change frames every 10 ticks
          frameNum+=1
           #If we are over the number of frames in our sprite, reset to 0.
           #In this particular case, there are 10 frames (0 through 9)
        if frameNum>3: 
           frameNum = 0
     # RENDER--------------------------------------------------------------------------------
    # Once we've figured out what frame we're on and where we are, time to render.
            
    
 
    # RENDER Section--------------------------------------------------------------------------------
           
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
    screen.blit(Link, (xpos, ypos), (frameWidth*frameNum, RowNum*frameHeight, frameWidth, frameHeight))

    #for i in range (16):
         #for j in range(16):
             #if map[i][j]==1:
                 #pygame.draw.rect(screen, (200, 0, 100), (i*30, 750, 100, 20))
    #pygame.draw.rect(screen, (100, 200, 100), (xpos, ypos, 20, 40))
   
    #first platform
    p1.draw()
    p2.draw()
    p3.draw()
    p4.draw()
    p5.draw()
    p6.draw()
    p7.draw()
    p8.draw()

   
    pygame.display.flip()#this actually puts the pixel on the screen
   
#end game loop------------------------------------------------------------------------------
pygame.quit()
