import pyautogui # type: ignore
while True:
    x, y = pyautogui.position()
    color = pyautogui.pixel(x,y)
    print('>>> andando >>>', end='/r')
    if(color[0] > 100):
        print('*** PULA *** >>>', end='/r')
        pyautogui.press('space')