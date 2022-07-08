import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import pandas as pd
import cv2
import urllib.request
import numpy as np
import os
from datetime import datetime
import face_recognition
##########################
# For buzzer -----------------
import RPi.GPIO as GPIO
from time import sleep
#Disable warnings (optional)
GPIO.setwarnings(False)
#Select GPIO mode
GPIO.setmode(GPIO.BCM)
#Set buzzer - pin 23 as output
buzzer=23 
GPIO.setup(buzzer,GPIO.OUT)
redlight = 22
greenlight = 27
##########################

from email.quoprimime import body_check
from PIL import Image
import requests
import base64
import time
#########################
import urllib.request
#url1 = "https://iot-door-lock-system.herokuapp.com/img"
#########################
#
path = "/home/pi/Desktop/face_detect/DoorLockUnlock/image_folder"
# url = 'http://192.168.135.71' #/cam-hi.jpg'
url = r"http://192.168.214.71/capture?_cb=1649673650721.jpg"
##'''cam.bmp / cam-lo.jpg /cam-hi.jpg / cam.mjpeg '''
print(os.listdir())
# if 'Attendance.csv' in os.listdir(os.path.join(os.getcwd(), 'attendace')):
if 'EntryTime.csv' in os.listdir():
    print("there iss..")
    # os.remove("Attendance.csv")
else:
    df = pd.DataFrame(list())
    df.to_csv("EntryTime.csv")


images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def markAttendance(name):
    with open("EntryTime.csv", 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                dtString = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dtString}')


encodeListKnown = findEncodings(images)
print('Encoding Complete')

#cap = cv2.VideoCapture(0)

while True:

    #success, img = cap.read()
    print(url)
    img_resp = urllib.request.urlopen(url)
    imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
    img = cv2.imdecode(imgnp, -1)
    # print(img)
    # im = cv.LoadImage(url)
    # a = np.asarray(img)
    # cv2.imshow(a)
# img = captureScreen()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    imgS = img
    # cv2.imshow(imgS)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
# print(faceDis)
        matchIndex = np.argmin(faceDis)
        if matches[matchIndex]:
            #print(matchIndex)
            name = classNames[matchIndex].upper()
            
            print(name)
            
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2),
                          (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name)
            
            i = 0
            while i<5:
                i = i+1
                GPIO.output(buzzer,GPIO.HIGH)
                #GPIO.output(greenlight,GPIO.HIGH)
                print ("Beep")
                print ("ENTER")
                sleep(0.5) # Delay in seconds
                GPIO.output(buzzer,GPIO.LOW)
                #GPIO.output(greenlight,GPIO.LOW)
                print ("No Beep")
                sleep(0.5)
            
        else:
            
            print("Not Match\n")
            
            #save image
            urllib.request.urlretrieve(url, "test.jpg")
            
            ##sending image part
            with open("test.jpg", "rb") as img_file:
                my_string = base64.b64encode(img_file.read())

            url1 = 'https://iot-door-lock-system.herokuapp.com/send'

            r = requests.post('https://iot-door-lock-system.herokuapp.com/send', json={
                "Id": 78912,
                "Customer": "Unknown",
                "Quantity": 1,
                "Price": 18.00,
                "file": my_string.decode("utf-8")
            })
            print(r.text)
            
            time.sleep(20)
            ##
            
            ##check
            url1 = 'https://iot-door-lock-system.herokuapp.com/doorstate'
            response = requests.get(url1)
            data = response.json()
            print(data['msg'])
            if(data['msg']=="NO"):
                #don't open raspberry pi
                i = 0
                GPIO.output(buzzer,GPIO.HIGH)
                
                while i<5:
                    i = i+1
                    #GPIO.output(redlight,GPIO.HIGH)
                    print ("Beep")
                    print ("STOP")
                    sleep(0.5) # Delay in seconds
                    #GPIO.output(redlight,GPIO.LOW)
                    print ("No Beep")
                    sleep(0.5)
                    
                GPIO.output(buzzer,GPIO.LOW)
            else:
                #open open the door or buzz the buzzer    
                i = 0
                while i<5:
                    i = i+1
                    GPIO.output(buzzer,GPIO.HIGH)
                    #GPIO.output(greenlight,GPIO.HIGH)
                    print ("Beep")
                    print ("ENTER")
                    sleep(0.5) # Delay in seconds
                    GPIO.output(buzzer,GPIO.LOW)
                    #GPIO.output(greenlight,GPIO.LOW)
                    print ("No Beep")
                    sleep(0.5)
                
            ##
            
            ##set again to false
            url1 = 'https://iot-door-lock-system.herokuapp.com/changedoorstate'
            r = requests.post(url1, json={
                "msg": "NO",
            })
            print(r.text)
            ##
            

    cv2.imshow('ESPCAM32', imgS)
    key = cv2.waitKey(5)
    if key == ord('q'):
        break
cv2.destroyAllWindows()
cv2.imread
