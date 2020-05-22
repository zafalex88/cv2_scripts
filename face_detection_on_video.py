import cv2

face_cascade = cv2.CascadeClassifier("./haarcascades/haarcascade_frontalface_default.xml")

#creating face detection and rectangle around it function
def detect_face(vid):
    #detect face on video with classifier    
    face_rects = face_cascade.detectMultiScale(vid,scaleFactor=1.2,minNeighbors=5)
    #draw rectangle in the coordinates on which face is detected
    for (x,y,w,h) in face_rects:
        cv2.rectangle(vid,(x,y),(x+w,y+h),(255,255,255),10) 
    
    return vid

#load camera and use detect face function on video
cap = cv2.VideoCapture(0)

while True:
    #read camera input
    ret, frame = cap.read(0)
    #run function on frame
    face_rec = detect_face(frame)
    #window name and function
    cv2.imshow("VIDEO FACE DETECT", face_rec)
    #close camera and all windows when Esc is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()