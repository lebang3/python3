import pyautogui
# pyautogui.sleep(5)
# print(pyautogui.position())
pyautogui.hotkey('window','s')
pyautogui.write('vẽ')
pyautogui.press('enter')
distance = 200
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.5)   
    distance -= 5
    pyautogui.drag(0, distance, duration=0.5)  
    pyautogui.drag(-distance, 0, duration=0.5)  
    pyautogui.drag(0, -distance, duration=0.5)  