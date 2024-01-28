import pyautogui
import time
from wonderwords import RandomWord

r = RandomWord()

time.sleep(1)

pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.keyUp('alt')

time.sleep(1)

pyautogui.keyDown('ctrl')
pyautogui.press('e')
pyautogui.keyUp('ctrl')


res = r.word()
pyautogui.typewrite(res)
pyautogui.press('enter')
time.sleep(1)

for i in range (1, 165):
    time.sleep(1)
    pyautogui.keyDown('ctrl')
    pyautogui.press('e')
    pyautogui.keyUp('ctrl')
    res = r.word()
    pyautogui.typewrite(res)
    time.sleep(1)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    for j in range (1, 6):
        pyautogui.press('tab')
    pyautogui.keyUp('alt')
