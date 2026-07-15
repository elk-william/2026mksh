#day10_2_processing_python_firework_dragonball_3images
life=[]#每顆火花都有自己的生命值
x,y=[],[]#一開始的座標
vx,vy=[],[]#一開始也沒有速度
gx,gy=0,0.018#加速度
N=0
r,g,b=[],[],[]#每顆都有自己的色彩

# --- 新增/修改：用來控制多張照片輪流的變數 ---
img_list = []      # 用來存放三張照片的列表
photo_index = 0    # 用來記錄下一次點擊該輪到哪張照片 (0, 1, 或 2)
photos = []        # 儲存照片資訊：[ [cx, cy, current_size, age, max_life, img_id] ]
                   # 這裡多記錄了 img_id，代表這張煙火是用哪張照片

def setup():
    size(900,900)
    global img_list
    # 請確保你的資料夾內有這三張照片，名字分別為 photo0.png, photo1.png, photo2.png
    # (也可以自行修改成你的圖片檔名與格式，例如 .jpg)
    img_list.append(loadImage("dragonball1.png"))
    img_list.append(loadImage("dragonball2.png"))
    img_list.append(loadImage("dragonball3.png"))
    
    imageMode(CENTER) # 設定圖片以中心點繪製

def draw():
    global N
    background(0)
    
    # 1. 先畫照片
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
    global photos, img_list
    for i in range(len(photos)-1, -1, -1):
        p = photos[i] # p = [cx, cy, current_size, age, max_life, img_id]
        
        cx, cy, current_size, age, max_life, img_id = p
        
        # 1. 根據煙火擴散速度 (v=2) 計算當前煙火的半徑
        firework_radius = 2.0 * age 
        
        # 2. 限制照片大小在煙火圈內
        target_size = firework_radius * 1.4
        
        # 3. 讓照片平滑變大
        current_size += (target_size - current_size) * 0.1
        p[2] = current_size # 更新回陣列中
        
        # 4. 計算透明度（隨著生命值結束而淡出）
        alpha_val = map(max_life - age, 0, max_life, 0, 255)
        tint(255, alpha_val)
        
        # 5. 根據當初記錄的 img_id，從 img_list 取出對應的照片繪製
        image(img_list[img_id], cx, cy, current_size, current_size)
        
        # 6. 更新時間
        p[3] += 1 # age 增加 1 幀
        
        # 如果時間到了，就銷毀照片
        if p[3] >= max_life:
            del photos[i]
            
    noTint() # 重設 tint

def mousePressed():
    global r,g,b,x,y,vx,vy,N,life, photos, photo_index
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
    
    # --- 新增：記錄照片的初始狀態與分配照片 ---
    # [ 點擊X, 點擊Y, 初始大小(0), 已活時間(0), 總壽命(150), 照片編號 ]
    photos.append([mouseX, mouseY, 0.0, 0, 150, photo_index])
    
    # 讓下一次點擊時換下一張照片，利用餘數 (%) 確保它永遠在 0, 1, 2 之間循環
    photo_index = (photo_index + 1) % 3
