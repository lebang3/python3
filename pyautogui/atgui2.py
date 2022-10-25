import pyautogui



# pyautogui.sleep(5)
# print(pyautogui.position())
pyautogui.click(x=731, y=1045)
pyautogui.moveTo(x=719, y=500)
distance = 200
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.5)   # move right
    distance -= 5
    pyautogui.drag(0, distance, duration=0.5)   # move down
    pyautogui.drag(-distance, 0, duration=0.5)  # move left
    distance -= 5
    pyautogui.drag(0, -distance, duration=0.5)  # move up


pyautogui.sleep()#tam dung
pyautogui.displayMousePosition()#vi tri con tro chuot theo thoi gian thuc
print(pyautogui.position()) #hien thi vi tri hien tai cua con chuot
pyautogui.click() #click chuot tai vi tri
pyautogui.moveTo() #di chuyen den 
pyautogui.keyDown('ctrl') #giu phim 
pyautogui.keyUp('ctrl') # tha phim
pyautogui.write('') #go ki tu tuong uong
pyautogui.press('enter') #nhan phim 
pyautogui.doubleClick() #nhan 2 lan
pyautogui.hotkey('alt' , 'tab') #su dung phim long to hop phim