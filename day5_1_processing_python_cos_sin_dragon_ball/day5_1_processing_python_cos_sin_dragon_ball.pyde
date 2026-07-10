#day5_1_processing_python_cos_sin_dragon_ball
#國中教cos() sin() Q: 陳冠宏問:學cos()sin()有什麼用?A: 上市場買冬瓜cos(60)西瓜(30)
#老師在大學3D電腦圖學 很有用
size(400,400)#視窗大小400*400, 正中心(200,200)
ellipse(200,200,300,300)#圖正中心(200,200)圓的大小300*300
for i in range(7):#七龍珠有7個龍珠
    a=(PI*2 / 7)*i#對應的角度a是1/7個圓*i
    ellipse(200+150*cos(a),200+150*sin(a),80,80)
    #圓心200半徑150X座標對應cos(a)
    #圓心200半徑150Y座標對應sin(a)
