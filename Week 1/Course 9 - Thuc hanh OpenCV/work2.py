import cv2
import imutils

video_file = "anh\\sample.mp4"

cam = cv2.VideoCapture(video_file)

while True:
    ret , frame = cam.read()
    if ret:
        if ret:
            cv2.imshow("Goc",frame)
        phim_bam = cv2.waitKey(1)
        if phim_bam == ord('a'):
            anh_xoay = imutils.rotate(frame , 90)
            cv2.imshow("Anh Xoay",anh_xoay)
        if phim_bam == ord('d'):
            anh_xoay = imutils.rotate(frame, 270)
            cv2.imshow("Anh Xoay 270" , anh_xoay)
    if cv2.waitKey == ord('q'):
        break

cv2.destroyAllWindows()
video_file.release()