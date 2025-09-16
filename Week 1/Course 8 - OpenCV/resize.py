import cv2

anh_doc_tu_file = cv2.imread("anh\\sample.jpg")

#Show anh

cv2.imshow("The Forest",anh_doc_tu_file)

#Resize
anh_nho = cv2.resize(anh_doc_tu_file,dsize = None , fx = 0.5,fy=0.5)

cv2.imshow("Anh",anh_nho)

cv2.waitKey()