#day8_1_spyder_opencv_webcam
#我想在spyder裡使用opencv讀入webcam視訊鏡頭的畫面
#即時更新。要做打些步驟?那些能卡住?
#因為中文的注音輸入法會卡住q鍵，退出鍵可以改成ESC鍵嗎?
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2

# 開啟預設攝影機
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# 檢查是否成功開啟
if not cap.isOpened():
    print("❌ 無法開啟攝影機")
    exit()

print("✅ 攝影機已開啟")

while True:
    ret, frame = cap.read()

    if not ret:
        print("❌ 無法讀取畫面")
        break

    cv2.imshow("Webcam", frame)

    # 按 q 離開
    key = cv2.waitKey(1) & 0xFF

# 按 ESC (ASCII 27) 離開
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
