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
                ['pill','time',[pillboxHoles],'Priority','Back'],\
            [['Set Alarm']],\
            [['Emergency Contacts'],\
                ['Mary Stieber','212-435-2398','mary@example.com','123 Madeline Way','Back'],\
                ['John Adams','800-342-7734','adams@apples.org','77 High St','Back'],\
                ['Back']], \
            [['Change Contacts'],\
                ['New Contact','Back'],\
                ['Delete Contact','Back'],\
                ['Back']], \
            [['Settings'],\
                ['Screen Color','White','Cyan','Yellow','Orange','Purple','Blue','Back'],\
                ['Volume:   0','Increase','Lower','Silent','Back'],\
                ['Vibration','On','Off','Back'],['Back']], \
            [['Back']]]

volume = 0
newContact = [0]*5

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

def textInput(str,alphabet,length):
    alphabet = alphabet + '>'
    output = ''
    inside = 0
    pos = 0
    while True:
        os.system('cls')
        print(str)
        print(output)
        i = 0
        while i < len(alphabet):
            if i == pos: sys.stdout.write('#')
            else: sys.stdout.write(alphabet[i])
            if i % length == length-1: sys.stdout.write('\n')
            i += 1
        ask = input()
        if ask == 'q' and inside:
            if pos % length == length-1: pos -= length-1 ; inside = 0
            else: pos += 1
        if ask == 'q' and not inside:
            pos += length
            if pos > len(alphabet): pos = 0
        if ask == 'w' and inside:
            if alphabet[pos] == '>': break
            else: output = output + alphabet[pos]
        if ask == 'w' and not inside: inside = 1
    return output

def addContact():
    newContact[0] = textInput('Name',' ABCDEFGHIJKLMNOPQRSTUVWXYZ',8)
    newContact[1] = textInput('Phone Number', '1234567890',3)
    newContact[2] = textInput('Email',' ABCDEFGHIJKLMNOPQRSTUVWXYZ@,.-',8)
    newContact[3] = textInput('Address',' ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',8)
    newContact[4] = 'Back'
    menuData[3].insert(1,newContact)

def updateDelContacts():
    menuData[4][2] = ['Delete Contact']
    i = 1
    while not menuData[3][i][0] == 'Back':
        menuData[4][2].append(menuData[3][i][0])
        i += 1
    menuData[4][2].append('Back')

def deleteContact(i):
    del menuData[3][i]
    updateDelContacts()

def setColor(c):
    print('Not yet done ' + str(c))

def getLevel():
    if menuState[2] != 0: return 2 
    elif menuState[1] != 0: return 1
    elif menuState[0] != 0: return 0
    else: return -1

def arrowButton():
    global level
    level = getLevel()
    if getMenuItem(2, menuState[2]) == 'Back': menuState[level] = 1
    else: menuState[level] += 1
    printMenu()

def enterButton():
    global level
    global volume
    level = getLevel()
    if getMenuItem(2, menuState[2]) == 'Back': menuState[level] = 0 ; level -= 1 #Exit a submenu
    #Put all the functions here
    elif menuState[0] == 5 and menuState[1] == 1 and not menuState[2] == 0: setColor(menuState[2])
    elif menuState == [4,1,0]: addContact()
    elif menuState[0] == 4 and menuState[1] == 2 and not menuState[2] == 0: deleteContact(menuState[2])
    elif menuState == [5,2,1] and volume < 100: volume += 10 ; menuData[5][2][0] = 'Volume:   ' + str(volume) #example changing volume
    elif menuState == [5,2,2] and volume > 0: volume -= 10 ; menuData[5][2][0] = 'Volume:   ' + str(volume)
    elif level < 2: level += 1 ; menuState[level] = 1 #Enter a submenu
    if menuState == [0,0,0]: os.system('cls') ; print('Idling...')
    else: printMenu()

updateDelContacts()

while True:

    ask = input()
    
    if ask == 'q' and menuState != [0,0,0]:arrowButton()
        
    if ask == 'w': enterButton()

#glcd.draw_string('abcdefghijklmnopqrstu', neato, 0, 24,spacing=1,invert=1)
#glcd.flip()

