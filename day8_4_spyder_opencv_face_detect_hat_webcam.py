# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 10:18:32 2026

@author: user
"""

#day8_4_spyder_opencv_face_detect_hat_webcam
#我想要把一個帽子放在人臉頭上，要怎麼改?
import cv2


# ==========================
# 載入人臉偵測模型
# ==========================

import cv2
import os


face_path = os.path.join(
    cv2.data.haarcascades,
    "haarcascade_frontalface_default.xml"
)


face_cascade = cv2.CascadeClassifier(
    face_path
)


# ==========================
# 載入帽子圖片
# 必須是 PNG 且有透明背景
# ==========================

hat = cv2.imread(
    "greenhat.png",
    cv2.IMREAD_UNCHANGED
)


# ==========================
# 平滑參數
# ==========================

alpha = 0.8

last_x = 0
last_y = 0
last_w = 0
last_h = 0

first = True



# ==========================
# 貼帽子函式
# ==========================

def put_hat(frame, hat, x, y, w, h):

    # 帽子寬度 = 臉寬
    hat_width = w

    # 保持比例
    hat_height = int(
        hat.shape[0] *
        hat_width /
        hat.shape[1]
    )


    hat_resize = cv2.resize(
        hat,
        (hat_width, hat_height)
    )


    # 帽子放在臉上方
    hat_x = x

    hat_y = y - int(hat_height * 0.75)


    # 避免超出畫面
    if hat_y < 0:
        hat_y = 0


    # 避免超出右邊
    if hat_x + hat_width > frame.shape[1]:
        hat_width = frame.shape[1] - hat_x
        hat_resize = cv2.resize(
            hat_resize,
            (hat_width, hat_height)
        )


    # 透明通道
    alpha_channel = (
        hat_resize[:, :, 3] / 255.0
    )


    for c in range(3):

        frame[
            hat_y:hat_y + hat_height,
            hat_x:hat_x + hat_width,
            c
        ] = (

            alpha_channel *
            hat_resize[:, :, c]

            +

            (1-alpha_channel) *
            frame[
                hat_y:hat_y + hat_height,
                hat_x:hat_x + hat_width,
                c
            ]

        )


    return frame



# ==========================
# 開啟攝影機
# ==========================

cap = cv2.VideoCapture(0)



while True:

    ret, frame = cap.read()

    if not ret:
        break


    # 鏡像效果
    frame = cv2.flip(frame, 1)



    # 轉灰階
    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )


    # 偵測臉
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )


    for (x, y, w, h) in faces:


        # ==========================
        # 平滑追蹤
        # ==========================

        if first:

            last_x = x
            last_y = y
            last_w = w
            last_h = h

            first = False


        else:

            x = int(
                alpha * last_x +
                (1-alpha) * x
            )

            y = int(
                alpha * last_y +
                (1-alpha) * y
            )

            w = int(
                alpha * last_w +
                (1-alpha) * w
            )

            h = int(
                alpha * last_h +
                (1-alpha) * h
            )


            last_x = x
            last_y = y
            last_w = w
            last_h = h



        # ==========================
        # 戴帽子
        # ==========================

        frame = put_hat(
            frame,
            hat,
            x,
            y,
            w,
            h
        )


        # 畫臉框(可刪)
        cv2.rectangle(
            frame,
            (x,y),
            (x+w,y+h),
            (255,0,0),
            2
        )



    cv2.imshow(
        "Hat Camera",
        frame
    )


    # ESC離開
    key = cv2.waitKey(1)

    if key == 27:
        break



cap.release()

cv2.destroyAllWindows()