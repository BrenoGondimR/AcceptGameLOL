import pyautogui
import time
import cv2
import keyboard

time.sleep(2)
i = 0
while keyboard.is_pressed('q') == False:
    if pyautogui.locateOnScreen('teste.png', confidence=0.5):
        print('vendo')
        time.sleep(1)
        pyautogui.click('teste.png')
    else:
        print('nao apareceu ainda')
        time.sleep(1)

    if keyboard.is_pressed('q') == True:
        exit()





