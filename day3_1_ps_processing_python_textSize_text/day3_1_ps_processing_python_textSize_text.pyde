#day3_1_ps_processing_python_textSize_text
#不同格子布同顏色
a=[99,88,77,66,55]
def setup():#設定的函式
    size(500,100)#視窗大小500*100
    
def draw():#畫圖的函式
    for i in range(5):#迴圈跑五次
        if i%2==1: fill(150,100,70)#米色
        else: fill(0,255,0)
        rect(i*100,0,100,100)#畫格子
        fill(255,0,0)#紅色的字
        textSize(80)
        text(str(a[i]),(i*100)+10,80)#畫出a[i]
