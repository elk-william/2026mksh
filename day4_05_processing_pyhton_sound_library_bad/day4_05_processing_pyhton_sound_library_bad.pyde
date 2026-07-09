#day4_05_processing_pyhton_sound_library_bad
#Help-examples
music=None
def setup():
    global music
    size(400,400)
    music=SoundFile(this,"music.mp3")#這行失敗了
    music.play()
    
def draw():
    background(200,160,200)
#程式沒錯，錯在相容性的問題
    
