#day5_2processing_python_cos_sin_fragon_ball_move
#想讓7科龍珠轉動
def setup(): # 設定的函式
    size(400,400)
    
def draw():#畫圖的函式
    background(0)#背景 黑色
    for i in range(7): #七龍珠,跑7次迴圈
        #a=(PI*@/7)*i+mouseX/1000.0 #轉動增加   
        a=(PI*2 / 7)*i+radians(frameCount)/3
        fill(193,119,27)
        ellipse(200+150*cos(a),200+150*sin(a),80,80)
