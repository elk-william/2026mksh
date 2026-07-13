#day6_5_processing_python_firework_mousePressed_many_colorful
#修改自day6_4_processing_python_firework_mosuePressed
#想要做出互動的花火，而且mouse可點很多次，不同顏色
def setup():
    size(900,900)
x,y=[],[]#一開始的座標
vx,vy=[],[]#一開始也沒有速度
gx,gy=0,0.018#加速度
N=0
r,g,b=[],[],[]#每顆都有自己的色彩
def draw():
    background(0)
    
    ellipse(mouseX,mouseY,10,10)#先寫到這裡為止
    if x !=None:
        for i in range(N):
            fill(r[i],g[i],b[i])
            ellipse(x[i],y[i],10,10)
            x[i]+=vx[i]
            y[i]+=vy[i]
            vx[i]+=gx
            vy[i]+=gy
def mousePressed():
    global r,g,b,x,y,vx,vy,N#mouse按下去，要射出花火
    x+=[mouseX]*20#要去修改外面的變數
    r+=[random(256)]*20
    g+=[random(256)]*20
    b+=[random(256)]*20
    y+=[mouseY]*20
    vx+=[2*cos(PI*2/20*i) for i in range(20)]
    vy+=[2*sin(PI*2/20*i) for i in range(20)]
    N+=20
