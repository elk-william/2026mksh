#day3_4_processing_python_countdawn
#倒數計時，先把時間印出來囉
def setup():
    size(500,200)
def draw(): #畫圖的函式
    background(255) #背景白色
    fill(255,0,0) #字紅色
    textSize (150) #字很大150
    #text("00:00",80,150) #測式大小，位置用的
    mm=minute() #分鐘
    ss=second() #秒鐘
    text(nf(mm,2)+":"+nf(ss,2),80,150) #接成數字
