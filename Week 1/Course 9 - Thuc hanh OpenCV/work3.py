import cv2

nhan_dien= cv2.CascadeClassifier("anh\\haarcascade_frontalface_default.xml")

cam = cv2.VideoCapture(0)
while True:
    ret , frame = cam.read()
    if ret:
        anh_xam = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = nhan_dien.detectMultiScale(anh_xam,scaleFactor= 1.05,minNeighbors=5 , minSize=(30,30))

        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        print("So khuon mat la :",len(faces))
        cv2.imshow("Webcam",frame)

    phim_bam = cv2.waitKey(1)
    if phim_bam == ord('q'):
        break
    elif phim_bam  == ord('s'):
        #luu anh
        dem = 0
        for (x,y,w,h) in faces:
            crop_frame = frame[y:y+h,x:x+w]
            cv2.imwrite(f"faces\\{dem}.png",crop_frame)
            dem+=1

cv2.destroyAllWindows()


