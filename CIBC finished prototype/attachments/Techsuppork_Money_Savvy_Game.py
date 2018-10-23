import random
import time
import pygame
pygame.init()
gameDisplay = pygame.display.set_mode((1000,600))
clock = pygame.time.Clock()
Player_width = 30
player_height = 70

start_money = 200
money_earned = 10
money_invested = int()
money_saved =int()
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
splash = pygame.image.load('splash.png')
wood = pygame.image.load('wood.png')
payday = pygame.image.load('payday.png')#payday
QMark = pygame.image.load('Qmark.png')#chance
menu = pygame.image.load('menu.png')#Menu
rules = pygame.image.load('rules.png')#Rules
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
menu_buttons= [(851,28,110,70)]
roll = pygame.Rect(210,280,70,70)
option_rect = [roll,(0,0,35,35),(0,70,35,35),(420,490,70,70),(70,490,70,70),(280,350,70,70),(210,210,70,70),(490,70,70,70),(420,0,70,70),(70,0,70,70),(0,280,70,70),(490,490,70,70),(210,350,70,70),(280,210,70,70),(490,0,70,70),(0,490,70,70),(0,0,70,70),(0,140,70,70),(140,0,70,70),(490,140,70,70),(140,210,70,70),(350,350,70,70),(140,490,70,70),(600,8,380,550),(210,490,35,35),(490,420,35,35),(420,350,35,35),(490,210,35,35),(210,0,35,35),(0,420,35,35),(0,210,35,35),(0,70,35,35),(280,0,35,35),(420,210,35,35),(140,280,35,35),(280,490,35,35),(0,350,35,35),(350,0,35,35),(350,210,35,35),(140,350,35,35),(490,350,35,35),(350,490,35,35)]
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

def question_pop_up(money):
    pressed = pygame.key.get_pressed()
    global start_money 
    global money_earned
    global money_invested
    global money_saved
    if pressed[pygame.K_m]:
        gameDisplay.blit(menu,(90,170))
    if pressed[pygame.K_r]:
        gameDisplay.blit(rules,(90,170))
#darkblue donate
    if pressed[pygame.K_RETURN]:
        for rect in option_rect:
            if select_rect.colliderect(rect):
                if rect == (0,350,35,35):
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
                    if pressed[pygame.K_a]:
                        start_money-=money_earned
                if rect ==(350,0,35,35):
                    gameDisplay.blit(square1,(0,140))
                    font = pygame.font.SysFont(None, 40)
                    customText1 ='You can Donate time or money.'
                    customText2 ='Which would you like to donate to?'
                    customText3 ='A-Donate money to local shelter'
                    customText4 ='B-Donate time reading to third'
                    customText5 ='grader at your school.'
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
                    if pressed[pygame.K_a]:
                        start_money-=money_earned
                if rect ==(350,210,35,35):
                    gameDisplay.blit(square1,(0,140))
                    font = pygame.font.SysFont(None, 40)
                    customText1 ='You can Donate time or money.'
                    customText2 ='Which would you like to donate to?'
                    customText3 ='A-Donate money to the homless'
                    customText4 ='B-Donate time in your local'
                    customText5 ='soup kitchen.'
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
                    if pressed[pygame.K_a]:
                        start_money-=money_earned
                if rect ==(140,350,35,35):
                    gameDisplay.blit(square1,(0,140))
                    font = pygame.font.SysFont(None, 40)
                    customText1 ='You can Donate time or money.'
                    customText2 ='Which would you like to donate to?'
                    customText3 ='A-Donate money to local food pantry'
                    customText4 ='B-Donate time helping your teacher'
                    customText5 ='clean the classroom.'
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
                    if pressed[pygame.K_a]:
                        start_money-=money_earned
                if rect ==(490,350,35,35):
                    gameDisplay.blit(square1,(0,140))
                    font = pygame.font.SysFont(None, 40)
                    customText1 ='You can Donate time or money.'
                    customText2 ='Which would you like to donate to?'
                    customText3 ='A-Donate money to help your school.'
                    customText4 ='B-Donate time helping in the'
                    customText5 ='hospital.'
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
                    if pressed[pygame.K_a]:
                        start_money-=money_earned
                if rect ==(350,490,35,35):
                    gameDisplay.blit(square1,(0,140))
                    font = pygame.font.SysFont(None, 40)
                    customText1 ='You can Donate time or money.'
                    customText2 ='Which would you like to donate to?'
                    customText3 ='A-Donate money to save the Rain Forest'
                    customText4 ='B-Donate time cleaing local Park.'
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
                    if pressed[pygame.K_a]:
                        start_money-=money_earned
#qmark                   
                elif rect ==(280,490,35,35):
                    gameDisplay.blit(square1,(0,140))
                    font = pygame.font.SysFont(None, 40)
                    customText1 ='Oh NO!! You lost your cell phone.'
                    customText2 ='Pay your deductable. -$40'
                    text1 = font.render(customText1, True, white)
                    text2 = font.render(customText2, True, white)
                    gameDisplay.blit(text1,(10,160))
                    gameDisplay.blit(text2,(10,200))
                    if pressed[pygame.K_SPACE]:
                        start_money -= 40
                elif rect == (280,0,35,35):
                    gameDisplay.blit(square1,(0,140))
                    font = pygame.font.SysFont(None, 40)
                    customText1 ='You made an "A" on your last exam'
                    customText2 ='you get a bonus on your allowance $50'
                    text1 = font.render(customText1, True, white)
                    text2 = font.render(customText2, True, white)
                    gameDisplay.blit(text1,(10,160))
                    gameDisplay.blit(text2,(10,200))
                    if pressed[pygame.K_SPACE]:
                        start_money += 50
                elif rect == (420,210,35,35):
                    gameDisplay.blit(square1,(0,140))
                    font = pygame.font.SysFont(None, 40)
                    customText1 ="It's Lundry day and you found"
                    customText2 ='$10 in the dryer.'
                    text1 = font.render(customText1, True, white)
                    text2 = font.render(customText2, True, white)
                    gameDisplay.blit(text1,(10,160))
                    gameDisplay.blit(text2,(10,200))
                    if pressed[pygame.K_SPACE]:
                        start_money += 10
                elif rect == (140,280,35,35):
                    gameDisplay.blit(square1,(0,140))
                    font = pygame.font.SysFont(None, 40)
                    customText1 ='Oops!! You went over on data.'
                    customText2 ='Pay your parents $30.'
                    text1 = font.render(customText1, True, white)
                    text2 = font.render(customText2, True, white)
                    gameDisplay.blit(text1,(10,160))
                    gameDisplay.blit(text2,(10,200))
                    if pressed[pygame.K_SPACE]:
                        start_money -= 30
#Start Square
                elif rect ==(0,0,35,35):
                            gameDisplay.blit(square1,(0,140))
                            font = pygame.font.SysFont(None, 40)
                            customText1 ='''Welcome to TechSuppork's "Money''' 
                            customText2 ='''Savvy Game!" Let's Get started!'''
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

#endgame square
                elif rect ==(0,70,35,35):
                    gameDisplay.blit(square1,(0,140))
                    font = pygame.font.SysFont(None, 40)
                    customText1 ="You have Finished the Game!!!YAY!!" 
                    customText3 ="Play again and try and beat your"
                    customText4 ="score!! Or dare someone else!!"
                    customText5 ='Until next time. TechSuppork out!!'
                    text1 = font.render(customText1, True, white)
                    text2 = font.render('With $'+str(money_saved+money_invested+start_money), True, white)
                    text3 = font.render(customText3, True, white)
                    text4 = font.render(customText4, True, white)
                    text5 = font.render(customText5, True, white)

                    gameDisplay.blit(text1,(10,160))
                    gameDisplay.blit(text2,(10,200))
                    gameDisplay.blit(text3,(10,240))
                    gameDisplay.blit(text4,(10,280))
                    gameDisplay.blit(text5,(10,320))
#payday                    
                elif rect == (210,490,35,35):
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
                    if pressed[pygame.K_a]:
                        start_money+= 40
                elif rect == (490,420,35,35):
                    gameDisplay.blit(square1,(0,140))
                    font = pygame.font.SysFont(None, 40)
                    customText1 ='You are AAmazing.'
                    customText2 ='Here is $100 just for being you.'
                    text1 = font.render(customText1, True, white)
                    text2 = font.render(customText2, True, white)
                    gameDisplay.blit(text1,(10,160))
                    gameDisplay.blit(text2,(10,200))
                    if pressed[pygame.K_a]:
                        start_money+= 100
                elif rect == (420,350,35,35):
                    gameDisplay.blit(square1,(0,140))
                    font = pygame.font.SysFont(None, 40)
                    customText1 ='Which of these is a form of Investing'
                    customText2 ='money?'
                    customText3 ='A- Buying Stock'
                    customText4 ='B- Put money to the side'
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
                    if pressed[pygame.K_a]:
                        start_money+= 40
                elif rect == (490,210,35,35):
                    gameDisplay.blit(square1,(0,140))
                    font = pygame.font.SysFont(None, 40)
                    customText1 ='Which of these is a form of Saving.'
                    customText2 ='A- Putting money in Bank.'
                    customText3 =''
                    customText4 ='B- Buying a share of stock.'
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
                    if pressed[pygame.K_a]:
                        start_money+= 40
                elif rect == (210,0,35,35):
                    gameDisplay.blit(square1,(0,140))
                    font = pygame.font.SysFont(None, 40)
                    customText1 ='Whic of these is a good spending habit?'
                    customText2 ='A- Buying things you need!'
                    customText3 =''
                    customText4 ='B- Going to the Arcade.'
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
                    if pressed[pygame.K_a]:
                        start_money+= 40
                elif rect == (0,420,35,35) or rect == (0,210,35,35):
                    gameDisplay.blit(square1,(0,140))
                    font = pygame.font.SysFont(None, 40)
                    customText1 ='What is a bad spending habbit?'
                    customText2 ='A- Buying junk food.'
                    customText3 =''
                    customText4 ='B- Buying school supplies.'
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
                    if pressed[pygame.K_a]:
                        start_money+= 40
                elif rect == (0,210,35,35):
                    gameDisplay.blit(square1,(0,140))
                    font = pygame.font.SysFont(None, 40)
                    customText1 ='Buying a home is a form of?'
                    customText2 ='A- Investing'
                    customText3 =''
                    customText4 ='B- Saving'
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
                    if pressed[pygame.K_a]:
                        start_money+= 40

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
                    if pressed[pygame.K_a]:
                        start_money-= 50
                        money_invested+= 50
                        

#red spend      
                elif rect == (490,490,70,70) or rect == (210,350,70,70) or rect == (280,210,70,70) or rect == (490,0,70,70) or rect == (0,490,70,70):
                    gameDisplay.blit(square1,(0,140))
                    font = pygame.font.SysFont(None, 35)
                    customText1 ='Spending: pay out (money) in buying or'
                    customText2 ='hiring goods or services'
                    customText3 ='Would You like to purchase a badge?'
                    customText4 ='A. The Game Console for $600'
                    customText5 ='B. The Puppy for $900'
                    customText6 ='C. The Bike for $390'
                    customText7 ='D. The Smart Phone for $950'
                    customText8 ='E. The Tablet for $800'
                    customText9 ='F. No not now.'

                    text1 = font.render(customText1, True, white)
                    text2 = font.render(customText2, True, white)
                    text3 = font.render(customText3, True, yellow)
                    text4 = font.render(customText4, True, white)
                    text5 = font.render(customText5, True, white)
                    text6 = font.render(customText6, True, white)
                    text7 = font.render(customText7, True, white)
                    text8 = font.render(customText8, True, white)
                    text9 = font.render(customText9, True, white)

                    gameDisplay.blit(text1,(10,160))
                    gameDisplay.blit(text2,(10,195))
                    gameDisplay.blit(text3,(10,230))
                    gameDisplay.blit(text4,(10,265))
                    gameDisplay.blit(text5,(10,300))
                    gameDisplay.blit(text6,(10,335))
                    gameDisplay.blit(text7,(10,370))
                    gameDisplay.blit(text8,(10,405))
                    gameDisplay.blit(text9,(10,440))
                    if pressed[pygame.K_a]:
                        start_money -= 600
                    elif pressed[pygame.K_b]:
                        start_money-= 900
                    elif pressed[pygame.K_c]:
                        start_money-=390
                    elif pressed[pygame.K_d]:
                        start_money-= 950
                    elif pressed[pygame.K_e]:
                        start_money-=800
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
                    if pressed[pygame.K_a]:
                        start_money-= 50
                        money_saved+= 50
                    elif pressed[pygame.K_b]:
                        start_money-= 100
                        money_saved+= 100
                        

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
    pygame.draw.rect(gameDisplay, blue, (155,110,280,50))

#white outline for all the squares
    pygame.draw.rect(gameDisplay,white, (210,280,70,70,),2)#area for the dice
    pygame.draw.rect(gameDisplay, white, (0,0,70,70),2)
    pygame.draw.rect(gameDisplay, white, (0,70,70,70),2)
    pygame.draw.rect(gameDisplay, white, (0,140,70,70),2)
    pygame.draw.rect(gameDisplay, white, (0,210,70,70),2)
    pygame.draw.rect(gameDisplay, white, (0,280,70,70),2)
    pygame.draw.rect(gameDisplay, white, (0,350,70,70),2)
    pygame.draw.rect(gameDisplay, white, (0,420,70,70),2)
    pygame.draw.rect(gameDisplay, white, (0,490,70,70),2)
    pygame.draw.rect(gameDisplay, white, (70,0,70,70),2)
    pygame.draw.rect(gameDisplay, white, (140,0,70,70),2)
    pygame.draw.rect(gameDisplay, white, (210,0,70,70),2)
    pygame.draw.rect(gameDisplay, white, (280,0,70,70),2)
    pygame.draw.rect(gameDisplay, white, (350,0,70,70),2)
    pygame.draw.rect(gameDisplay, white, (420,0,70,70),2)
    pygame.draw.rect(gameDisplay, white, (490,0,70,70),2)
    pygame.draw.rect(gameDisplay, white, (490,70,70,70),2)
    pygame.draw.rect(gameDisplay, white, (490,140,70,70),2)
    pygame.draw.rect(gameDisplay, white, (490,210,70,70),2)
    pygame.draw.rect(gameDisplay, white, (420,210,70,70),2)
    pygame.draw.rect(gameDisplay, white, (350,210,70,70),2)
    pygame.draw.rect(gameDisplay, white, (280,210,70,70),2)
    pygame.draw.rect(gameDisplay, white, (210,210,70,70),2)
    pygame.draw.rect(gameDisplay, white, (140,210,70,70),2)
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
    pygame.draw.rect(gameDisplay, white, (155,110,280,50),5)
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos= pygame.mouse.get_pos()
                for rect in menu_buttons:
                    if rect == (851,28,110,70):
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
            select_rect.x,select_rect.y= x,y
        x+= x_change
        y+= y_change
        board()
        player(x,y)
        dice_roll()
        global start_money
        if not question_pop_up(start_money) == None:
            start_money = question_pop_up(start_money)
            money_invested = 50
        if x > 600 - Player_width or x < 0:
            dead = False
        elif y >625-player_height or y<0:
            dead = False
        pygame.display.update()
        clock.tick(60)
def start_game():
    start = False

    while not start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = True

            if True:
                gameDisplay.blit(splash,(0,0))
               
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_loop()            
        pygame.display.update()
        clock.tick(60)
        
start_game()
pygame.quit()
quit()
