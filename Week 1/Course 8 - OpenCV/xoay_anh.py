import cv2
import imutils

anh_doc_tu_file = cv2.imread("anh\\sample.jpg")

#Show anh

cv2.imshow("The Forest",anh_doc_tu_file)

#Xoay anh

anh_xoay = imutils.rotate(anh_doc_tu_file , 90)

#Show anh da xoay
cv2.imshow("Anh xoay",anh_xoay)

cv2.waitKey()