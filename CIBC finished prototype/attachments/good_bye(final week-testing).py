import random
import time
import pygame
pygame.init()
clock = pygame.time.Clock()
Player_width = 30
player_height = 70

sprite = pygame.image.load('pig.png')
roll_1 = pygame.image.load('dice1.png')
roll_2 = pygame.image.load('dice2.png') 
roll_3 = pygame.image.load('dice3.png')
roll_4 = pygame.image.load('dice4.png')
roll_5 = pygame.image.load('dice5.png')
roll_6 = pygame.image.load('dice6.png')
square1 = pygame.image.load('square.png')
puppy = pygame.image.load('puppy.png')
game_console = pygame.image.load('game_console.png')
tablet = pygame.image.load('tablet.png')
phone = pygame.image.load('phone.png')
bike = pygame.image.load('bike.png')
finish = pygame.image.load('finish.png')
start = pygame.image.load('start.png')
title=pygame.image.load('title.png')
splash = pygame.image.load('splash.png')
Height = 70
Width = 70
Margin = 5
x,y = 0,0
white = (255,255,255)
red =(255,0,0)#spend
black =(0,0,0)
blue = (0,0,255)#invest
green =(0,255,0)#save
darkBlue = (0,0,128)#donate
pink = (255,165,0) #actually orange
yellow = (255,255,0)
payday = pygame.image.load('payday.png')#payday
QMark = pygame.image.load('Qmark.png')#chance
##sim_rect = pygame.Rect(225,125,30,30)
##quiz_rect =pygame.Rect(500,125,30,30)
##quit_rect = pygame.Rect(375,425,30,30)
roll = pygame.Rect(210,280,70,70)
gameDisplay = pygame.display.set_mode((1000,600))
wood = pygame.image.load('wood.png')

option_rect = [roll,(0,0,35,35),(0,70,35,35),(420,490,70,70),(70,490,70,70),(280,350,70,70),(210,210,70,70),(490,70,70,70),(420,0,70,70),(70,0,70,70),(0,280,70,70),(490,490,70,70),(210,350,70,70),(280,210,70,70),(490,0,70,70),(0,490,70,70),(0,0,70,70),(0,140,70,70),(140,0,70,70),(490,140,70,70),(140,210,70,70),(350,350,70,70),(140,490,70,70),(600,8,380,550),(210,490,35,35),(490,420,35,35),(420,350,35,35),(490,210,35,35),(210,0,35,35),(0,420,35,35),(0,210,35,35),(0,70,35,35),(280,0,35,35),(420,210,35,35),(140,280,35,35),(280,490,35,35),(0,350,35,35),(350,0,35,35),(350,210,35,35),(140,350,35,35),(490,350,35,35),(350,490,-35,-35)]
select_rect = pygame.Rect(x,y,60,60)

def player(x,y):
    gameDisplay.blit(sprite,(x,y))
def dice_roll():
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        toss = random.randint(1,6)
        if (toss == 1):
            gameDisplay.blit(roll_1,(210,280))
        elif (toss == 2):
            gameDisplay.blit(roll_2,(210,280))
        elif (toss == 3):
            gameDisplay.blit(roll_3,(210,280))
        elif (toss == 4):
            gameDisplay.blit(roll_4, (210,280))
        elif (toss == 5):
            gameDisplay.blit(roll_5, (210,280))
        elif (toss == 6):
            gameDisplay.blit(roll_6, (210,280))

def question_pop_up():
    pressed = pygame.key.get_pressed()
    start_money = 200
    money_earned = 10
    money_spend = int()
    money_invested = 0
    money_saved =int()

    
    
    
#darkblue donate
    if pressed[pygame.K_RETURN]:
        for rect in option_rect:
            if select_rect.colliderect(rect):
                if rect == (0,350,35,35) or rect ==(350,0,35,35)or rect ==(350,210,35,35)or rect ==(140,350,35,35)or rect ==(490,350,35,35)or rect ==(350,490, 35,35):
                    gameDisplay.blit(square1,(0,140))
                    font = pygame.font.SysFont(None, 40)
                    customText1 ='You can Donate time or money.'
                    customText2 ='Which would you like to donate to?'
                    customText3 ='A-Donate to Paws'
                    customText4 ='B-Donate time to TechSupporks IT'
                    customText5 ='program for children'
                    customText6 ='Press A or B to enter your choice'
                    text1 = font.render(customText1, True, white)
                    text2 = font.render(customText2, True, white)
                    text3 = font.render(customText3, True, yellow)
                    text4 = font.render(customText4, True, yellow)
                    text5 = font.render(customText5, True, yellow)
                    text6 = font.render(customText6, True, white)
                    gameDisplay.blit(text1,(10,160))
                    gameDisplay.blit(text2,(10,200))
                    gameDisplay.blit(text3,(10,250))
                    gameDisplay.blit(text4,(10,290))
                    gameDisplay.blit(text5,(10,320))
                    gameDisplay.blit(text6,(10,380))
#qmark                   
                elif rect ==(280,490,35,35)or rect == (280,0,35,35) or rect == (420,210,35,35)or rect == (140,280,35,35):
                    gameDisplay.blit(square1,(0,140))
                    font = pygame.font.SysFont(None, 40)
                    customText1 ='Oops!! You lost your cell phone.'
                    customText2 ='Pay your deductable.YOU LOST -$40'
                    text1 = font.render(customText1, True, white)
                    text2 = font.render(customText2, True, white)
                    gameDisplay.blit(text1,(10,160))
                    gameDisplay.blit(text2,(10,200))



#                elif rect ==(0,0,35,35):

                elif rect ==(0,70,35,35):
                    gameDisplay.blit(square1,(0,140))
                    font = pygame.font.SysFont(None, 40)
                    customText1 ="You have Finished the Game!!!YAY!!" 
                    customText2 ="Play again and try and beat your"
                    customText3 ="score!! Or dare someone else!!"
                    customText4 ='Until next time. TechSuppork out!!'
                    text1 = font.render(customText1, True, white)
                    text2 = font.render(customText2, True, white)
                    text3 = font.render(customText3, True, white)
                    text4 = font.render(customText4, True, white)
                    gameDisplay.blit(text1,(10,160))
                    gameDisplay.blit(text2,(10,200))
                    gameDisplay.blit(text3,(10,240))
                    gameDisplay.blit(text4,(10,280))
                    


#payday                    
                elif rect == (210,490,35,35) or rect == (490,420,35,35) or rect == (420,350,35,35) or rect == (490,210,35,35) or rect == (210,0,35,35) or rect == (0,420,35,35) or rect == (0,210,35,35):
                    gameDisplay.blit(square1,(0,140))
                    font = pygame.font.SysFont(None, 40)
                    customText1 ='What are the two ways'
                    customText2 ='you can donate?'
                    customText3 ='A- Time and Money'
                    customText4 ='B- Saving and Investing '
                    customText6 ='Press A or B to enter your choice'

                    text1 = font.render(customText1, True, white)
                    text2 = font.render(customText2, True, white)
                    text3 = font.render(customText3, True, yellow)
                    text4 = font.render(customText4, True, yellow)
                    text6 = font.render(customText6, True, white)

                    gameDisplay.blit(text1,(10,160))
                    gameDisplay.blit(text2,(10,200))
                    gameDisplay.blit(text3,(10,250))
                    gameDisplay.blit(text4,(10,290))
                    gameDisplay.blit(text6,(10,380))

#blue invest
                elif rect == (0,140,70,70) or rect == (140,0,70,70) or rect == (490,140,70,70) or rect == (140,210,70,70) or rect == (350,350,70,70) or rect == (140,490,70,70) or rect == (600,8,380,550):
                    gameDisplay.blit(square1,(0,140))
                    font = pygame.font.SysFont(None, 40)
                    customText1 ='Investing: To invest is to'
                    customText2 ='distribute money in the expectation'
                    customText3 ='of some benefit in the future.'
                    customText4 ='Which would you like to invest in?'
                    customText5 ='A - Buy a share of CIBC stock.'
                    customText6 ='B - Buy a share of VICI stock.'
                    text1 = font.render(customText1, True, white)
                    text2 = font.render(customText2, True, white)
                    text3 = font.render(customText3, True, white)
                    text4 = font.render(customText4, True, white)
                    text5 = font.render(customText5, True, yellow)
                    text6 = font.render(customText6, True, yellow)
                    gameDisplay.blit(text1,(10,160))
                    gameDisplay.blit(text2,(10,200))
                    gameDisplay.blit(text3,(10,240))
                    gameDisplay.blit(text4,(10,280))
                    gameDisplay.blit(text5,(10,320))
                    gameDisplay.blit(text6,(10,360))
 #red spend      
                elif rect == (490,490,70,70) or rect == (210,350,70,70) or rect == (280,210,70,70) or rect == (490,0,70,70) or rect == (0,490,70,70):
                    gameDisplay.blit(square1,(0,140))
                    font = pygame.font.SysFont(None, 40)
                    customText1 ='Spending: '
                    customText2 ='Def'
                    customText3 ='def'
                    customText4 ='Would you like to buy a badge? '
                    customText6 ='A. Yes'

                    text1 = font.render(customText1, True, white)
                    text2 = font.render(customText2, True, white)
                    text3 = font.render(customText3, True, yellow)
                    text4 = font.render(customText4, True, yellow)
                    text6 = font.render(customText6, True, white)

                    gameDisplay.blit(text1,(10,160))
                    gameDisplay.blit(text2,(10,200))
                    gameDisplay.blit(text3,(10,250))
                    gameDisplay.blit(text4,(10,290))
                    gameDisplay.blit(text6,(10,380))
#green save
                elif rect == (420,490,70,70) or rect == (70,490,70,70) or rect == (280,350,70,70) or rect == (210,210,70,70) or rect == (490,70,70,70) or rect == (420,0,70,70) or rect == (70,0,70,70) or rect == (0,280,70,70):
                    gameDisplay.blit(square1,(0,140))
                    font = pygame.font.SysFont(None, 40)
                    customText1 ='Save: an amount of something that is'
                    customText2 ='not spent or used.'
                    customText3 ='Would you like to put money in your'
                    customText4 ='CIBC savings account?'
                    customText5 ='A. Yes put $50'
                    customText6 ='B. Yes put $100'
                    customText7 ='C. Not now.'

                    text1 = font.render(customText1, True, white)
                    text2 = font.render(customText2, True, white)
                    text3 = font.render(customText3, True, yellow)
                    text4 = font.render(customText4, True, yellow)
                    text5 = font.render(customText5, True, green)
                    text6 = font.render(customText6, True, pink)
                    text7 = font.render(customText7, True, red)

                    gameDisplay.blit(text1,(10,160))
                    gameDisplay.blit(text2,(10,200))
                    gameDisplay.blit(text3,(10,250))
                    gameDisplay.blit(text4,(10,290))
                    gameDisplay.blit(text5,(10,330))
                    gameDisplay.blit(text6,(10,370))
                    gameDisplay.blit(text7,(10,410))
    

    font = pygame.font.SysFont(None, 60)
    text = font.render('Saved:     $'+str(money_saved), True, white)

    gameDisplay.blit(text,(640,200))


  

#Money they have
    
    font = pygame.font.SysFont(None, 60)
    text = font.render('Invested: $'+str(money_invested), True, white)

    gameDisplay.blit(text,(640,130))

    
#Menu
    font = pygame.font.SysFont(None, 40)
    text = font.render('Menu', True, white)

    gameDisplay.blit(text,(635,50))
#rules

    font = pygame.font.SysFont(None, 40)
    text = font.render('Rules', True, white)

    gameDisplay.blit(text,(750,50))

    #Exit
    font = pygame.font.SysFont(None, 40)
    text = font.render('Exit', True, white)

    gameDisplay.blit(text,(880,50))
#Badges
    font = pygame.font.SysFont(None, 50)
    text = font.render('Badges', True, white)
    gameDisplay.blit(text,(740,280))

#Money
    font = pygame.font.SysFont(None,50)
    text = font.render('Account: $' + str(start_money), True, white)
    gameDisplay.blit(text,(165,120))


def board():
#squares
    gameDisplay.blit(wood,(0,0))
    gameDisplay.blit(title,(70,70))
    gameDisplay.blit(start,(0,0))
    gameDisplay.blit(finish,(0,70))
    pygame.draw.rect(gameDisplay, blue, (0,140,70,70))
    gameDisplay.blit(payday, (0,210))
    pygame.draw.rect(gameDisplay, green, (0,280,70,70))
    pygame.draw.rect(gameDisplay, darkBlue, (0,350,70,70))
    gameDisplay.blit(payday, (0,420))
    pygame.draw.rect(gameDisplay, red, (0,490,70,70))
    pygame.draw.rect(gameDisplay, green, (70,0,70,70))
    pygame.draw.rect(gameDisplay, blue, (140,0,70,70))
    gameDisplay.blit(payday,(210,0))
    gameDisplay.blit(QMark,(280,0))
    pygame.draw.rect(gameDisplay, darkBlue, (350,0,70,70))
    pygame.draw.rect(gameDisplay, green, (420,0,70,70))
    pygame.draw.rect(gameDisplay, red, (490,0,70,70))
    pygame.draw.rect(gameDisplay, green, (490,70,70,70))
    pygame.draw.rect(gameDisplay, blue, (490,140,70,70))
    gameDisplay.blit(payday, (490,210))
    gameDisplay.blit(QMark,(420,210))
    pygame.draw.rect(gameDisplay, darkBlue, (350,210,70,70))
    pygame.draw.rect(gameDisplay, red, (280,210,70,70))
    pygame.draw.rect(gameDisplay, green, (210,210,70,70))
    pygame.draw.rect(gameDisplay, blue, (140,210,70,70))
    gameDisplay.blit(QMark,(140,280))    
    pygame.draw.rect(gameDisplay, darkBlue, (140,350,70,70))
    pygame.draw.rect(gameDisplay, red, (210,350,70,70))
    pygame.draw.rect(gameDisplay, green, (280,350,70,70))
    pygame.draw.rect(gameDisplay, blue, (350,350,70,70))
    gameDisplay.blit(payday, (420,350))
    pygame.draw.rect(gameDisplay, darkBlue, (490,350,70,70))
    gameDisplay.blit(payday,(490,420))
    pygame.draw.rect(gameDisplay, red, (490,490,70,70))
    pygame.draw.rect(gameDisplay, green, (70,490,70,70))
    pygame.draw.rect(gameDisplay, blue, (140,490,70,70))
    gameDisplay.blit(payday,(210,490))
    gameDisplay.blit(QMark,(280,490))
    pygame.draw.rect(gameDisplay, darkBlue, (350,490,70,70))
    pygame.draw.rect(gameDisplay, green, (420,490,70,70))
    pygame.draw.rect(gameDisplay, blue, (600,8,380,550))

#white outline for all the squares
    pygame.draw.rect(gameDisplay,white, (210,280,70,70,),2)#area for the dice
    pygame.draw.rect(gameDisplay, white, (0,0,70,70),1)
    pygame.draw.rect(gameDisplay, white, (0,70,70,70),1)
    pygame.draw.rect(gameDisplay, white, (0,140,70,70),1)
    pygame.draw.rect(gameDisplay, white, (0,210,70,70),1)
    pygame.draw.rect(gameDisplay, white, (0,280,70,70),1)
    pygame.draw.rect(gameDisplay, white, (0,350,70,70),1)
    pygame.draw.rect(gameDisplay, white, (0,420,70,70),1)
    pygame.draw.rect(gameDisplay, white, (0,490,70,70),1)
    pygame.draw.rect(gameDisplay, white, (70,0,70,70),1)
    pygame.draw.rect(gameDisplay, white, (140,0,70,70),1)
    pygame.draw.rect(gameDisplay, white, (210,0,70,70),1)
    pygame.draw.rect(gameDisplay, white, (280,0,70,70),1)
    pygame.draw.rect(gameDisplay, white, (350,0,70,70),1)
    pygame.draw.rect(gameDisplay, white, (420,0,70,70),1)
    pygame.draw.rect(gameDisplay, white, (490,0,70,70),1)
    pygame.draw.rect(gameDisplay, white, (490,70,70,70),1)
    pygame.draw.rect(gameDisplay, white, (490,140,70,70),1)
    pygame.draw.rect(gameDisplay, white, (490,210,70,70),1)
    pygame.draw.rect(gameDisplay, white, (420,210,70,70),1)
    pygame.draw.rect(gameDisplay, white, (350,210,70,70),1)
    pygame.draw.rect(gameDisplay, white, (280,210,70,70),1)
    pygame.draw.rect(gameDisplay, white, (210,210,70,70),1)
    pygame.draw.rect(gameDisplay, white, (140,210,70,70),1)
    pygame.draw.rect(gameDisplay, white, (140,280,70,70),2)
    pygame.draw.rect(gameDisplay, white, (140,350,70,70),2)
    pygame.draw.rect(gameDisplay, white, (210,350,70,70),2)
    pygame.draw.rect(gameDisplay, white, (280,350,70,70),2)
    pygame.draw.rect(gameDisplay, white, (350,350,70,70),2)
    pygame.draw.rect(gameDisplay, white, (420,350,70,70),2)
    pygame.draw.rect(gameDisplay, white, (490,350,70,70),2)
    pygame.draw.rect(gameDisplay, white, (490,420,70,70),2)
    pygame.draw.rect(gameDisplay, white, (490,490,70,70),2)
    pygame.draw.rect(gameDisplay, white, (70,490,70,70),2)
    pygame.draw.rect(gameDisplay, white, (140,490,70,70),2)
    pygame.draw.rect(gameDisplay, white, (210,490,70,70),2)
    pygame.draw.rect(gameDisplay, white, (280,490,70,70),2)
    pygame.draw.rect(gameDisplay, white, (350,490,70,70),2)
    pygame.draw.rect(gameDisplay, white, (420,490,70,70),2)
    pygame.draw.rect(gameDisplay, white, (490,490,70,70),2)
    pygame.draw.rect(gameDisplay, white, (600,8,380,550),2)
    pygame.draw.rect(gameDisplay, white, (0,0,998,598),2)
    
    
    pygame.draw.rect(gameDisplay, white, (610,16,360,520),5)#inner line in blue circle
    pygame.draw.rect(gameDisplay, white, (617,28,110,70),5)#menu
    pygame.draw.rect(gameDisplay, white, (734,28,110,70),5)#rules
    pygame.draw.rect(gameDisplay, white, (851,28,110,70),5)#exit
    pygame.draw.rect(gameDisplay, white, (620,110,340,70),5)#cash square
    pygame.draw.rect(gameDisplay, white, (620,190,340,70),5)#saving square
    pygame.draw.rect(gameDisplay, white, (620,270,340,250),5)#badges square
##    pygame.draw.rect(gameDisplay, black, (70,70,420,140))
##    pygame.draw.rect(gameDisplay, black, (70,210,70,280))
##    pygame.draw.rect(gameDisplay, black, (140,420,350,70))
##    pygame.draw.rect(gameDisplay,black, (280,280,280,70,))
    gameDisplay.blit(game_console,(630,330))
    gameDisplay.blit(puppy,(670,420))
    gameDisplay.blit(tablet,( 735, 330))
    gameDisplay.blit(phone,(860,330))
    gameDisplay.blit(bike,(790,420))
    


    
def game_loop():

    x = (20*.5)
    
    y = (10*.5)
    x_change = 0
    y_change = 0
    dead = False    

    while not dead:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dead = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change=0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    y_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5


            if event.type == pygame.KEYUP:
                if event.key==pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change=0        
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP] and y > 0:
                y -= 5
                
            if pressed[pygame.K_DOWN] and y < 600 - 60:
                y += 5
            if pressed[pygame.K_LEFT] and x > 0:
                x -= 5
            if pressed[pygame.K_RIGHT] and x < 800 - 60:
                x += 5 

            select_rect.x,select_rect.y= x,y

            

     


                
        x+= x_change
        y+= y_change

        ##gameDisplay.fill()

        
        board()
        player(x,y)
        dice_roll()
        question_pop_up()
        
        if x > 600 - Player_width or x < 0:
            dead = False
        elif y >625-player_height or y<0:
            dead = False
        pygame.display.update()
        clock.tick(60)
def start_roll():
    gameDisplay.blit(square1,(0,140))
    font = pygame.font.SysFont(None, 40)
    customText1 ="Welcome to TechSuppork's Money" 
    customText2 ="Savvy Game! Let's Get started!"
    customText3 ="Roll the Dice by hitting the"
    customText4 ='SpaceBar to Begin. Safe Travels!'
    text1 = font.render(customText1, True, white)
    text2 = font.render(customText2, True, white)
    text3 = font.render(customText3, True, white)
    text4 = font.render(customText4, True, white)
    gameDisplay.blit(text1,(10,160))
    gameDisplay.blit(text2,(10,200))
    gameDisplay.blit(text3,(10,240))
    gameDisplay.blit(text4,(10,280))
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RETURN]:
        game_loop()
def start_game():
    start = False

    while not start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = True

            if True:
                gameDisplay.fill(black)
                gameDisplay.blit(splash,(0,0))
               
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_loop()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            start_roll()
##               
            
        pygame.display.update()
        clock.tick(60)
        
start_game()
#game_loop()
pygame.quit()
quit()
