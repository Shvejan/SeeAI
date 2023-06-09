import cv2
import numpy as np
import pickle
import os
import webbrowser
face_cas = cv2.CascadeClassifier('C:\my files\ece-hackathon\cassFiles\haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
os.chdir('C:\my files\ece-hackathon')
recognizer.read("traied.yml")
lables = {}
with open("lables.pickle", 'rb') as f:
    lables = pickle.load(f)
    lables = {v:k for k,v in lables.items()}

unk = []

cap = cv2.VideoCapture(0)
while(1):
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cas.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roicolor = frame[y:y+h, x:x+w]
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,255,0),2)
        id,conf = recognizer.predict(roi_gray)
        font = cv2.FONT_HERSHEYDUPLEX
        if(conf>=60 and conf<=85):
            print(lables[id])
            name = lables[id_]
            cv2.putText(frame, name,(x,y), font, 1, (255,0,0), 2 )
            unk.clear()

        else:

            #cv2.putText(frame, "unknown",(x,y), font, 1, (0,0,255), 2 )
            print("unknown")
            unk.append("unknown")

            if len(unk)>20:
                cv2.putText(frame, "unknown",(x,y), font, 1, (0,0,255), 2 )
                webbrowser.open('192.168.4.1/one')
                unk.clear()


    cv2.imshow('vdo', frame)
    if(cv2.waitKey(1) == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()