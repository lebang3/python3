import pyautogui

# print(pyautogui.position())   #x=726, y=57

pyautogui.sleep(15)
pyautogui.click(x=726, y=57)
for i in range(30):
    pyautogui.write('')
    pyautogui.press('enter')
    pyautogui.sleep(20)
    pyautogui.hotkey('ctrl','w')
    pyautogui.sleep(20)
    print(i)