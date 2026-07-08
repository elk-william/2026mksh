#day3_3_processing_python_def_mouseDragged_glabal
#修改自day3_1_processing_python_textSize_text
#字形相關的部分
a=[99,88,77,66,55]
target=0
def mousePressed():
    global target
    target =mouseX//100
    
def mouseDragged ():
    a[target]-=mouseY-pmouseY
def setup():#設定的函式
    size(500,100)#視窗大小500*100
    
def draw():#畫圖的函式
    for i in range(5):#迴圈跑五次
        fill(255,255,242)#米色
        rect(i*100,0,100,100)#畫格子
        fill(255,0,0)#紅色的字
        textSize(80)
        text(str(a[i]),(i*100)+10,80)#畫出a[i]
