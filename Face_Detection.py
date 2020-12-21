import numpy as np
import cv2


#Define face and eye classifier.
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 
eye_cascade=cv2.CascadeClassifier("haarcascade_eye.xml")
cap=cv2.VideoCapture(0)

while True:
    RET,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,4)
    
      #define face in down loop.
     
      #define face as x and y axis in this loop.
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),4)  #Use rengtangle for defining face but you should circle.
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=img[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray)
        i=0
        for(ex,ey,ew,eh) in eyes: #define eye as x and y axis in this loop.
          cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),4) #Use rengtangle for defining eye but you should circle. 
          i+=1
          if(i==2): #This station is important because people just have two eyes.
              break

      
        #This loop printed Defining face and eye.
        while True:
           cv2.imshow("Face Detection",img)
           if cv2.waitKey(30) & 0xff:
               break


  





cap.release()
cv2.destroyAllWindows()
       








   











  
    


        







