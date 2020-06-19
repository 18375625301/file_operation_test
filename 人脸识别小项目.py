#人脸监测
import cv2 as cv
# def fac_detect_demo():
#     gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#     fac_detector=cv.CascadeClassifier('G:/opencv/build/etc/haarcascades/haarcascade_frontalface_default.xml')
#     faces=fac_detector.detectMultiScale(gray_img)
#     for x,y,w,h in faces:
#         cv.rectangle(img,(x,y),(x+w,y+h),color=(0,255,0),thickness=2)
#     cv.imshow('result',img)
#
#
# #读取图片
# img=cv.imread('G:/siamfc tc/tc_Airport_ce/0083.jpg')
# fac_detect_demo()
# cv.waitKey()
# cv.destroyAllWindows()

##检测多张人脸
# def fac_detect_demo():
#     gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#     face_detector=cv.CascadeClassifier('G:/opencv/build/etc/haarcascades/haarcascade_frontalface_default.xml')
#     faces=face_detector.detectMultiScale(gray_img,scaleFactor=1.1,minNeighbors=3)
#     for x,y,w,h in faces:
#         print(x,y,w,h)
#         cv.rectangle(img,(x,y),(x+w,y+h),color=(0,255,255),thickness=2)
#     cv.imshow('result',img)
#
#
# img=cv.imread('G:/siamfc tc/tc_Airport_ce/0007.jpg')
# fac_detect_demo()
# cv.waitKey()
# cv.destroyAllWindows()

#视频中人脸检测
# def fac_detect_demo(img):
#     gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#     face_detector=cv.CascadeClassifier('G:/opencv/build/etc/haarcascades/haarcascade_frontalface_default.xml')
#     faces=face_detector.detectMultiScale(gray_img)
#     for x,y,w,h in faces:
#         print(x,y,w,h)
#         cv.rectangle(img,(x,y),(x+w,y+h),color=(0,255,255),thickness=2)
#     cv.imshow('result',img)
# cap=cv.VideoCapture(0)
# while True:
#     flag,frame=cap.read()
#     if not flag:
#         break
#     fac_detect_demo(frame)
#     if ord('q')==cv.waitKey(10):
#         break
# cv.destroyAllWindows()
# cap.release()