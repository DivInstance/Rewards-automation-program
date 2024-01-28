import pyautogui
import time

from wonderwords import RandomWord
r = RandomWord()

pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.keyUp('alt')

time.sleep(1)

for i in range(42):
    res = r.word() 

    pyautogui.keyDown('ctrl')
    pyautogui.press('e')
    pyautogui.keyUp('ctrl')

    time.sleep(6)
    pyautogui.write(res)

    pyautogui.press('enter')

    time.sleep(0)









