#program to upvote answers on quora using chrome browser
import webbrowser
import pyautogui as pag
import cv2
import imutils
import numpy as np
import time
from random import randint

url = 'https://www.instagram.com/' #our website
path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s' #path of chrome
webbrowser.get(path).open(url) #open website on chrome
time.sleep(3)
image = pag.screenshot("ss.png") #take screenshot
image = cv2.imread("ss.png")
#cv2.imshow("Screenshot",imutils.resize(image, width = 400)) #to check the screenshot
#cv2.waitKey(0)
logoLocation = pag.locateOnScreen('logo.png', confidence = 0.9)
logoPoint = pag.center(logoLocation)
pag.moveTo(logoPoint)
time.sleep(3)
timeout = time.time() + 60 #1 minute
while True:
    rand1 = randint(600,800)/1000   
    time.sleep(rand1)
    print(1)
    if time.time() > timeout: 
        break
    rand2 = randint(150,250)
    pag.scroll(-rand2)
    image = pag.screenshot("ss.png") #take screenshot
    image = cv2.imread("ss.png")
    likeLocation = pag.locateOnScreen('like.png', confidence = 0.9)
    if likeLocation != None:
        likePoint = pag.center(likeLocation)
        pag.moveTo(likePoint)
        pag.click()
        rand3 = randint(10,30)/30
        time.sleep(rand3)
