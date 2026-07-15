# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 09:40:04 2026

@author: user
"""

#day8_2_spyder_opencv_profile_face_webcam
#我想要在剛剛的程式延伸，能夠偵測人臉
#用一些線條或圓形把臉框起來，請問要再做甚麼修改?
#稍微把臉測果去，就沒有框框了，我想改進
import cv2

# 載入人臉模型
# 正面臉
front_face = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# 側臉
profile_face = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_profileface.xml"
)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:

    ret, frame = cap.read()
    if not ret:
        break

    # 轉灰階
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    front_faces = front_face.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )
    
    profile_faces = profile_face.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )

    # 綠色：正面臉
    for (x, y, w, h) in front_faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
    
    # 藍色：側臉
    for (x, y, w, h) in profile_faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 2)
        cv2.imshow("Face Detection", frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == 27:   # ESC 離開
        break

cap.release()
cv2.destroyAllWindows()