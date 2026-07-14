#day7_11_processing_python_gemini_code_tetris
#gemini:要用processing寫python mode，模仿俄羅斯方塊遊戲
import random

# 遊戲視窗與網格設定
COLS = 10
ROWS = 20
BLOCK_SIZE = 30
INFO_WIDTH = 150 # 右側資訊欄寬度

# 網格地圖：儲存顏色（0 代表空，1~7 代表不同方塊的顏色）
grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

# 7 種經典方塊的形狀 (0 代表空，1 代表有方塊)
SHAPES = [
    [[1, 1, 1, 1]], # I (天藍色)
    
    [[1, 1],
     [1, 1]],       # O (黃色)
    
    [[0, 1, 0],
     [1, 1, 1]],    # T (紫色)
    
    [[0, 1, 1],
     [1, 1, 0]],    # S (綠色)
    
    [[1, 1, 0],
     [0, 1, 1]],    # Z (紅色)
    
    [[1, 0, 0],
     [1, 1, 1]],    # J (藍色)
    
    [[0, 0, 1],
     [1, 1, 1]]     # L (橘色)
]

# 7 種方塊對應的 RGB 顏色 (索引從 1 到 7)
COLORS = {
    1: (0, 240, 240),   # I: 天藍
    2: (240, 240, 0),   # O: 黃
    3: (160, 0, 240),   # T: 紫
    4: (0, 240, 0),     # S: 綠
    5: (240, 0, 0),     # Z: 紅
    6: (0, 0, 240),     # J: 藍
    7: (240, 160, 0)    # L: 橘
}

# 遊戲狀態變數
score = 0
high_score = 0
game_over = False

current_shape = None
current_color_id = 0
current_x = 0
current_y = 0

next_shape = None
next_color_id = 0

last_fall_time = 0
fall_interval = 500 # 下落速度 (毫秒)

def setup():
    # 畫布寬度 = 遊戲區 + 資訊區
    size(COLS * BLOCK_SIZE + INFO_WIDTH, ROWS * BLOCK_SIZE)
    reset_game()

def reset_game():
    """初始化/重置遊戲"""
    global grid, score, game_over, fall_interval, last_fall_time
    grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    score = 0
    game_over = False
    fall_interval = 500
    last_fall_time = millis()
    
    # 預先生成第一個與下一個方塊
    generate_next_piece()
    spawn_piece()
    loop() # 重新啟動 draw 循環

def generate_next_piece():
    """預先隨機生成下一個方塊"""
    global next_shape, next_color_id
    next_color_id = random.randint(1, len(SHAPES))
    next_shape = SHAPES[next_color_id - 1]

def spawn_piece():
    """將預覽的方塊移到畫面上，並生成新的預覽方塊"""
    global current_shape, current_color_id, current_x, current_y
    current_shape = next_shape
    current_color_id = next_color_id
    
    # 計算方塊初始的 X 座標（畫布居中）
    current_x = COLS // 2 - len(current_shape[0]) // 2
    current_y = 0
    
    # 生成下一個預備方塊
    generate_next_piece()
    
    # 檢查一出生是否就碰撞（代表 Game Over）
    if check_collision(current_shape, current_x, current_y):
        end_game()

def end_game():
    """遊戲結束處理"""
    global game_over, high_score
    game_over = True
    if score > high_score:
        high_score = score
    noLoop() # 停止 draw 更新

def draw():
    background(30)
    
    # 1. 繪製遊戲左側的格線與已固定的方塊
    draw_grid()
    
    # 2. 繪製目前控制的下落方塊
    if not game_over:
        draw_current_piece()
        
        # 定時自動下落
        global last_fall_time
        if millis() - last_fall_time > fall_interval:
            move_piece(0, 1)
            last_fall_time = millis()
            
    # 3. 繪製右側資訊看板 (分數、最高紀錄、下一個方塊)
    draw_info_panel()
    
    # 4. 如果遊戲結束，顯示 Game Over 畫面
    if game_over:
        draw_game_over_screen()

def draw_grid():
    """繪製左側主遊戲區網格"""
    stroke(50)
    for r in range(ROWS):
        for c in range(COLS):
            val = grid[r][c]
            if val != 0:
                # 取得該數值對應的顏色
                fill(*COLORS[val])
            else:
                fill(15) # 空白格子的背景色
            rect(c * BLOCK_SIZE, r * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)

def draw_current_piece():
    """繪製玩家正在控制的方塊"""
    if current_shape is None:
        return
    fill(*COLORS[current_color_id])
    stroke(255, 100) # 給控制中的方塊加上微亮邊框
    for r in range(len(current_shape)):
        for c in range(len(current_shape[r])):
            if current_shape[r][c] != 0:
                px = (current_x + c) * BLOCK_SIZE
                py = (current_y + r) * BLOCK_SIZE
                rect(px, py, BLOCK_SIZE, BLOCK_SIZE)

def draw_info_panel():
    """繪製右側資訊看板"""
    # 繪製灰色分隔線與背景
    fill(25)
    noStroke()
    rect(COLS * BLOCK_SIZE, 0, INFO_WIDTH, height)
    
    stroke(100)
    line(COLS * BLOCK_SIZE, 0, COLS * BLOCK_SIZE, height)
    
    # 顯示文字資訊
    fill(255)
    textSize(16)
    textAlign(CENTER, TOP)
    
    # 1. 分數
    text("SCORE", COLS * BLOCK_SIZE + INFO_WIDTH // 2, 30)
    textSize(22)
    text(str(score), COLS * BLOCK_SIZE + INFO_WIDTH // 2, 55)
    
    # 2. 最高紀錄
    textSize(16)
    text("HIGH SCORE", COLS * BLOCK_SIZE + INFO_WIDTH // 2, 110)
    textSize(22)
    text(str(high_score), COLS * BLOCK_SIZE + INFO_WIDTH // 2, 135)
    
    # 3. 預覽下一個方塊
    textSize(16)
    text("NEXT", COLS * BLOCK_SIZE + INFO_WIDTH // 2, 210)
    
    # 繪製下一個方塊的微型預覽
    if next_shape:
        fill(*COLORS[next_color_id])
        stroke(50)
        # 計算置中的偏移量
        preview_block_size = 20
        shape_w = len(next_shape[0]) * preview_block_size
        shape_h = len(next_shape) * preview_block_size
        start_x = COLS * BLOCK_SIZE + (INFO_WIDTH - shape_w) // 2
        start_y = 250 + (80 - shape_h) // 2
        
        for r in range(len(next_shape)):
            for c in range(len(next_shape[r])):
                if next_shape[r][c] != 0:
                    rect(start_x + c * preview_block_size, start_y + r * preview_block_size, preview_block_size, preview_block_size)

def draw_game_over_screen():
    """繪製遊戲結束的半透明覆蓋畫面"""
    # 半透明黑色背景
    fill(0, 0, 0, 200)
    rect(0, 0, width, height)
    
    fill(255, 50, 50)
    textSize(32)
    textAlign(CENTER, CENTER)
    text("GAME OVER", width // 2, height // 2 - 40)
    
    fill(255)
    textSize(16)
    text("Press 'R' to Restart", width // 2, height // 2 + 20)

def check_collision(shape, offset_x, offset_y):
    """碰撞偵測"""
    for r in range(len(shape)):
        for c in range(len(shape[r])):
            if shape[r][c] != 0:
                grid_x = offset_x + c
                grid_y = offset_y + r
                
                if grid_x < 0 or grid_x >= COLS or grid_y >= ROWS:
                    return True
                if grid_y >= 0 and grid[grid_y][grid_x] != 0:
                    return True
    return False

def move_piece(dx, dy):
    """移動目前方塊"""
    global current_x, current_y
    if not check_collision(current_shape, current_x + dx, current_y + dy):
        current_x += dx
        current_y += dy
        return True
    
    # 往下移卻撞到 -> 鎖定並消除
    if dy > 0:
        lock_piece()
        clear_lines()
        spawn_piece()
    return False

def lock_piece():
    """將目前的方塊固化寫入網格地圖"""
    for r in range(len(current_shape)):
        for c in range(len(current_shape[r])):
            if current_shape[r][c] != 0:
                grid[current_y + r][current_x + c] = current_color_id

def clear_lines():
    """消除已滿行，並根據消除行數給予對應分數"""
    global grid, score, fall_interval
    # 過濾掉沒有包含 0 的行 (即代表全滿的行)
    new_grid = [row for row in grid if 0 in row]
    lines_cleared = ROWS - len(new_grid)
    
    if lines_cleared > 0:
        # 在頂部補回空行
        new_grid = [[0 for _ in range(COLS)] for _ in range(lines_cleared)] + new_grid
        grid = new_grid
        
        # 經典俄羅斯方塊計分公式
        score_table = {1: 100, 2: 300, 3: 600, 4: 1000}
        score += score_table.get(lines_cleared, 1000)
        
        # 隨著分數增加，稍微調快下落速度 (最低速限 100 毫秒)
        fall_interval = max(100, 500 - (score // 1000) * 40)

def rotate_piece():
    """順時針旋轉方塊，包含防止卡在牆壁的簡易位移處理"""
    global current_shape, current_x
    rotated = [list(x) for x in zip(*current_shape[::-1])]
    
    # 測試旋轉：如果直接旋轉會碰撞，嘗試向左或向右移 1 格再測 (踢牆處理)
    test_offsets = [0, -1, 1, -2, 2]
    for offset in test_offsets:
        if not check_collision(rotated, current_x + offset, current_y):
            current_x += offset
            current_shape = rotated
            break

def keyPressed():
    """按鍵事件監聽"""
    global game_over
    
    # 如果遊戲結束，此時只有按 'R' 或 'r' 能有反應
    if game_over:
        if key == 'r' or key == 'R':
            reset_game()
        return
        
    # 正常遊戲時的控制
    if key == CODED:
        if keyCode == LEFT:
            move_piece(-1, 0)
        elif keyCode == RIGHT:
            move_piece(1, 0)
        elif keyCode == DOWN:
            move_piece(0, 1) # 手動加速下落
        elif keyCode == UP:
            rotate_piece()   # 旋轉方塊
    elif key == ' ':
        # 空白鍵：直接掉落到底部 (瞬降 Hard Drop)
        while move_piece(0, 1):
            pass
