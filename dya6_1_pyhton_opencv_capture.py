#dya6_1_pyhton_opencv_capture.py
#從CHATGPT得到的程式
#修改自day4_7_processing_java_video_library_Capture_start_read
import cv2

# 開啟攝影機(0代表第一台攝影機)
cam = cv2.VideoCapture(0)

# 設定解析度
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)#視訊寬度
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)#視訊高度

while True:  #迴圈會一直跑，直到有break跳開結束
    # 讀取一張畫面
    ret, frame = cam.read()

    # 如果讀取失敗就離開
    if not ret:
        break

    # 顯示畫面
    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1)==27:#按Esc離開(改成按Esc)
        break#waitKey(等多久?單位ms)


# 關閉攝影機
cam.release()#把camera正確關閉(收尾很重要)
cv2.destroyAllWindows()#把剛剛開啟的OpenCV視窗全部關掉