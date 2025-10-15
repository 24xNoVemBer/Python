import cv2

#Doc anh
imgage = cv2.imread("anh\\lap_phuong.jpg")

#Tao anh xam
anh_xam = cv2.cvtColor(imgage,cv2.COLOR_BGR2GRAY)

#Tao nguong
ret , nguong = cv2.threshold(anh_xam,230 , 255,cv2.THRESH_BINARY)
cv2.imshow("Nguong",nguong)
#Dem duoc so hinh lap phuong
contours , _ = cv2.findContours(nguong,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
dem = 0
MIN_AREA = imgage.shape[1] * imgage.shape[0] / 150
for cnt in contours[:-1]:
    if cv2.contourArea(cnt) >= MIN_AREA:
        dem+=1
        cv2.drawContours(imgage , [cnt],-1,(0,255,0),2,cv2.LINE_AA)
    cv2.imshow("GOC",imgage)
#Dem duong bao
print("So bong la : " , dem)




cv2.waitKey()