#############
#File Name: Pong Game
#Description: Pong Game with pygame
#Author: Vincent Zhou
#############

#Import modules
import pygame
import time
from pygame.locals import QUIT
import random

WIDTH = 800
HEIGHT = 600
WHITE=255,255,255
BLACK=0,0,0
GREY=156,155,152

pygame.init() #intiate

#Font
font1 = pygame.font.SysFont("Arial",25)
font2 = pygame.font.Font("Retro Gaming.ttf",50)
#Ball shape
pygame.mixer.music.load("Yomama.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(loops=-1)
ballX = 320
ballY = 240
ballR = 10
shiftY = 7
shiftX = 7

#Paddle Lengths
PADDLELENGTH = 20
PADDLEWIDTH = 80
L= 7        
W = 80
#First Paddle Cords
firstPaddleX=60
firstPaddleY=300
#Second Paddle Cords
secondPaddleX=740
secondPaddleY=300
gameWindow = pygame.display.set_mode((WIDTH,HEIGHT))

#Score
score1 = 0
score1X = 300
score1Y = 50
score2 = 0
score2X = 500
score2Y = 50
scoreLimit = 7

#Load Images  
background2 = pygame.image.load("bing chilling.png")
kissJoemama = pygame.image.load("kiss Joe MAMA.png")
theRock = pygame.image.load("cover2.jpg")

#Flags
run = True
firstWindow = True
inPlay = False
gameEnd = False
#Flags for modes
hard=False
medium=False
easy=False

#Clock
clock=pygame.time.Clock()

#Load Sounds  
sound1=pygame.mixer.Sound("Bouncing sound effect.mp3")
sound1.set_volume(0.35)
sound2=pygame.mixer.Sound("Ping Pong score sound effect.mp3")
sound2.set_volume(0.35)
sound3=pygame.mixer.Sound("Bing Chilling vine boom.mp3")
sound3.set_volume(0.35)
sound4=pygame.mixer.Sound("Mario lose sound effect (HD).mp3")
sound4.set_volume(0.35)
sound5=pygame.mixer.Sound("The Rock sound effect.mp3")
sound5.set_volume(0.35)
sound6=pygame.mixer.Sound("Ohmygawd.mp3")
sound6.set_volume(0.35)

#Graphics/Words -  
title1 = font2.render("JOEMAMA'S", 50, BLACK)
title1X = 250
title1Y = 100

title2 = font2.render("Ping Pong Game", 50, BLACK)
title2X = 175
title2Y = 150

level1 = font2.render("EASY", 45, WHITE)
level11 = font2.render("EASY", 45, BLACK)
level1X = 325
level1Y = 265

level2 = font2.render("MEDIUM", 45, WHITE)
level22 = font2.render("MEDIUM", 45, BLACK)
level2X = 285
level2Y = 390

level3 = font2.render("Hard", 45, WHITE)
level33 = font2.render("Hard", 45, BLACK)
level3X = 325
level3Y = 515

endScreenTitle = font2.render("GAME OVER", 45, BLACK)
replayButton1 = font2.render("PLAY AGAIN", 45, BLACK)
replayButton2 = font2.render("PLAY AGAIN", 45, WHITE)
replayButton1X = 220
replayButton1Y = 265


exitButton1 = font2.render("Kiss JoeMAMA",45, BLACK)
exitButton2 = font2.render("Kiss JoeMAMA",45, WHITE)
exitButton1X = 190
exitButton1Y = 375

#Define Drawings Functions - First Screen  
def titleDraw():
   gameWindow.blit(title1, (title1X, title1Y))#First Line
   gameWindow.blit(title2, (title2X, title2Y))#Second Line

def easyModeButtonDraw(): 
   pygame.draw.rect(gameWindow,BLACK,(200,250,400,100),3)   #Rect
   gameWindow.blit(level11, (level1X, level1Y)) #Text

def mediumModeButtonDraw():
   pygame.draw.rect(gameWindow,BLACK,(200,375,400,100),3)
   gameWindow.blit(level22, (level2X, level2Y))

def hardModeButtonDraw():
   pygame.draw.rect(gameWindow,BLACK,(200,500,400,100),3)   
   gameWindow.blit(level33, (level3X, level3Y))

def easyModeButtonHighlightedDraw():
   pygame.draw.rect(gameWindow,GREY,(200,250,400,100),0)
   gameWindow.blit(level1, (level1X, level1Y))    

def mediumModeButtonHighlightedDraw():
   pygame.draw.rect(gameWindow,GREY,(200,375,400,100),0) 
   gameWindow.blit(level2, (level2X, level2Y))  

def hardModeButtonHighlightedDraw():
   pygame.draw.rect(gameWindow,GREY,(200,500,400,100),0)   
   gameWindow.blit(level3, (level3X, level3Y))

#Define Drawing Functons - Second Screen  
def score1Draw(x,y):
   score = font1.render(str(score1), 5, BLACK)
   gameWindow.blit(score, (score1X, score1Y))

def score2Draw(x,y):
   score = font1.render(str(score2), 5, BLACK)
   gameWindow.blit(score, (score2X, score2Y))

def firstPaddleDraw(firstPaddleX,firstPaddleY):
   pygame.draw.rect(gameWindow,BLACK,(firstPaddleX,firstPaddleY,L,W),0)

def secondPaddleDraw(secondPaddleX, secondPaddleY):
   pygame.draw.rect(gameWindow,BLACK,(secondPaddleX,secondPaddleY,L,W),0)

def drawBall(ballX, ballY):
   pygame.draw.circle(gameWindow,BLACK, (ballX, ballY), ballR, 0)

def dottedMiddleLine(HEIGHT):
   for x in range(0,HEIGHT,40):
        pygame.draw.rect(gameWindow,BLACK,(395,x,10,30),0)

def movementRedraw():
    firstPaddleDraw(firstPaddleX,firstPaddleY)
    secondPaddleDraw(secondPaddleX, secondPaddleY)
    drawBall(ballX, ballY)
    score1Draw(score1X, score1Y)
    score2Draw(score2X,score2Y)
def movementRedraw1():
    pygame.draw.rect(gameWindow,(random.randint(1,255),random.randint(1,255),random.randint(1,255)),(firstPaddleX,firstPaddleY,L,W),0)
    pygame.draw.rect(gameWindow,(random.randint(1,255),random.randint(1,255),random.randint(1,255)),(secondPaddleX,secondPaddleY,L,W),0)
    pygame.draw.circle(gameWindow,(random.randint(1,255),random.randint(1,255),random.randint(1,255)), (ballX, ballY), ballR, 0)
    score1Draw(score1X, score1Y)
    score2Draw(score2X,score2Y)


#Define Drawing Functions - Third Screen  
def playerOneWinDraw():
   winnerTitle = font2.render("PLAYER ONE WINS", 45, BLACK)
   winnerTitleX = 150
   winnerTitleY = 150
   gameWindow.blit(winnerTitle, (winnerTitleX, winnerTitleY))

def playerTwoWinDraw():
   winnerTitle = font2.render("PLAYER TWO WINS", 45, BLACK)
   winnerTitleX = 150
   winnerTitleY = 150
   gameWindow.blit(winnerTitle, (winnerTitleX, winnerTitleY))

def replayButtonDraw():
   pygame.draw.rect(gameWindow,BLACK,(150,250,500,100),3)
   gameWindow.blit(replayButton1, (replayButton1X, replayButton1Y)) 

def exitButtonDraw():
   pygame.draw.rect(gameWindow,BLACK,(150,360,500,100),3)
   gameWindow.blit(exitButton1, (exitButton1X, exitButton1Y))

def replayButtonHighlightedDraw():
   pygame.draw.rect(gameWindow,GREY,(150,250,500,100),0)
   gameWindow.blit(replayButton2, (replayButton1X, replayButton1Y))

def exitButtonHighlightedDraw():
   pygame.draw.rect(gameWindow,GREY,(150,360,500,100),0)
   gameWindow.blit(exitButton2, (exitButton1X, exitButton1Y))

easyArrayX1=[]
easyArrayY1=[]
for z in range (0,500):
    u=200
    u=u+z
    easyArrayX1.append(u)

for z in range(0,100):
    u=250
    u=u+z
    easyArrayY1.append(u)

mediumArrayX1=[]
mediumArrayY1=[]
for z in range (0,400):
    u=200
    u=u+z
    mediumArrayX1.append(u)

for z in range(0,100):
    u=355
    u=u+z
    mediumArrayY1.append(u)

hardArrayX1=[]
hardArrayY1=[]
for z in range (0,400):
    u=200
    u=u+z
    hardArrayX1.append(u)

for z in range(0,100):
    u=460
    u=u+z
    hardArrayY1.append(u)


#Third Screen Buttons  
playArrayX2=[]
playArrayY2=[]
for z in range (0,500):
    u=150
    u=u+z
    playArrayX2.append(u)

for z in range(0,100):
    u=250
    u=u+z
    playArrayY2.append(u)

exitArrayX=[]
exitArrayY=[]
for z in range (0,500):
    u=150
    u=u+z
    exitArrayX.append(u)

for z in range(0,100):
    u=360
    u=u+z
    exitArrayY.append(u)


#Game Loops
#First Window
while run == True:
   while firstWindow == True: # 
      background = pygame.image.load("background for starting screen.png")
      gameWindow.blit(background,(0,0))
      titleDraw()
      pygame.event.get()
      positionx,positiony=pygame.mouse.get_pos()
      leftMouse,middleMouse,rightMouse=pygame.mouse.get_pressed() #Tracks Mouse
      pygame.event.clear()
      easyModeButtonDraw()
      mediumModeButtonDraw()
      hardModeButtonDraw()
      pygame.display.update()
   
      #Click Function for easy button  
      while positionx in easyArrayX1 and positiony in easyArrayY1 and firstWindow == True: 
         pygame.event.get()
         positionx,positiony=pygame.mouse.get_pos()
         leftMouse,middleMouse,rightMouse=pygame.mouse.get_pressed()
         gameWindow.blit(background,(0,0))
         easyModeButtonHighlightedDraw()
         mediumModeButtonDraw()
         hardModeButtonDraw()
         titleDraw()
         pygame.display.update()
         if leftMouse == True:
            easy=True
            firstWindow = False
            inPlay=True
   #Click Function for medium button  
      while positionx in mediumArrayX1 and positiony in mediumArrayY1 and firstWindow == True: 
         pygame.event.get()
         positionx,positiony=pygame.mouse.get_pos()
         leftMouse,middleMouse,rightMouse=pygame.mouse.get_pressed()
         gameWindow.blit(background,(0,0))
         easyModeButtonDraw()
         mediumModeButtonHighlightedDraw()
         hardModeButtonDraw()
         titleDraw()
         pygame.display.update()
         if leftMouse == True:
            medium=True
            firstWindow = False
            inPlay=True
         #Click Function for hard button  
      while positionx in hardArrayX1 and positiony in hardArrayY1 and firstWindow == True: 
         pygame.event.get()
         positionx,positiony=pygame.mouse.get_pos()
         leftMouse,middleMouse,rightMouse=pygame.mouse.get_pressed()
         gameWindow.blit(background,(0,0))
         easyModeButtonDraw()
         mediumModeButtonDraw()
         hardModeButtonHighlightedDraw()
         titleDraw()
         pygame.display.update()
         if leftMouse == True:
            hard=True
            firstWindow = False
            inPlay=True

   #Flags and Variables for Cheat  
   elapsed=time.time() #Timer
   BEGIN=0 #To make so you dont have to hold the cheat button and instead tap it to work
   fast=False  #Flag for increased Paddle Movement Speed
   bingchiling=False #Flag for Cheat
   musicVariable=0 #Added to make the background sound so it is not constantly looping and can reloop even after the cheat music is done playing
   FPS=60 #Frames
   if easy:
      shiftX=3
   if medium:
      shiftX=5
   if hard:
      shiftX=6.5
   while inPlay == True:
      
      #music for cheat  
      musicVariable=musicVariable+1
      if musicVariable==1: 
         pygame.mixer.music.load("Background music PSX.mp3") #Background Music 
         pygame.mixer.music.set_volume(0.1)                  #Used mixer to allow it to play in the background
         pygame.mixer.music.play(loops=-1)
      #fps and elapsed time  
      clock.tick(FPS)
      if bingchiling and fast:
         elapsed=time.time()-BEGIN
      
      if elapsed<10:
         fast=True
         bingchiling=True
      else:
         if elapsed>10 and elapsed<20: #Cheat is ten seconds long
            musicVariable=0
            elapsed=21
         fast=False
         bingchiling=False
      

      if bingchiling==False: #Reset the background
         gameWindow.fill(WHITE)
         dottedMiddleLine(HEIGHT)
         
      else:
         gameWindow.blit(background2,(0,0))

         
      #intial score display  
      score1Draw(score1X, score1Y)
      score2Draw(score2X,score2Y)

      #Intial Paddle Drawing
      firstPaddleDraw(firstPaddleX,firstPaddleY)
      secondPaddleDraw(secondPaddleX, secondPaddleY)
      
      pygame.event.get()
      keys=pygame.key.get_pressed() #Gets input from keyboard
      
      if bingchiling==True: #Makes the paddles turn Rainbow consistently during the cheat. Without it they only switch colours when a key is pressed
         movementRedraw1()
      #First Paddle Movement  
      #Up 
      if keys[pygame.K_w]:
         gameWindow.fill(WHITE) #Redrawing
         dottedMiddleLine(HEIGHT)
         if firstPaddleY>0:
            firstPaddleY-=10
         if bingchiling==True: #Redrawing
            gameWindow.blit(background2,(0,0))
            movementRedraw1() 
         else:
            movementRedraw()   
      #Down
      if keys[pygame.K_s]:
         gameWindow.fill(WHITE)
         dottedMiddleLine(HEIGHT) #Redrawing
         if firstPaddleY<HEIGHT-PADDLEWIDTH:
            firstPaddleY+=10
         if bingchiling==True: #Redrawing
            gameWindow.blit(background2,(0,0))
            movementRedraw1()
         else:
            movementRedraw()
      

      #Second Paddle  
      pygame.event.get()
      keys=pygame.key.get_pressed()
      #Up
      if keys[pygame.K_UP]:
         gameWindow.fill(WHITE)
         dottedMiddleLine(HEIGHT) #Redrawing
         if secondPaddleY>0 and fast!=True: #Cheat for second paddle
            secondPaddleY=secondPaddleY-10
         if secondPaddleY>0 and fast==True:
            secondPaddleY=secondPaddleY-100
         if bingchiling==True: #Redrawing
            gameWindow.blit(background2,(0,0))
            movementRedraw1()
         else:
            movementRedraw()
      #Down
      if keys[pygame.K_DOWN]: 
         gameWindow.fill(WHITE)
         dottedMiddleLine(HEIGHT) #Redrawing
         if secondPaddleY<HEIGHT-PADDLEWIDTH and fast!=True: #Cheat for second paddle
            secondPaddleY+=10
         if secondPaddleY<HEIGHT-PADDLEWIDTH and fast==True:
            secondPaddleY=secondPaddleY+100
         if bingchiling==True: #Redrawing
            gameWindow.blit(background2,(0,0))
            movementRedraw1()
         else:
            movementRedraw()



      if secondPaddleY<0:
         secondPaddleY=0 #Stop the paddle from going off screen   
         pygame.draw.rect(gameWindow,BLACK,(740,0,20,80),0)
      if secondPaddleY>HEIGHT-PADDLEWIDTH:
         secondPaddleY=HEIGHT-PADDLEWIDTH
         pygame.draw.rect(gameWindow,BLACK,(740,HEIGHT-80,20,80),0)       

      if keys[pygame.K_TAB]: #Key to activate Cheat  
         BEGIN=time.time()
         bingchiling=True
         fast=True
         pygame.mixer.music.pause()
         pygame.mixer.music.load("Bing Chilling vine boom.mp3")
         pygame.mixer.music.set_volume(0.35)
         pygame.mixer.music.play()


      #Ball movement  
      if bingchiling==True:
         pygame.draw.circle(gameWindow,(random.randint(1,255),random.randint(1,255),random.randint(1,255)),(ballX,ballY),ballR,0)
      else:
         pygame.draw.circle(gameWindow,BLACK, (ballX, ballY), ballR, 0)
      ballY = ballY + shiftY
      ballX = ballX + shiftX
      #Ball Bounce of off Top and Bottom Wall  
      if ballY > HEIGHT or ballY <0: 
         shiftY = -shiftY
         sound1.play(loops = 0) 
      
      #Ball Bounce off of Paddle Horizontal   and  
      
      shiftYListEasy=[-5,-3,0,3,5] #Difficulty for each level just makes the ball's angle steaper
      shiftYListMedium=[-8,-4,0,4,8]
      shiftYListHard = [-10,-5,0,5,10]
      
      if ballX>secondPaddleX and ballX<secondPaddleX+L and ballY>secondPaddleY and ballY<secondPaddleY+W: # we made the condition for the BallX to be between the secondPaddleX and the SecondPaddleX+10 because sometimes in hard difficulty, the ball would travel too fast and phase through the paddle so we had to make it a range
         shiftX=-shiftX
         sound1.play(loops = 0)
         if easy:
            shiftY= int(shiftYListEasy[random.randint(0,4)])
         if medium:
            shiftY= int(shiftYListMedium[random.randint(0,4)])
         if hard:
            shiftY= int(shiftYListHard[random.randint(0,4)])
      
      if ballX<firstPaddleX+L and ballX>firstPaddleX and ballY>firstPaddleY and ballY<firstPaddleY+W:
         shiftX=-shiftX
         sound1.play(loops = 0)
         if easy:
            shiftY= int(shiftYListEasy[random.randint(0,4)])
         if medium:
            shiftY= int(shiftYListMedium[random.randint(0,4)])
         if hard:
            shiftY= int(shiftYListHard[random.randint(0,4)])
   
      #Scoring  
      #Left side
      randomnumber=0
      if ballX <= -5:
         score2 = score2 + 1
         sound2.play(loops = 0)
         ballX = 400
         ballY = 300
         pygame.time.delay(350)
         shiftY=1

         randomnumber=random.randint(1,2) #Spawn direction is random
         
         shiftX=-shiftX
         if randomnumber==1:
            shiftY=shiftY
         else:
            shiftY=-shiftY
      #Right Side
      if ballX >=805:
         score1 = score1 + 1
         sound2.play(loops = 0)
         ballX = 400
         ballY = 300
         pygame.time.delay(350)
         shiftY=1
      
         randomnumber=random.randint(1,2) #Spawn direction is random
         shiftX=-shiftX
         if randomnumber==1:
            shiftY=shiftY
         else:
            shiftY=-shiftY
      pygame.display.update() 
      #End Screen   and  
      if score1>=scoreLimit or score2>=scoreLimit: #If scorelimit has been reached 
         gameEnd=True
         inPlay = False
         firstWindow = False
         sound4.play(loops=0)
         pygame.mixer.music.pause() #Stops background music 

   while gameEnd==True:
      gameWindow.fill(WHITE)
      background = pygame.image.load("end screen.png") #Background Image
      gameWindow.blit(background,(0,0))
      gameWindow.blit(endScreenTitle, (250, 100))
      if score1 == scoreLimit: #Declarition of which player won
         playerOneWinDraw()
      elif score2 == scoreLimit:
         playerTwoWinDraw()
      replayButtonDraw()
      exitButtonDraw()
            
      
      positionx,positiony=pygame.mouse.get_pos()
      
         
      #Replay Button   and  
      while positionx in playArrayX2 and positiony in playArrayY2 and gameEnd == True:
         
         replayButtonHighlightedDraw()
         positionx,positiony=pygame.mouse.get_pos()
         leftMouse,middleMouse,rightMouse=pygame.mouse.get_pressed()
         pygame.display.update()
         if leftMouse == True: #Reset all Varibles 
            gameEnd=False
            inPlay=True
            firstWindow = False
            score1=0
            score2=0
            elapsed=11
            bingchiling=False
            fast=False
            firstPaddleY=300
            secondPaddleY=300
            musicVariable=0
            pygame.event.clear()
         else:
            pygame.event.clear()
      pygame.event.clear()
      pygame.display.update()

         #Exit button Sound Effect  
      if positionx in exitArrayX and positiony in exitArrayY and gameEnd == True:
         sound5.play(loops=0)
         sound6.play(loops=0) 
      #Exit Button   and  
      while positionx in exitArrayX and positiony in exitArrayY and gameEnd == True:
         exitButtonHighlightedDraw()
         gameWindow.blit(kissJoemama, (50,100))
         gameWindow.blit(theRock, (500, 25))
         positionx,positiony=pygame.mouse.get_pos()
         leftMouse,middleMouse,rightMouse=pygame.mouse.get_pressed()
         pygame.display.update()
         if leftMouse == True:
            run = False  
            firstWindow = False
            inPlay = False
            gameEnd = False
         else: 
            pygame.event.clear()
      pygame.event.clear()
      pygame.display.update()     
   pygame.display.update()
   pygame.event.clear()    
pygame.quit()    
