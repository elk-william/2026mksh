#day4_02_processing_python_countdown_start_
#希望 mouse 右鍵,會開始,會暫停
def setup():
    size(400,400)
t=10
start=False #沒有開始   
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
