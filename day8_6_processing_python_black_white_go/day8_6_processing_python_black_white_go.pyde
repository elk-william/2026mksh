#day8_6_processing_python_black_white_go
#黑白棋
def setup():
    size(300,300) 
    
a=[[0,0,0],[0,0,0],[0,0,0]]    
def draw():
    background(178,146,29)
    line(0,100,300,100) #橫1
    line(0,200,300,200) #橫2
    line(100,0,100,300) #直1
    line(200,0,200,300) #直2
    for i in range(3): #左手i對應y座標
        for j in range(3): #右手j對應x座標           
            if  a[i][j]>0:#黑色
                fill(0)
                ellipse(j*100+50,i*100+50,80,80)
            if a[i][j]<0: #白色
                fill(255)
                ellipse(j*100+50,i*100+50,80,80)
def mousePressed():
    i=mouseY//100
    j=mouseX//100
    if mouseButton==LEFT: a[i][j]=1 #左鍵黑色
    if mouseButton==RIGHT: a[i][j]=-1 #右鍵白色
    if mouseButton==CENTER: a[i][j]=0 #中鍵沒東西
