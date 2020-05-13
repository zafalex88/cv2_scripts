#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2

#CALLBACK FUNCTION FOR DRAWING
def drawing(event,x,y,flags,param):
    global pt1,pt2,topLeft_clicked,botRight_clicked,clicked,center
    if event == cv2.EVENT_LBUTTONDOWN:
        #RESET THE RECTANGLE (IT CHECKS IF RECT IS THERE)
        if topLeft_clicked == True and botRight_clicked == True:
            pt1 = (0,0)
            pt2 = (0,0)
            topLeft_clicked = False
            botRight_clicked = False
        #DRAW RECTANGLE (first click)
        if topLeft_clicked == False:
            pt1 = (x,y)
            topLeft_clicked = True
        #second click
        elif botRight_clicked == False:
            pt2 = (x,y)
            botRight_clicked = True
    #get coordinates for the circle center on click 
    if event == cv2.EVENT_RBUTTONDOWN:
        center = (x,y)
        clicked = False
    #when we release the button then clicked is true and the circle is drawn
    if event == cv2.EVENT_RBUTTONUP:
        clicked = True

#GLOBAL VARIABLES
pt1 = (0,0)
pt2 = (0,0)
topLeft_clicked = False
botRight_clicked = False
center = (0,0)
clicked = False

#CONNECT TO CALLBACK
cap = cv2.VideoCapture(0)
cv2.namedWindow('Test')
cv2.setMouseCallback('Test',drawing)

while True:
    ret, frame = cap.read()
    
    #DRAWING ON THE FRAME BASED ON GLOBAL VARIABLES
    if topLeft_clicked:
        cv2.circle(frame,center=pt1,radius=3,color=(0,0,255),thickness=-1)
    if topLeft_clicked and botRight_clicked:
        cv2.rectangle(frame,pt1,pt2,(0,0,255),3)
    if clicked:
        cv2.circle(frame,center,50,color=(255,0,0),thickness=5)
    
    cv2.imshow('Test',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()


# In[ ]:




