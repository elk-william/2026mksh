#day5_3_processing_pyhton_cos_sin_pikimin
#抽獎勵(金色花苗)會有轉動的花苗
def setup():
    size(400,300)
    
def draw():
    background(54,39,155)
    for i in range(6):
        a=(PI*2/6)*i+radians(frameCount)*(mouseX/5+1)
        #rect(200+150*cos(a)-25,150+80*sin(a)-25,50,50)
        rectMode(CENTER)
        rect(200+100*cos(a),150+80*sin(a),50,50)
