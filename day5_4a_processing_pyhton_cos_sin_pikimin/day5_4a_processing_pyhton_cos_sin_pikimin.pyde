#day5_4a_processing_pyhton_cos_sin_pikimin
#抽獎勵(金色花苗)會有轉動的花苗
#PImage img
#img=loadImage("pikimin.jpg")
img = None
def setup():
    global img
    size(400,300)
    img = loadImage("pikimin.jpg")
    
def draw():
    background(54,39,155)
    for i in range(6):
        a=(PI*2/6)*i+radians(frameCount)*(mouseX/5+1)
        imageMode(CENTER)
        image(img,200+150*cos(a)-25,150+80*sin(a)-25,50,50)
        
