# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 10:02:56 2026

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 09:40:04 2026

@author: user
"""

#day8_3_spyder_opencv_profile_face_detect_webcam
#我想要在剛剛的程式延伸，能夠偵測人臉
#用一些線條或圓形把臉框起來，請問要再做甚麼修改?
#稍微把臉測果去，就沒有框框了，我想改進
import cv2

# 載入模型
front_face = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
profile_face = cv2.CascadeClassifier( cv2.data.haarcascades + "haarcascade_profileface.xml")

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# ← ① 在 while 迴圈前加入
last_x = 0
last_y = 0
last_w = 0
last_h = 0
alpha = 0.8

while True:

    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    front_faces = front_face.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )

    # ← ② 就是在這裡，把原本畫框的 for 迴圈換掉

    for (x, y, w, h) in front_faces:

        x = int(alpha * last_x + (1 - alpha) * x)
        y = int(alpha * last_y + (1 - alpha) * y)
        w = int(alpha * last_w + (1 - alpha) * w)
        h = int(alpha * last_h + (1 - alpha) * h)

        last_x = x
        last_y = y
        last_w = w
        last_h = h

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()