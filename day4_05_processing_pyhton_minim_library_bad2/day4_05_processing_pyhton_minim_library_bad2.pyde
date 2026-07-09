#day4_05_processing_pyhton_minim_library_bad2
add_library("minim")
music=None
def setup():
    global music
    size(400,400)
    nimim=Minim(this)
    music=minim.loadFile("music.mp3")
    music.play()
def draw():
    background(255,255,242)
