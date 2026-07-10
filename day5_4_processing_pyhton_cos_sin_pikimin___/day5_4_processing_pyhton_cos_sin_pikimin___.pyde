#day5_4_processing_pyhton_cos_sin_pikimin_殘影
#抽獎勵(金色花苗)會有轉動的花苗
def setup():
    size(400,300)
    
def draw():
    background(54,39,155)
    for i in range(6):
        a=(PI*2/6)*i+radians(frameCount)*(mouseX/5+1)
        #rect(200+150*cos(a)-25,150+80*sin(a)-25,50,50)
        rectMode(CENTER)
        for r in range(-3,1):#要做殘影 剩下的影子
            fill(255,255/(-r+1))
            rect(200+100*cos(a+r*0.1),150+80*sin(a+r*0.1),50,50)
