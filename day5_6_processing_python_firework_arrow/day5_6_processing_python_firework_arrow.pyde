#day5_6_processing_python_firework_arrow
#修改自say5_5_processing_python_firework
#黑色背景
def setup():#設定的函式
    size(500,500)#視窗大小500*500 中心(250,250)
def draw():#畫圖的函式
    background(0)
    for i in range(40):
        R=30+mouseX#花火半徑式mouseX+20
        a=(PI*2/40)*i#有30條花火
        stroke(232,204,32)#線條筆觸是黃色
        line(250+(R-30)*cos(a),250+(R-30)*sin(a),250+R*cos(a),250+R*sin(a))
        #從(R-20)距離，射到R距離(往外射出去)
