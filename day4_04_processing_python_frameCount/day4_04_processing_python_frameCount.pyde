#day4_04_processing_python_frameCount
#希望了解day4_03的frameCount 是什麼意思
def setup():
    size(400,400)
    #frameRate(5) #希望draw()跑慢一點，一秒五次，等一下會刪掉
#如果想知道現在是第幾次執行voiddraw()要用t來數
t=0 #第一行，宣告t變數
def draw():
    global t #第二行，要認識外面的t
    background(0)
    textSize(100)
    textAlign(CENTER,CENTER)
    text(frameCount,200,100) #值會跟4行的t一樣
    text (t,200,200) #第三行，試著畫出t的值
    t+=1 #第四行，每次結束時t會加一
    
    text(frameCount//60,200,300) #每秒60次，除以60就會變秒
