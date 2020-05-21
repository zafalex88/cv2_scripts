#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


#load the face_cascade xml
face_cascade = cv2.CascadeClassifier("./haarcascades/haarcascade_frontalface_default.xml")


# In[3]:


#creating face detection and rectangle around it function
def detect_face(vid):
    #detect face on video with classifier    
    face_rects = face_cascade.detectMultiScale(vid)
    
    #draw rectangle in the coordinates on which face is detected
    for (x,y,w,h) in face_rects:
        cv2.rectangle(vid,(x,y),(x+w,y+h),(255,255,255),10)
    
    return vid


# In[4]:


#load camera and use detect face function on video

cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read(0)
    face_rec = detect_face(frame)
    cv2.imshow("VIDEO FACE DETECT", face_rec)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

#close camera and all windows when Esc is pressed
cap.release()
cv2.destroyAllWindows()

