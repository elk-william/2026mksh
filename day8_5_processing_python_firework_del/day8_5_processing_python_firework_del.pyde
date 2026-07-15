#day8_5_processing_python_firework_del
#想要了解del的意思day7_07_processing_python_firework_life
a=[10,20] #空白的陣列裡面空空
def setup(): #設定的函式
    size(600,100)
    frameRate(1) #每秒畫draw一次
def draw():
    background(0) #背景黑色
    #for i in range(len(a)):#迴圈，把每一個a[i]走一次 #len:陣列的大小
    for i in range(len(a)-1,-1,-1): #改成倒過來的迴圈
        fill(255) #白色的方塊
        rect(i*80,0,80,80)
        fill(255,0,0) #紅色的字
        text(a[i],i*80+40,40)
        a[i]-=1 #數值慢慢變少
        if a[i]<0: del a[i]
def mousePressed(): #mouse每按下一次，就增加一格
    a.append(int(random(5,30))) #用append()加1格的數值
