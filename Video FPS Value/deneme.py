import cv2

vid_capture = cv2.VideoCapture('click.mp4')

if not vid_capture.isOpened():
    print("Video dosyası açılırken hata oluştu!")

else:
    fps = vid_capture.get(cv2.CAP_PROP_FPS)
    print('Saniyedeki kare sayısı:', fps, 'FPS')

    kare_sayisi = vid_capture.get(cv2.CAP_PROP_FRAME_COUNT)
    print('Kare sayısı:', kare_sayisi)

while vid_capture.isOpened():
    ret, frame = vid_capture.read()
    if ret:
        cv2.imshow('Frame çerçevesi:', frame)
        key = cv2.waitKey(20)

        if key == ord('q'):
            break

vid_capture.release()
cv2.destroyAllWindows()