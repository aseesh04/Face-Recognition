import cv2
img=cv2.VideoCapture(0)
file=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:

    ret, frame = img.read()
    imggrey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=file.detectMultiScale(imggrey,1.1,4)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(frame,'Avinash',(h+6,w-6),cv2.FONT_HERSHEY_DUPLEX,1.0,(255,0,0),2)
    cv2.imshow("image",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
img.release()
cv2.destroyAllWindows()