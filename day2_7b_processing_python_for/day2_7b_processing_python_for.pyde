#day2_7b_processing_python_for
img=None#沒有東西，但有名字
def setup():
    global img #這行要小心
    size(500,100)
    img=loadImage("cat.jpg")
def draw():
    for i in range(5):
        image(img,i*100,0,100,100)
