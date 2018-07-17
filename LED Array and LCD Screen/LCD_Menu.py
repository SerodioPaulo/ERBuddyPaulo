#import st7565
#import xglcd_font as font
import os
import sys

#neato = font.XglcdFont('/home/pi/Pi-ST7565/fonts/Neato5x7.c', 5, 7) #5, 7 refers to the pixel size of each character. This file must exist
#glcd = st7565.Glcd(rgb=[21, 20, 16]) #Don't change these numbers
#glcd.init()

menuState = [1,0,0] #[First Item in Top Level, Not in Second Level, Not in Third Level]

menuData =  [[['ERBuddy Main Menu']],\
            [['Pill Schedule']],\
            [['Set Alarm']],\
            [['Contact Information'],['Mary Stieber','212-435-2398','mary@example.com','123 Madeline Way','Back'],['John Adams','800-342-7734','adams@apples.org','77 High St','Back'],['Back']], \
            [['Settings'],['Screen Color','White','Cyan','Yellow','Orange','Purple','Blue','Back'],['Volume:   0','Increase','Lower','Silent','Back'],['Vibration','On','Off','Back'],['Back']], \
            [['Back']]]

volume = 0
level = 0
            
def getMenuItem(L,i):
    if L == 0: return menuData[i][0][0]
    if L == 1: return menuData[menuState[0]][i][0]
    if L == 2: return menuData[menuState[0]][menuState[1]][i]

def printMenu():
    os.system('cls')
    i = 0
    while getMenuItem(level, i - 1) != 'Back' or i == 0:
        if menuState[level] == i: sys.stdout.write('#')
        print(getMenuItem(level, i))
        i += 1
        
def getLevel():
    if menuState[2] != 0: level = 2 
    elif menuState[1] != 0: level = 1
    elif menuState[0] != 0: level = 0
    else: level = -1

def arrowButton():
    getLevel()
    if getMenuItem(2, menuState[2]) == 'Back': menuState[level] = 1
    else: menuState[level] += 1
    printMenu()

def enterButton():
    getLevel()
    if getMenuItem(2, menuState[2]) == 'Back': menuState[level] = 0 ; level -= 1 #Exit a submenu
    #Put all the functions here
    #elif menuState == [4,1,1]: #set color white
    #elif menuState == [4,1,2]: #set color cyan
    #elif menuState == [4,1,3]: #set color yellow
    #elif menuState == [4,1,4]: #set color orange
    #elif menuState == [4,1,5]: #set color purple
    #elif menuState == [4,1,6]: #set color blue
    elif menuState == [4,2,1] and volume < 100: volume += 10 ; menuData[4][2][0] = 'Volume:   ' + str(volume) #example changing volume
    elif menuState == [4,2,2] and volume > 0: volume -= 10 ; menuData[4][2][0] = 'Volume:   ' + str(volume) 
    else: level += 1 ; menuState[level] = 1 #Enter a submenu
    if menuState == [0,0,0]: os.system('cls') ; print('Idling...')
    else: printMenu()
    
while True:

    ask = input()
    
    if ask == 'q' and menuState != [0,0,0]:arrowButton()
        
    if ask == 'w': enterButton()

#glcd.draw_string('abcdefghijklmnopqrstu', neato, 0, 24,spacing=1,invert=1)
#glcd.flip()

