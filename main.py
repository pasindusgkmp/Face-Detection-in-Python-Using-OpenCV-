import cv2
cap=cv2.VideoCapture(0)

cascade = cv2.CascadeClassifier("xml/haarcascade_frontalface_default.xml")

while True:
    success,frame=cap.read()
    Gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=cascade.detectMultiScale(Gray,1.3,5)

    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(225,0,0),2)
        cv2.imshow("webcam",frame)
        if cv2.waitKey(1) & 0xFF ==ord("s"):
            break

cap.release()
