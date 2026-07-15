#day10_1_processing_python_firework_dragonball
life=[]#每顆火花都有自己的生命值
x,y=[],[]#一開始的座標
vx,vy=[],[]#一開始也沒有速度
gx,gy=0,0.018#加速度
N=0
r,g,b=[],[],[]#每顆都有自己的色彩

# --- 新增/修改：用來控制照片的變數 ---
img = None
photos = [] # 儲存照片資訊：[ [cx, cy, current_size, age, max_life] ]
# 這裡把原本記錄的 "大小" 改成記錄 "照片活了多久 (age)"，用時間來動態算半徑

def setup():
    size(900,900)
    global img
    img = loadImage("dragonball.png") 
    imageMode(CENTER) # 設定圖片以中心點繪製

def draw():
    global N
    background(0)
    
    # 1. 先畫照片（讓煙火粒子在照片上方飛散，視覺效果最自然）
    draw_and_update_photos()
    
    # 2. 煙火邏輯
    ellipse(mouseX,mouseY,10,10)
    for i in range(N-1,-1,-1):
        fill(r[i],g[i],b[i])
        stroke(r[i],g[i],b[i])
        strokeWeight(5)
        line(x[i],y[i],x[i]+vx[i],y[i]+vy[i])
        x[i]+=vx[i]
        y[i]+=vy[i]
        vx[i]+=gx
        vy[i]+=gy

        line(x[i],y[i],x[i]+vx[i],y[i]+vy[i])
        if life[i]>0:
            life[i]-=1
        else:
            del life[i]
            del r[i]
            del g[i]
            del b[i]
            del x[i]
            del y[i]
            del vx[i]
            del vy[i]
            N-=1

def draw_and_update_photos():
    global photos
    for i in range(len(photos)-1, -1, -1):
        p = photos[i] # p = [cx, cy, current_size, age, max_life]
        
        cx, cy, current_size, age, max_life = p
        
        # 1. 根據煙火擴散速度 (v=2) 計算當前煙火的半徑
        # 煙火半徑 = 速度 * 時間 (age)
        firework_radius = 2.0 * age 
        
        # 2. 為了讓照片「完全在煙火圓圈內」，照片的最大寬度（對角線）不應超過圓的直徑
        # 我們將目標大小設為：直徑的 70% (1.4 倍半徑)，這樣照片邊角就不會戳出煙火圓圈
        target_size = firework_radius * 1.4
        
        # 3. 讓照片平滑地變大，追趕這個目標大小
        current_size += (target_size - current_size) * 0.1
        p[2] = current_size # 更新回陣列中
        
        # 4. 計算透明度（隨著生命值結束而淡出）
        alpha_val = map(max_life - age, 0, max_life, 0, 255)
        tint(255, alpha_val)
        
        # 5. 繪製照片
        image(img, cx, cy, current_size, current_size)
        
        # 6. 更新時間
        p[3] += 1 # age 增加 1 幀
        
        # 如果時間到了，就銷毀照片
        if p[3] >= max_life:
            del photos[i]
            
    noTint() # 重設 tint

def mousePressed():
    global r,g,b,x,y,vx,vy,N,life, photos
    # 產生煙火
    life+=[random(120,180)]*20 
    x+=[mouseX]*20
    r+=[random(256)]*20
    g+=[random(256)]*20
    b+=[random(256)]*20
    y+=[mouseY]*20
    vx+=[2*cos(PI*2/20*i) for i in range(20)]
    vy+=[2*sin(PI*2/20*i) for i in range(20)]
    N+=20
    
    # --- 新增：記錄照片的初始狀態 ---
    # [ 點擊X, 點擊Y, 初始大小(0), 已活時間(0), 總壽命(150幀) ]
    photos.append([mouseX, mouseY, 0.0, 0, 150])
