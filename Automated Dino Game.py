import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    # Draw the rectangle for crows
    for i in range(310, 415):
        for j in range(410, 583):
            if data[i, j] < 100:
                hit("down")
                return

    for i in range(600, 415):
        for j in range(863, 650):
            if data[i, j] < 100:
                hit("up")
                return
    return

if __name__ == "__main__":
    print("Chrome Dino game about to start in 3 seconds")
    time.sleep(3)
    hit('up') 

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollide(data)
            
        # print(asarray(image))
        '''
        # Draw the rectangle for cactus
        for i in range(275, 325):
            for j in range(563, 650):
                data[i, j] = 0
        
        # Draw the rectangle for birds
        for i in range(250, 300):
            for j in range(410, 563):
                data[i, j] = 171

        image.show()
        break
      '''
