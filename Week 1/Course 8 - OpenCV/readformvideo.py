import cv2

# Mo video

video_file = "anh/sample.mp4"

cam = cv2.VideoCapture(video_file)

# Doc anh lien tuc tu camera

while True:
    ret ,frame = cam.read()
    if ret:
        cv2.imshow("Webcam",frame)
    phim_bam = cv2.waitKey(1)
    if phim_bam == ord('q'):
        break

cam.release()
cv2.destroyAllWindow

