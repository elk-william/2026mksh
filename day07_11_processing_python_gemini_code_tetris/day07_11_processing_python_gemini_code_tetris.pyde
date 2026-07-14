# day07_11_processing_python_gemini_code_tetris
# gemini: 想要寫一個 Processing 的 Python Mode 的程式, 可以模仿「俄羅斯方塊」的遊戲, 請給我程式
# 遊戲視窗與網格設定
COLS = 10
ROWS = 20
BLOCK_SIZE = 30

# 網格邊界
BOARD_WIDTH = COLS * BLOCK_SIZE
BOARD_HEIGHT = ROWS * BLOCK_SIZE

# 7 種經典方塊的形狀定義（使用 0/1 矩陣）
SHAPES = {
    'I': [[1, 1, 1, 1]],
    'J': [[1, 0, 0], 
          [1, 1, 1]],
    'L': [[0, 0, 1], 
          [1, 1, 1]],
    'O': [[1, 1], 
          [1, 1]],
    'S': [[0, 1, 1], 
          [1, 1, 0]],
    'T': [[0, 1, 0], 
          [1, 1, 1]],
    'Z': [[1, 1, 0], 
          [0, 1, 1]]
}

# 方塊顏色對應 (RGB)
COLORS = {
    'I': (0, 255, 255),    # 青色
    'J': (0, 0, 255),      # 藍色
    'L': (255, 165, 0),    # 橘色
    'O': (255, 255, 0),    # 黃色
    'S': (0, 255, 0),      # 綠色
    'T': (128, 0, 128),    # 紫色
    'Z': (255, 0, 0)       # 紅色
}

# 遊戲全域變數
board = []          # 2D 陣列，記錄落下的方塊顏色，None 表示空白
current_piece = None # 當前方塊的形狀 (2D list)
current_color = None # 當前方塊的顏色
piece_x = 0         # 當前方塊在網格中的 X 座標
piece_y = 0         # 當前方塊在網格中的 Y 座標

score = 0
game_over = False
fall_speed = 30     # 每隔多少幀下落一格（越小越快）

def setup():
    size(BOARD_WIDTH + 150, BOARD_HEIGHT)  # 右邊留 150px 顯示分數與資訊
    frameRate(60)
    reset_game()

def draw():
    background(40)
    
    # 畫出遊戲盤面邊界
    fill(20)
    rect(0, 0, BOARD_WIDTH, BOARD_HEIGHT)
    
    if not game_over:
        # 控制自動下落時間
        if frameCount % fall_speed == 0:
            move_piece(0, 1)
            
        draw_board()
        draw_current_piece()
    else:
        draw_board()
        # 遊戲結束畫面
        fill(0, 150)
        rect(0, 0, BOARD_WIDTH, BOARD_HEIGHT)
        fill(255)
        textSize(30)
        textAlign(CENTER, CENTER)
        text("GAME OVER", BOARD_WIDTH / 2, BOARD_HEIGHT / 2 - 20)
        textSize(15)
        text("Press 'R' to Restart", BOARD_WIDTH / 2, BOARD_HEIGHT / 2 + 20)
        
    draw_sidebar()

# 初始化 / 重設遊戲
def reset_game():
    global board, score, game_over, fall_speed
    board = [[None for _ in range(COLS)] for _ in range(ROWS)]
    score = 0
    game_over = False
    fall_speed = 30
    spawn_piece()

# 生成新方塊
def spawn_piece():
    global current_piece, current_color, piece_x, piece_y, game_over
    # 隨機選取方塊類型
    shape_keys = list(SHAPES.keys())
    key = shape_keys[int(random(len(shape_keys)))]
    
    current_piece = SHAPES[key]
    current_color = COLORS[key]
    
    # 初始位置：置中偏上
    piece_x = COLS // 2 - len(current_piece[0]) // 2
    piece_y = 0
    
    # 如果一生成就碰撞，代表滿了，Game Over
    if check_collision(current_piece, piece_x, piece_y):
        game_over = True

# 繪製已固定的方塊
def draw_board():
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] is not None:
                fill(board[r][c][0], board[r][c][1], board[r][c][2])
                stroke(0)
                rect(c * BLOCK_SIZE, r * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            else:
                # 繪製背景網格線，方便對齊
                stroke(50)
                noFill()
                rect(c * BLOCK_SIZE, r * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)

# 繪製正在控制的方塊
def draw_current_piece():
    if current_piece is None:
        return
    fill(current_color[0], current_color[1], current_color[2])
    stroke(0)
    for r in range(len(current_piece)):
        for c in range(len(current_piece[0])):
            if current_piece[r][c] == 1:
                draw_x = (piece_x + c) * BLOCK_SIZE
                draw_y = (piece_y + r) * BLOCK_SIZE
                rect(draw_x, draw_y, BLOCK_SIZE, BLOCK_SIZE)

# 繪製右側資訊欄
def draw_sidebar():
    fill(60)
    noStroke()
    rect(BOARD_WIDTH, 0, 150, BOARD_HEIGHT)
    
    fill(255)
    textAlign(LEFT, TOP)
    textSize(20)
    text("TETRIS", BOARD_WIDTH + 20, 30)
    
    textSize(16)
    text("Score:", BOARD_WIDTH + 20, 90)
    textSize(24)
    text(str(score), BOARD_WIDTH + 20, 115)
    
    # 簡單操作說明
    textSize(12)
    fill(200)
    text("Controls:", BOARD_WIDTH + 20, 200)
    text("Left/Right: Move", BOARD_WIDTH + 20, 225)
    text("Up: Rotate", BOARD_WIDTH + 20, 245)
    text("Down: Soft Drop", BOARD_WIDTH + 20, 265)
    text("Space: Hard Drop", BOARD_WIDTH + 20, 285)

# 碰撞偵測
def check_collision(piece, offset_x, offset_y):
    for r in range(len(piece)):
        for c in range(len(piece[0])):
            if piece[r][c] == 1:
                target_x = offset_x + c
                target_y = offset_y + r
                
                # 檢查是否超出邊界
                if target_x < 0 or target_x >= COLS or target_y >= ROWS:
                    return True
                # 檢查是否與已固定的方塊重疊
                if target_y >= 0 and board[target_y][target_x] is not None:
                    return True
    return False

# 移動方塊
def move_piece(dx, dy):
    global piece_x, piece_y
    if not check_collision(current_piece, piece_x + dx, piece_y + dy):
        piece_x += dx
        piece_y += dy
        return True
    
    # 如果是向下移動卻撞到，代表到底了，需要固定方塊
    if dy > 0:
        lock_piece()
        clear_lines()
        spawn_piece()
    return False

# 旋轉方塊（順時針 90 度）
def rotate_piece():
    global current_piece, piece_x
    # 矩陣轉置並翻轉列，達到旋轉效果
    rotated = [list(x) for x in zip(*current_piece[::-1])]
    
    # 旋轉後如果碰撞，嘗試左右微調（Kick 牆壁排除）
    if not check_collision(rotated, piece_x, piece_y):
        current_piece = rotated
    elif not check_collision(rotated, piece_x - 1, piece_y):
        piece_x -= 1
        current_piece = rotated
    elif not check_collision(rotated, piece_x + 1, piece_y):
        piece_x += 1
        current_piece = rotated

# 將方塊固定在盤面上
def lock_piece():
    global board
    for r in range(len(current_piece)):
        for c in range(len(current_piece[0])):
            if current_piece[r][c] == 1:
                board_y = piece_y + r
                board_x = piece_x + c
                if 0 <= board_y < ROWS and 0 <= board_x < COLS:
                    board[board_y][board_x] = current_color

# 消除滿行並計分
def clear_lines():
    global board, score
    new_board = [row for row in board if any(cell is None for cell in row)]
    cleared = ROWS - len(new_board)
    
    # 補足被消除的行數
    if cleared > 0:
        for _ in range(cleared):
            new_board.insert(0, [None for _ in range(COLS)])
        board = new_board
        
        # 簡單計分機制
        points = [0, 100, 300, 500, 800] # 消 1, 2, 3, 4 行的分數
        score += points[cleared]

# 瞬間下落 (Hard Drop)
def hard_drop():
    global piece_y
    while not check_collision(current_piece, piece_x, piece_y + 1):
        piece_y += 1
    lock_piece()
    clear_lines()
    spawn_piece()

# 鍵盤輸入事件
def keyPressed():
    global game_over
    if game_over:
        if key == 'r' or key == 'R':
            reset_game()
        return

    if key == CODED:
        if keyCode == LEFT:
            move_piece(-1, 0)
        elif keyCode == RIGHT:
            move_piece(1, 0)
        elif keyCode == DOWN:
            move_piece(0, 1)
        elif keyCode == UP:
            rotate_piece()
    elif key == ' ':
        hard_drop()
