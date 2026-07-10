#day5_7_processing_pyhton_firework_gravity
#牛頓f=ma 位置,速度,加速度
def setup():
    size(500,500)
x, y=0,250 #位置
vx,vy=10, -10 #速度
gx, gy=0,0.98 #加速度(9.8變成0.98)
def draw():
    global x,y,vx,vy,gx,gy#要修改外面的變數
    #background(0) #先不要背景，才能看到殘影
    stroke(255,255,0)
    ellipse(x,y,10,10)
    x+=vx #位置會隨著速度改變
    y+=vy
    vx+=gx #速度會因為加速度而改變
    vy+=gy
