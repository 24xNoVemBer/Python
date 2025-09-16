import cv2

anh_doc_tu_file = cv2.imread("anh\\sample.jpg",cv2.IMREAD_GRAYSCALE)

cv2.imshow("The Forest" , anh_doc_tu_file)
cv2.imwrite("anh\\dentrang.png",anh_doc_tu_file)

#Dung chuong trinh cho ban phim

cv2.waitKey()

cv2.destroyAllWindows() # <-- dong tat ca cac cua so dang mo 
