import cv2

#Doc anh

image = cv2.imread("anh\\bien_so.jpg")

#Tao anh xam

anh_xam = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#Tao nguong

ret , nguong = cv2.threshold(anh_xam,50,255,cv2.THRESH_BINARY)
cv2.imshow("Nguong",nguong)

#Dem duoc so hinh lap phuong
contours , _ = cv2.findContours(nguong,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
dem = 0
MIN_HEIGHT = image.shape[0] * 0.2
MAX_WIDTH = image.shape[1] * 0.4
for cnt in contours[:-1]:
    #Lay toa do hinh chu nhat bao quanh duong bien
    x,y,w,h = cv2.boundingRect(cnt)
    if w <= MAX_WIDTH and h >= MIN_HEIGHT:
        dem+=1
        crop_number = image[y:y+h , x:x+w]
        cv2.imwrite("number\\{}.png".format(dem),crop_number)
        cv2.drawContours(image , [cnt],-1,(0,255,0),2,cv2.LINE_AA)
    
cv2.imshow("Anh",image)
cv2.waitKey()
