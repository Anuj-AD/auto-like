#code here
#program to upvote answers on quora using chrome browser
import webbrowser
import pyautogui as pag
import cv2
import imutils
import numpy as np
import time

url = 'https://www.quora.com/' #our website
path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s' #path of chrome
webbrowser.get(path).open(url) #open website on chrome
time.sleep(3) #due to poor connection, webpage may take time to load
image = pag.screenshot("ss.png") #take screenshot
image = cv2.imread("ss.png")
#cv2.imshow("Screenshot",imutils.resize(image, width = 400)) #to check the screenshot
#cv2.waitKey(0)
logoLocation = pag.locateOnScreen('logo.png', confidence = 0.9)
logoPoint = pag.center(logoLocation)
pag.moveTo(logoPoint)
time.sleep(3)
timeout = time.time() + 60*5 #5 minute
while True:
    time.sleep(0.5)
    print(1)
    if time.time() > timeout: 
        break
    pag.scroll(-200)
    image = pag.screenshot("ss.png") #take screenshot
    image = cv2.imread("ss.png")
    likeLocation = pag.locateOnScreen('like.png', confidence = 0.9)
    if likeLocation != None:
        likePoint = pag.center(likeLocation)
        pag.moveTo(likePoint)
        pag.click()
