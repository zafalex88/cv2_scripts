import cv2

def ask_for_tracker():
    print("Welcome! What Tracker API would you like to use?")
    print("Enter 0 for BOOSTING: ")
    print("Enter 1 for MIL: ")
    print("Enter 2 for KCF: ")
    print("Enter 3 for TLD: ")
    print("Enter 4 for MEDIANFLOW: ")
    choice = input("Please select your tracker: ")
    
    if choice == '0':
        tracker = cv2.TrackerBoosting_create()
    if choice == '1':
        tracker = cv2.TrackerMIL_create()
    if choice == '2':
        tracker = cv2.TrackerKCF_create()
    if choice == '3':
        tracker = cv2.TrackerTLD_create()
    if choice == '4':
        tracker = cv2.TrackerMedianFlow_create()
    
    return tracker

tracker = ask_for_tracker()
tracker_name = str(tracker).split()[0][1:]

#read video
cap = cv2.VideoCapture(0)

#read first frame
ret, frame = cap.read()
#function that allows us to draw on the very first frame of desired ROI
roi = cv2.selectROI(frame, False)

#Initiate tracker with first frame and bouning box
ret = tracker.init(frame,roi)

while True:
    #read a new frame
    ret, frame = cap.read()
    
    #update tracker
    success, roi = tracker.update(frame)
    
    #roi variable is a tuple of 4 floats
    #we need each value and we need them as integers
    (x,y,w,h) = tuple(map(int,roi))
    
    #draw rectangle as tracker moves
    if success:
        #tracking success
        p1 = (x,y)
        p2 = (x+w,y+h)
        cv2.rectangle(frame, p1, p2, (0,255,0), 3)
    else:
        #tracking fails
        cv2.putText(frame,"Failure to Detect tracking!", (100,200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 3)
    
    #Display tracker type on frame
    cv2.putText(frame, tracker_name, (20,400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)
    
    #display result
    cv2.imshow(tracker_name, frame)
    
    #exit if Esc is pressed
    k = cv2.waitKey(10) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()