import cv2
import imutils

anh_doc_tu_file = cv2.imread("anh\\book.jpg",cv2.IMREAD_GRAYSCALE)

#Show anh

cv2.imshow("The Forest",anh_doc_tu_file)

# #Lay nguong

# nguong = 150
max = 255

# ketqua , anh_da_loc = cv2.threshold(anh_doc_tu_file,nguong,max,cv2.THRESH_BINARY)

#Lay nguong bang adaptive

anh_da_loc = cv2.adaptiveThreshold(anh_doc_tu_file,max,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,199,5)

#Show anh da loc nguong

cv2.imshow("nguong",anh_da_loc)

cv2.waitKey()
