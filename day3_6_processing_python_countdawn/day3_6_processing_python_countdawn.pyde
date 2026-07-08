#day3_6_processing_python_countdawn
#修改自day3_5_processing_python_countdawn
#有時候變負數,而且太快開始,而且不能暫停
#(1)我:用max()找最大值max(負數,0)
#(2)鬧鐘要可以修改用mouseDragged來滑動
#(3)要可以暫停
target=0 #我們的目標時間
#要可以修改鬧鐘
def setup(): #設定的函式
    global target #要可以修改外面的target變數
    size(500,200) #視窗大小
    mm=minute() #分鐘(現在的時間)
    ss=second() #秒數(現在的時間)
    target =(mm+5)*60+ss #我們的target 目標時間
def draw(): #畫圖的函式
    background(255) #背景白色
    fill(255,0,0) #字紅色
    textSize (150) #字很大150
    remain=max(0,target-minute()*60-second())#剩下的秒數最多到0
    #text("00:00",80,150) #測式大小，位置用的
    mm=remain // 60 #分鐘
    ss=remain % 60 #秒鐘
    text(nf(mm,2)+":"+nf(ss,2),80,150) #接成數字
