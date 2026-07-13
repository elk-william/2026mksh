#day6_3_processing_python_firework_gravity_20
#想要做出互動的花光(花火)
def setup():
    size(900,900)
x,y=None,None#一開始的座標
vx,vy=None,None#一開始也沒有速度
gx,gy=0,0.018#加速度
def draw():
    background(0)
    fill(198,186,42)
    ellipse(mouseX,mouseY,10,10)#先寫到這裡為止
    if x !=None:
        for i in range(20):
            ellipse(x[i],y[i],10,10)
            x[i]+=vx[i]
            y[i]+=vy[i]
            vx[i]+=gx
            vy[i]+=gy
def mousePressed():
    global x,y,vx,vy#mouse按下去，要射出花火
    x=[mouseX]*20#要去修改外面的變數
    y=[mouseY]*20
    vx=[2*cos(PI*2/20*i) for i in range(20)]
    vy=[2*sin(PI*2/20*i) for i in range(20)]
    
