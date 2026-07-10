#day5_5_processing__python_firework
#花火節的煙花
def setup():#設定的函式
    size(500,500)#視窗大小500*500 中心(250,250)
def draw():#畫圖的函式
     background(255)
     for i in range(30):
        R=30+mouseX#花火半徑式mouseX+20
        a=(PI*2/30)*i#有30條花火
        stroke(232,204,32)
        line(250,250,250+R*cos(a),250+R*sin(a))
