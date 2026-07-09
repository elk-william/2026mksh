#day4_03_processing_python_countdown_mouseDragged
#修改自day4_02_processing_python_countdown_start_
#希望mouse左鍵dragged拖曳 改時間
def setup():
    size(400,400)
start=False #沒有開始
t=10
def draw():
    global t
    background(0)
    textSize(300)
    textAlign(CENTER,CENTER)
    text (t,200,200)
    if start and frameCount%60==0 and t>0:t-=1
def mousePressed ():
    global start
    if mouseButton==RIGHT:start=True=not start
def mouseDragged(): #mosue往上滑,往下滑
    global t #會修改t的值
    if mouseButton==LEFT:
        t-=(mouseY-pmouseY) #向量差
        t=max(0,min(59,t)) #限制在0~59之間
