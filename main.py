import turtle
from tkinter import *
from tkinter import ttk
import math
import time

WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 576

isAnimating = False

hcn = None
p = None
t = None
screen = None

def drawOxy():
    if p is None: 
        return
    p.clear()
    #Vẽ lưới
    p.pencolor('#C0C0C0')
    p.penup()
    p.pensize(0.5)
    for i in range(285, -290, -5):
        p.goto(-510, i)   
        p.pendown()
        p.forward(1020)
        p.penup()
    p.right(90)
    for i in range(-510, 515, 5):
        p.goto(i, 285)   
        p.pendown()
        p.forward(570)
        p.penup()   
    p.setheading(0) #Hướng E (đông)

    p.pencolor('black')
    p.pensize(2)
    #Vẽ trục Ox
    p.penup()
    p.goto(-510, 0)
    p.pendown()
    p.setheading(0)
    p.forward(1020)
    p.penup()
    p.goto(510, -25)
    p.write('x', align='right', font=('arial', 12, 'normal'))
    #Vẽ trục Oy
    p.penup()
    p.goto(0, -285)
    p.pendown()
    p.setheading(90) 
    p.forward(570)
    p.penup()
    p.goto(10, 270)
    p.write('y', align='left', font=('arial', 12, 'normal'))
    #Vẽ điểm O
    p.penup()
    p.goto(-2, -22)
    p.write('O', align='right', font=('arial', 12, 'normal'))
    p.setheading(0)
    # #Vẽ các đường kẻ trục Ox
    # p.penup()
    # p.pensize(1)
    # for i in range(-500, 525, 25):
    #     p.goto(i, -5)
    #     p.pendown()
    #     p.forward(11)
    #     p.penup()
    #     if i != 0:
    #         p.write(i//5, align='center', font=('arial', 10, 'normal'))
    # #Vẽ các đường kẻ trục Oy
    # p.right(90)
    # for i in range(-275, 300, 25):
    #     p.goto(-5, i)
    #     p.pendown()
    #     p.forward(10)
    #     p.penup()
    #     if i != 0:
    #         p.goto(-15, i-8)
    #         p.write(i//5, align='center', font=('arial', 10, 'normal'))

def drawOxyz():
    if p is None: 
        return
    p.clear()
    #Vẽ lưới
    p.pencolor('#C0C0C0')
    p.penup()
    p.pensize(0.5)
    for i in range(285, -290, -5):
        p.goto(-510, i)   
        p.pendown()
        p.forward(1020)
        p.penup()
    p.right(90)
    for i in range(-510, 515, 5):
        p.goto(i, 285)   
        p.pendown()
        p.forward(570)
        p.penup()   
    p.setheading(0)

    p.pencolor('black')
    p.pensize(2)
    #Vẽ trục Ox
    p.penup()
    p.goto(0, 0)
    p.pendown()
    p.setheading(0)
    p.forward(510)
    p.penup()
    p.goto(510, -25)
    p.write('x', align='right', font=('arial', 12, 'normal'))
    #Vẽ trục Oy
    p.penup()
    p.goto(0, 0)
    p.pendown()
    p.setheading(90)  
    p.forward(285)
    p.penup()
    p.goto(10, 270)
    p.pendown()
    p.write('y', align='left', font=('arial', 12, 'normal'))
    #Vẽ trục Oz
    p.penup()
    p.goto(0, 0)
    p.pendown()
    p.left(135)    
    p.forward(405)
    p.write('z', align='right', font=('arial', 12, 'normal'))
    #Vẽ điểm O
    p.penup()
    p.goto(12, -22)
    p.write('O', align='right', font=('arial', 12, 'normal'))
    p.setheading(0)
    # #Vẽ các đường kẻ trục Ox
    # p.penup()
    # p.pensize(1)
    # for i in range(-500, 525, 25):
    #     p.goto(i, -5)
    #     p.pendown()
    #     p.forward(11)
    #     p.penup()
    #     if i != 0:
    #         p.write(i//5, align='center', font=('arial', 10, 'normal'))
    # #Vẽ các đường kẻ trục Oy
    # p.right(90)
    # for i in range(-275, 300, 25):
    #     p.goto(-5, i)
    #     p.pendown()
    #     p.forward(10)
    #     p.penup()
    #     if i != 0:
    #         p.goto(-15, i-8)
    #         p.write(i//5, align='center', font=('arial', 10, 'normal'))

def drawPoint(x, y):
    x *= 5
    y *= 5
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.dot(5, 'red')

def drawLine(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    step_x = 1 if x2 > x1 else -1
    step_y = 1 if y2 > y1 else -1

    if dx > dy:
        P = 2 * dy - dx
        x, y = x1, y1
        while x != x2:
            drawPoint(x, y)
            if P < 0:
                P += 2 * dy
            else:
                P += 2 * dy - 2 * dx
                y += step_y
            x += step_x
    else:
        P = 2 * dx - dy
        x, y = x1, y1
        while y != y2:
            drawPoint(x, y)
            if P < 0:
                P += 2 * dx
            else:
                P += 2 * dx - 2 * dy
                x += step_x
            y += step_y

    drawPoint(x2, y2)

def drawHCN(x1, y1, x2, y2):
    global hcn
    # t.clear()
    t.penup()
    t.goto(x1 * 5, y1 * 5)
    t.pendown()
    t.fillcolor('#ff9999')
    t.begin_fill()
    drawLine(x1, y1, x2, y1)
    drawLine(x2, y1, x2, y2)
    drawLine(x2, y2, x1, y2)
    drawLine(x1, y2, x1, y1)
    hcn = [x1, y1, x2, y2] # Cập nhật biến toàn cục hcn
    t.end_fill()

def drawNetDut(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    step_x = 1 if x2 > x1 else -1
    step_y = 1 if y2 > y1 else -1

    len_dash = 5
    
    x, y = x1, y1

    if dx == 0 and dy == 0:
        if len_dash >= 3:
            drawPoint(x,y)
        return

    if dx > dy:
        P = 2 * dy - dx
        while x != x2:
            if len_dash >= 3:
                drawPoint(x, y)           
            len_dash -= 1
            if len_dash == 0: 
                len_dash = 5     
            if P < 0:
                P += 2 * dy
            else:
                P += 2 * dy - 2 * dx
                y += step_y
            x += step_x
    else: # dy >= dx
        P = 2 * dx - dy
        while y != y2:
            if len_dash >= 3:
                drawPoint(x, y)
            len_dash -= 1
            if len_dash == 0:
                len_dash = 5               
            if P < 0:
                P += 2 * dx
            else:
                P += 2 * dx - 2 * dy
                x += step_x
            y += step_y

#Phần 2D
def tinhTien(dx, dy):
    if hcn:
        t.clear()
        x1, y1, x2, y2 = hcn
        newX1 = x1 + dx
        newY1 = y1 + dy
        newX2 = x2 + dx
        newY2 = y2 + dy
        drawHCN(newX1, newY1, newX2, newY2)
    else:
        print("Không có hình chữ nhật nào để tịnh tiến. Hãy vẽ một hình chữ nhật trước.")

def bienDoiTiLe(Sx, Sy):
    if hcn:
        t.clear()
        x1, y1, x2, y2 = hcn
        newX1 = x1
        newY1 = y1
        newX2 = x2 * Sx
        newY2 = y2 * Sy
        drawHCN(newX1, newY1, newX2, newY2)
    else:
        print("Không có hình chữ nhật.")

def quayQuanhDiem(pX, pY, gocQuay):
    if hcn:
        t.clear() 
        if pX != 0 or pY != 0:
            pX2 = pX * 5
            pY2 = pY * 5
            
            t.penup()
            t.goto(pX2, pY2)
            t.pendown()
            t.dot(5, 'red')
            
            t.penup()
            t.goto(pX2 - 2, pY2 - 22) 
            t.pencolor('red')
            t.pendown()
            t.write('P', align='right', font=('arial', 15, 'normal'))
            
        x1, y1, x2, y2 = hcn
        diem = [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]
        gocRad = math.radians(gocQuay)
        cosGoc = math.cos(gocRad)
        sinGoc = math.sin(gocRad)
        
        newDiem = []
        for x, y in diem:
            # Dịch điểm về gốc tọa độ
            # Quay quanh gốc tọa độ mới
            # Dịch chuyển trở lại vị trí ban đầu
            newX = pX + cosGoc * (x - pX) - sinGoc * (y - pY)
            newY = pY + sinGoc * (x - pX) + cosGoc * (y - pY)
            newDiem.append((int(round(newX)), int(round(newY))))

        slCanh = len(newDiem)
        for i in range(slCanh):
            pDau = newDiem[i]
            pCuoi = newDiem[(i + 1) % slCanh]
            drawLine(pDau[0], pDau[1], pCuoi[0], pCuoi[1])
    else:
        print("Không có hình chữ nhật.")

def doiXungQuaO():
    if hcn:
        t.clear() 
        x1, y1, x2, y2  = hcn
        
        newX1 = -x1  
        newY1 = -y1  
        newX2 = -x2  
        newY2 = -y2  
        drawHCN(newX1, newY1, newX2, newY2)
    else:
        print("Không có hình chữ nhật nào để thực hiện đối xứng. Hãy vẽ một hình chữ nhật trước.")

def doiXungQuaOX():
    if hcn:
        t.clear()
        x1, y1, x2, y2  = hcn
        
        newX1 = x1  
        newY1 = -y1  
        newX2 = x2
        newY2 = -y2  
        drawHCN(newX1, newY1, newX2, newY2)
    else:
        print("Không có hình chữ nhật nào để thực hiện đối xứng. Hãy vẽ một hình chữ nhật trước.")

def doiXungQuaOY():
    if hcn:
        t.clear()
        x1, y1, x2, y2  = hcn
        
        newX1 = -x1  
        newY1 = y1  
        newX2 = -x2
        newY2 = y2  
        drawHCN(newX1, newY1, newX2, newY2)
    else:
        print("Không có hình chữ nhật nào để thực hiện đối xứng. Hãy vẽ một hình chữ nhật trước.")

def doiXungDiem(xA, yA):
    if hcn:
        t.clear() 
        xA2 = xA * 5
        yA2 = yA * 5
        
        t.penup()
        t.goto(xA2, yA2)
        t.pendown()
        t.dot(5, 'red')
        
        t.penup()
        t.goto(xA2 - 2, yA2 - 22) 
        t.pencolor('red')
        t.pendown()
        t.write('A', align='right', font=('arial', 15, 'normal'))

        x1, y1, x2, y2  = hcn
        
        newX1 = 2*xA - x1
        newY1 = 2*yA - y1
        newX2 = 2*xA - x2
        newY2 = 2*yA - y2
        drawHCN(newX1, newY1, newX2, newY2)
    else:
        print("Không có hình chữ nhật nào để thực hiện đối xứng. Hãy vẽ một hình chữ nhật trước.")

def doiXungDoanThang(xA, yA, xB, yB):
    if hcn and (xA != xB or yA != yB):
        # t.clear() 

        xA2 = xA * 5
        yA2 = yA * 5
        xB2 = xB * 5
        yB2 = yB * 5
        
        t.penup()
        t.goto(xA2, yA2)
        t.pendown()
        t.dot(5, 'red')
        
        t.penup()
        t.goto(xA2 - 2, yA2 - 2) 
        t.pencolor('red')
        t.pendown()
        t.write('A', align='right', font=('arial', 15, 'normal'))

        t.penup()
        t.goto(xB2, yB2)
        t.pendown()
        t.dot(5, 'red')
        
        t.penup()
        t.goto(xB2 - 2, yB2 - 2)
        t.pencolor('red')
        t.pendown()
        t.write('B', align='right', font=('arial', 15, 'normal'))

        drawLine(xA, yA, xB, yB)

        x1, y1, x2, y2 = hcn
        diem = [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]

        gocQuay = math.atan2(yB - yA, xB - xA)

        cos2Goc = math.cos(2 * gocQuay)
        sin2Goc = math.sin(2 * gocQuay)

        newDiem = []
        for x, y in diem:
            newX = (x - xA) * cos2Goc + (y - yA) * sin2Goc + xA
            newY = (x - xA) * sin2Goc - (y - yA) * cos2Goc + yA
            newDiem.append((int(round(newX)), int(round(newY))))

        slCanh = len(newDiem)
        for i in range(slCanh):
            pDau = newDiem[i]
            pCuoi = newDiem[(i + 1) % slCanh]
            drawLine(pDau[0], pDau[1], pCuoi[0], pCuoi[1])
        
    else:
        print("Không có hình chữ nhật nào để thực hiện đối xứng. Hãy vẽ một hình chữ nhật trước.")

#Phần 3D
def drawHinhTron3D(x, y, R):
    x_i, y_i = 0, R
    P = 3 - 2 * R
    while x_i <= y_i:     
        drawPoint(x + x_i, y + y_i)
        drawPoint(x + y_i, y + x_i)
        drawPoint(x + y_i, y - x_i)
        drawPoint(x + x_i, y - y_i)
        drawPoint(x - x_i, y - y_i)
        drawPoint(x - y_i, y - x_i)
        drawPoint(x - y_i, y + x_i)
        drawPoint(x - x_i, y + y_i)

        if P < 0:
            P += 4 * x_i + 6
        else:
            P += 4 * (x_i - y_i) + 10
            y_i -= 1
        x_i += 1

def drawHinhEllipse3D(x, y, a, b):
    x_i, y_i = 0, b
    P = b**2 - a**2 * b + a**2 / 4
    len_dash = 5
    while a**2 * (y_i - 0.5) > b**2 * (x_i + 1):
        if len_dash >= 3:           
            drawPoint(x + x_i, y + y_i)
            drawPoint(x - x_i, y + y_i)
        len_dash -= 1
        if len_dash == 0:  
            len_dash = 5
        drawPoint(x - x_i, y - y_i)
        drawPoint(x + x_i, y - y_i)
        if P < 0:
            P += b**2 * (2 * x_i + 3)
        else:
            P += b**2 * (2 * x_i + 3) + a**2 * (-2 * y_i + 2)
            y_i -= 1
        x_i += 1

    Q = b**2 * (x_i + 0.5)**2 + a**2 * (y_i - 1)**2 - a**2 * b**2
    while y_i >= 0:
        if len_dash >= 3:           
            drawPoint(x + x_i, y + y_i)
            drawPoint(x - x_i, y + y_i)
        len_dash -= 1
        if len_dash == 0:  
            len_dash = 5
        drawPoint(x - x_i, y - y_i)
        drawPoint(x + x_i, y - y_i)
        if Q < 0:
            Q += b**2 * (2 * x_i + 2) + a**2 * (-2 * y_i + 3)
            x_i += 1
        else:
            Q += a**2 * (3 - 2 * y_i)
        y_i -= 1

def drawHinhHop(x, y, z, dai, rong, cao):
    t.clear()
    
    # Mặt đáy (theo mặt phẳng xz)
    A = (x, y, z)  # Đỉnh gốc
    B = (x + dai, y, z)
    C = (x + dai, y, z + rong)
    D = (x, y, z + rong)
    
    # Mặt trên
    E = (x, y + cao, z)
    F = (x + dai, y + cao, z)
    G = (x + dai, y + cao, z + rong)
    H = (x, y + cao, z + rong)
    
    # Hệ số để tạo hiệu ứng 3D (tỷ lệ góc nhìn theo trục z)
    factor = 0.5
    
    # Chuyển đổi tọa độ 3D sang 2D để hiển thị
    def to2D(point):
        x3d, y3d, z3d = point
        x2d = x3d - z3d * factor
        y2d = y3d - z3d * factor
        return int(x2d), int(y2d)
    
    # Chuyển đổi tọa độ các đỉnh
    A2D = to2D(A)
    B2D = to2D(B)
    C2D = to2D(C)
    D2D = to2D(D)
    E2D = to2D(E)
    F2D = to2D(F)
    G2D = to2D(G)
    H2D = to2D(H)    # Xác định các cạnh thấy được và ẩn (dựa trên góc nhìn)
    visible_edges = [
        (B2D, C2D), (C2D, D2D),  # Mặt đáy (thấy được)
        (D2D, H2D), (B2D, F2D), (C2D, G2D), # Các cạnh bên và sau (thấy được)
        (E2D, F2D), (F2D, G2D), (G2D, H2D), (H2D, E2D)   # Mặt trên (thấy được)
    ]
    
    hidden_edges = [
        (A2D, B2D), (A2D, D2D), (A2D, E2D)   # Các cạnh ẩn theo hình
    ]
    
    # Vẽ cạnh nét liền
    for start, end in visible_edges:
        drawLine(start[0], start[1], end[0], end[1])   
    # Vẽ cạnh nét đứt
    for start, end in hidden_edges:
        drawNetDut(start[0], start[1], end[0], end[1])
    
    # Đánh dấu các đỉnh bằng chữ cái và hiển thị tọa độ
    points = [(A, A2D, "A"), (B, B2D, "B"), (C, C2D, "C"), (D, D2D, "D"),
              (E, E2D, "E"), (F, F2D, "F"), (G, G2D, "G"), (H, H2D, "H")]
    
    # Tọa độ hiển thị trên Oxyz
    display_coords = ["Thông số Hình Hộp:"]
    for idx, (point3D, point2D, label) in enumerate(points):
        px, py = point2D
        t.penup()
        t.goto((px - 1) * 5, py * 5)  # Dịch sang trái 2 pixel
        t.pendown()
        t.pencolor('blue')
        t.write(label, align='right', font=('arial', 12, 'normal'))
        
        # Thêm tọa độ vào danh sách hiển thị
        display_coords.append(f"{label}({point3D[0]}, {point3D[1]}, {point3D[2]})")
    
    hienThiToaDo(display_coords)

def drawHinhChop(x, y, z, dai, rong, cao):
    t.clear()
    
    # Tính toán các đỉnh của hình chóp
    # Đỉnh gốc và đáy
    A = (x, y, z)  # Đỉnh gốc (góc dưới bên trái đáy)
    B = (x + dai, y, z)  # Góc dưới bên phải đáy
    C = (x + dai, y, z + rong)  # Góc trên bên phải đáy
    D = (x, y, z + rong)  # Góc trên bên trái đáy
    
    # Đỉnh chóp đặt ở giữa đáy và cao hơn
    E = (x + dai/2, y + cao, z + rong/2)
    
    # Hệ số để tạo hiệu ứng 3D (tỷ lệ góc nhìn theo trục z)
    factor = 0.5
    
    # Chuyển đổi tọa độ 3D sang 2D để hiển thị
    def to2D(point):
        x3d, y3d, z3d = point
        x2d = x3d - z3d * factor
        y2d = y3d - z3d * factor
        return int(x2d), int(y2d)
    
    # Chuyển đổi tọa độ các đỉnh
    A2D = to2D(A)
    B2D = to2D(B)
    C2D = to2D(C)
    D2D = to2D(D)
    E2D = to2D(E)
    
    # Xác định các cạnh nhìn thấy và ẩn - thay đổi theo yêu cầu
    visible_edges = [
        (D2D, C2D), (C2D, B2D), (C2D, E2D), (B2D, C2D),  # Cạnh nhìn thấy
        (D2D, E2D), (B2D, E2D)
    ]
    
    hidden_edges = [
        (A2D, D2D), (A2D, B2D), (A2D, E2D)  # Các cạnh ẩn AD, AB, AE theo yêu cầu
    ]
    
    # Vẽ cạnh nét liền (thấy được)
    for start, end in visible_edges:
        drawLine(start[0], start[1], end[0], end[1])
    
    # Vẽ cạnh nét đứt (ẩn) AD, AE, AB
    for start, end in hidden_edges:
        drawNetDut(start[0], start[1], end[0], end[1])
    
    
    # Đánh dấu các đỉnh bằng chữ cái và hiển thị tọa độ
    points = [(A, A2D, "A"), (B, B2D, "B"), (C, C2D, "C"), (D, D2D, "D"), (E, E2D, "E")]
    
    # Tọa độ hiển thị bên phải
    display_coords = ["Thông số Hình Chóp:"]
    
    # Vẽ các điểm và nhãn
    for idx, (point3D, point2D, label) in enumerate(points):
        px, py = point2D
        t.penup()
        t.goto((px - 1) * 5, py * 5)  # Dịch sang trái 1 pixel
        t.pendown()
        t.pencolor('blue')
        t.write(label, align='right', font=('arial', 12, 'normal'))
        
        # Thêm tọa độ vào danh sách hiển thị
        display_coords.append(f"{label}({point3D[0]}, {point3D[1]}, {point3D[2]})")
    
    hienThiToaDo(display_coords)

def drawHinhCau(x, y, z, ban_kinh):
    # Xóa hình vẽ trước
    t.clear()
    
    # Hệ số để tạo hiệu ứng 3D (tỷ lệ góc nhìn theo trục z)
    factor = 0.5
    
    # Chuyển đổi tọa độ 3D sang 2D để hiển thị
    def to2D(point):
        x3d, y3d, z3d = point
        x2d = x3d - z3d * factor
        y2d = y3d - z3d * factor
        return int(x2d), int(y2d)
    
    # Tọa độ tâm
    O = (x, y, z)
    O2D = to2D(O)
    
    # Vẽ tâm
    px, py = O2D
    t.penup()
    t.goto(px * 5, py * 5)
    t.pendown()
    t.dot(5, 'red')
    # Vẽ đường tròn chính (mặt chiếu)
    drawHinhTron3D(px, py, ban_kinh)
    
    # Vẽ một ellipse ngang (với trục lớn là đường kính của đường tròn)
    # Đảm bảo ellipse tiếp xúc với đường tròn chính ở 2 điểm
    # Trục lớn = 2*bán kính = đường kính
    # Trục nhỏ = factor * đường kính để tạo hiệu ứng 3D
    drawHinhEllipse3D(px, py, ban_kinh, ban_kinh * factor)
    
    # Hiển thị tên và tọa độ tâm
    t.penup()
    t.goto((px - 1) * 5, py * 5)
    t.pendown()
    t.pencolor('blue')
    t.write("I", align='right', font=('arial', 12, 'normal'))
    
    # Hiển thị tọa độ tâm và bán kính
    coord_text = [
        "Thông số Hình Cầu:",
        f"Tâm I({O[0]:.1f}, {O[1]:.1f}, {O[2]:.1f})",
        f"Bán kính R = {ban_kinh:.1f}"
    ]
    hienThiToaDo(coord_text)

# Phần Animation
def drawBackground():
    # Gradient từ #3c1668 (60,22,104) đến #23296d (35,41,109)
    R1, G1, B1 = 60, 22, 104
    R2, G2, B2 = 35, 41, 109
    height = WINDOW_HEIGHT
    width = WINDOW_WIDTH
    top = height // 2
    left = -width // 2

    for y in range(height):
        t = y / (height - 1)
        r = int((1 - t) * R1 + t * R2)
        g = int((1 - t) * G1 + t * G2)
        b = int((1 - t) * B1 + t * B2)
        color = f"#{r:02x}{g:02x}{b:02x}"
        p.pencolor(color)
        p.penup()
        p.goto(left, top - y)
        p.pendown()
        p.goto(left + width, top - y)
        p.penup()

def drawHinhEllipse(x, y, a, b, color):
    if color is not None:
        # Danh sách lưu các điểm (x_i, y_i) tương đối của 1/4 cung ellipse (góc phần tư 1)
        # Điểm được sắp xếp từ trục y dương (0, b) đến trục x dương (a, 0)
        dsDiem = []
        x_i, y_i = 0, b
        P = b**2 - a**2 * b + a**2 / 4
        while a**2 * (y_i - 0.5) > b**2 * (x_i + 1):         
            dsDiem.append((x + x_i, y + y_i))
            dsDiem.append((x - x_i, y + y_i))
            dsDiem.append((x - x_i, y - y_i))
            dsDiem.append((x + x_i, y - y_i))
            if P < 0:
                P += b**2 * (2 * x_i + 3)
            else:
                P += b**2 * (2 * x_i + 3) + a**2 * (-2 * y_i + 2)
                y_i -= 1
            x_i += 1

        Q = b**2 * (x_i + 0.5)**2 + a**2 * (y_i - 1)**2 - a**2 * b**2
        while y_i >= 0:          
            dsDiem.append((x + x_i, y + y_i))
            dsDiem.append((x - x_i, y + y_i))
            dsDiem.append((x - x_i, y - y_i))
            dsDiem.append((x + x_i, y - y_i))
            if Q < 0:
                Q += b**2 * (2 * x_i + 2) + a**2 * (-2 * y_i + 3)
                x_i += 1
            else:
                Q += a**2 * (3 - 2 * y_i)
            y_i -= 1
        
        if dsDiem:
            # Loại bỏ các điểm trùng lặp
            dsDiemSorted = sorted(list(set(dsDiem)))
            # Sắp xếp các điểm duy nhất theo góc giảm dần quanh tâm (x, y) cho thứ tự theo chiều kim đồng hồ 
            dsDiemSorted.sort(key=lambda p: math.atan2(p[1] - y, p[0] - x), reverse=True)
            dsDiem = dsDiemSorted
            # print(dsDiem)

            t.pencolor(color)
            t.fillcolor(color)
            t.penup()
            t.goto(dsDiem[0][0] * 5, dsDiem[0][1] * 5) # Điểm bắt đầu
            t.pendown()
            t.begin_fill()
            for diem in dsDiem:
                t.goto(diem[0] * 5, diem[1] * 5)
            t.goto(dsDiem[0][0] * 5, dsDiem[0][1] * 5)
            t.end_fill()
    else:
        x_i, y_i = 0, b
        P = b**2 - a**2 * b + a**2 / 4
        while a**2 * (y_i - 0.5) > b**2 * (x_i + 1):          
            drawPoint(x + x_i, y + y_i)
            drawPoint(x - x_i, y + y_i)
            drawPoint(x - x_i, y - y_i)
            drawPoint(x + x_i, y - y_i)
            if P < 0:
                P += b**2 * (2 * x_i + 3)
            else:
                P += b**2 * (2 * x_i + 3) + a**2 * (-2 * y_i + 2)
                y_i -= 1
            x_i += 1

        Q = b**2 * (x_i + 0.5)**2 + a**2 * (y_i - 1)**2 - a**2 * b**2
        while y_i >= 0:          
            drawPoint(x + x_i, y + y_i)
            drawPoint(x - x_i, y + y_i)
            drawPoint(x - x_i, y - y_i)
            drawPoint(x + x_i, y - y_i)
            if Q < 0:
                Q += b**2 * (2 * x_i + 2) + a**2 * (-2 * y_i + 3)
                x_i += 1
            else:
                Q += a**2 * (3 - 2 * y_i)
            y_i -= 1
    t.penup()

def setupdrawCloud():
    scale1 = 0.6
    scale2 = 0.4
    offset_scale1 = 1
    offset_scale2 = 0.8

    cloud1_info = [
        (int(-25*offset_scale1), int(-5*offset_scale1), int(13*scale1), int(8*scale1)),
        (int(0*offset_scale1), int(4*offset_scale1), int(17*scale1), int(14*scale1)),
        (int(15*offset_scale1), int(2*offset_scale1), int(18*scale1), int(10*scale1)),
        (int(-9*offset_scale1), int(10*offset_scale1), int(11*scale1), int(6*scale1)),
        (int(10*offset_scale1), int(8*offset_scale1), int(13*scale1), int(8*scale1)),
        (int(-30*offset_scale1), int(-8*offset_scale1), int(10*scale1), int(5*scale1)),
        (int(30*offset_scale1), int(3*offset_scale1), int(12*scale1), int(7*scale1)),
        (int(-5*offset_scale1), int(-9*offset_scale1), int(18*scale1), int(13*scale1)),
        (int(7*offset_scale1), int(-8*offset_scale1), int(14*scale1), int(10*scale1)),
        (int(-19*offset_scale1), int(-8*offset_scale1), int(12*scale1), int(8*scale1)),
        (int(25*offset_scale1), int(-3*offset_scale1), int(15*scale1), int(10*scale1)),
        (int(0*offset_scale1), int(-15*offset_scale1), int(11*scale1), int(6*scale1)),
        (int(-15*offset_scale1), int(1*offset_scale1), int(18*scale1), int(13*scale1)),
        (int(15*offset_scale1), int(-7*offset_scale1), int(9*scale1), int(5*scale1))
    ]
    cloud1_definition = {
        # "centerX": -165, "centerY": -10,
        # "ellipses_info": cloud1_info, "color": "#6c6995"
        "centerX": 0, "centerY": -10,
        "ellipses_info": cloud1_info, "color": "#6c6995"
    }

    cloud2_info = [
        (int(-11*offset_scale2), int(3*offset_scale2), int(17*scale2), int(9*scale2)),
        (int(2*offset_scale2), int(-2*offset_scale2), int(20*scale2), int(13*scale2)),
        (int(25*offset_scale2), int(5*offset_scale2), int(13*scale2), int(8*scale2)),
        (int(2*offset_scale2), int(7*offset_scale2), int(19*scale2), int(10*scale2)),
        (int(14*offset_scale2), int(10*offset_scale2), int(21*scale2), int(10*scale2)),
        (int(-25*offset_scale2), int(-5*offset_scale2), int(11*scale2), int(6*scale2)),
        (int(33*offset_scale2), int(0*offset_scale2), int(12*scale2), int(8*scale2)),
        (int(0*offset_scale2), int(-8*offset_scale2), int(17*scale2), int(12*scale2)),
        (int(10*offset_scale2), int(-10*offset_scale2), int(13*scale2), int(8*scale2)),
        (int(-14*offset_scale2), int(-6*offset_scale2), int(20*scale2), int(10*scale2)),
        (int(18*offset_scale2), int(-2*offset_scale2), int(25*scale2), int(16*scale2)),
        (int(-10*offset_scale2), int(-12*offset_scale2), int(10*scale2), int(5*scale2)),
        (int(30*offset_scale2), int(-6*offset_scale2), int(12*scale2), int(7*scale2))
    ]
    cloud2_definition = {
        # "centerX": -135, "centerY": 35,
        "centerX": 0, "centerY": 35,
        "ellipses_info": cloud2_info, "color": "#9e9dbd"
    }
    return [cloud1_definition, cloud2_definition]

def drawCloud(x=0, y=0):
    all_cloud_info = setupdrawCloud()

    for cloud in all_cloud_info:
        centerX = cloud["centerX"]
        centerY = cloud["centerY"]
        ellipses_info = cloud["ellipses_info"]
        color = cloud["color"]
        
        for offsetX, offsetY, a, b in ellipses_info:
            drawHinhEllipse(centerX + offsetX + x, centerY + offsetY + y, a, b, color)

def drawHinhTron(x, y, R, color=None):
    if color is not None:
        dsDiem = []
        x_i, y_i = 0, R
        P = 3 - 2 * R
        while x_i <= y_i:     
            dsDiem.append((x + x_i, y + y_i))
            dsDiem.append((x + y_i, y + x_i))
            dsDiem.append((x + y_i, y - x_i))
            dsDiem.append((x + x_i, y - y_i))
            dsDiem.append((x - x_i, y - y_i))
            dsDiem.append((x - y_i, y - x_i))
            dsDiem.append((x - y_i, y + x_i))
            dsDiem.append((x - x_i, y + y_i))

            if P < 0:
                P += 4 * x_i + 6
            else:
                P += 4 * (x_i - y_i) + 10
                y_i -= 1
            x_i += 1
        
        if dsDiem:
            # Loại bỏ các điểm trùng lặp
            dsDiemSorted = sorted(list(set(dsDiem)))
            # Sắp xếp các điểm duy nhất theo góc giảm dần quanh tâm (x, y) cho thứ tự theo chiều kim đồng hồ 
            dsDiemSorted.sort(key=lambda p: math.atan2(p[1] - y, p[0] - x), reverse=True)
            dsDiem = dsDiemSorted
            # print(dsDiem)
    
            t.pencolor(color)
            t.fillcolor(color)
            t.penup()
            t.goto(dsDiem[0][0] * 5, dsDiem[0][1] * 5) # Điểm bắt đầu
            t.pendown()
            t.begin_fill()
            for diem in dsDiem:
                t.goto(diem[0] * 5, diem[1] * 5)
            t.goto(dsDiem[0][0] * 5, dsDiem[0][1] * 5)
            t.end_fill()
    else:
        x_i, y_i = 0, R
        P = 3 - 2 * R
        while x_i <= y_i:     
            drawPoint(x + x_i, y + y_i)
            drawPoint(x + y_i, y + x_i)
            drawPoint(x + y_i, y - x_i)
            drawPoint(x + x_i, y - y_i)
            drawPoint(x - x_i, y - y_i)
            drawPoint(x - y_i, y - x_i)
            drawPoint(x - y_i, y + x_i)
            drawPoint(x - x_i, y + y_i)

            if P < 0:
                P += 4 * x_i + 6
            else:
                P += 4 * (x_i - y_i) + 10
                y_i -= 1
            x_i += 1
    t.penup()

def drawMoon():
    color = "#ffef00"
    drawHinhTron(-72, 35, 10, color)

def drawDaGiac(dsDiem, color=None):
    if color is not None:
        t.pencolor(color)
        t.fillcolor(color)
        t.penup()
        t.goto(dsDiem[0][0] * 5, dsDiem[0][1] * 5)
        t.pendown()
        t.begin_fill()
        for diem in dsDiem:
            t.goto(diem[0] * 5, diem[1] * 5)
        t.goto(dsDiem[0][0] * 5, dsDiem[0][1] * 5)
        t.end_fill()
    else:
        for diem in dsDiem:
            drawPoint(diem[0], diem[1])

def drawHouse():
    color="#000000"
    # Mái nhà
    roof_points = [
        (-103, -58), (30, -58), (20, -36), (-103, -36)
    ]
    drawDaGiac(roof_points, color)
    # Ống khói
    chimney_points = [
        (-97, -16), (-97, -14), (-74, -14), (-74, -16), (-78, -16), (-78, -36), (-93, -36), (-93, -16)
    ]
    drawDaGiac(chimney_points, color)

def xoayTaiCat(dsDiem, pX, pY, gocQuay):
    if dsDiem:
        gocRad = math.radians(gocQuay)
        cosGoc = math.cos(gocRad)
        sinGoc = math.sin(gocRad)
        
        newDiem = []
        for x, y in dsDiem:
            # Dịch điểm về gốc tọa độ
            # Quay quanh gốc tọa độ mới
            # Dịch chuyển trở lại vị trí ban đầu
            newX = pX + cosGoc * (x - pX) - sinGoc * (y - pY)
            newY = pY + sinGoc * (x - pX) + cosGoc * (y - pY)
            newDiem.append((int(round(newX)), int(round(newY))))

        return newDiem
    else:
        return []

def drawTamGiacDeu(x, y, size, color=None, gocQuay=0):
    rad = gocQuay
    points = [
        (x, y),
        (x + size, y),
        (x + size / 2, y + (size * (3 ** 0.5)) / 2)
    ]
    points = xoayTaiCat(points, x + size / 2, y + (size * (3 ** 0.5)) / 6, rad)
    if color is not None:
        drawDaGiac(points, color)
    else:
        drawDaGiac(points)

def drawCat(x, y, gocQuay=0):
    color="#000000"
    rad = gocQuay
    # Thân
    drawHinhEllipse(-40, -26, 10, 11, color)
    drawHinhEllipse(-40, -13, 6, 9, color)
    # Đầu
    drawHinhEllipse(-40, -1, 7, 7, color)
    # Tai
    size = 6
    drawTamGiacDeu(x, y, size, color, gocQuay=rad)
    drawTamGiacDeu(x + 10, y, size, color, gocQuay=-rad)

def animation(offsetX=0):
    global isAnimating
    if not isAnimating:
        return
    start = time.time()
    t.clear()
    drawBackground()
    drawMoon()
    drawCloud(offsetX, 0)
    # screen.update()
    # offsetX += 3.5
    # # print(f"Offset X: {offsetX}")
    # if offsetX >= 312:
    #     offsetX = 0
    # elapsed = (time.time() - start) * 1000
    # delay = max(1, int(40 - elapsed))
    # t.getscreen().ontimer(lambda: animation(offsetX), delay)
    drawHouse()
    drawCat(-48, 3, 45)

def hienThiToaDo(hang):
    if not toaDo:
        print("Lỗi toaDo chưa được khởi tạo!")
        return
    
    if hang:
        final_text = "\n".join(hang)
        toaDo.config(text=final_text, font=('Arial', 12, 'normal'), fg='blue', justify=LEFT, anchor='nw')
    else:
        toaDo.config(text="HIỂN THỊ TỌA ĐỘ", font=('Arial', 12, 'italic'), fg='black', justify=LEFT, anchor='nw')
    
def input_table(root):
    frameInput = Frame(root, bd=2, width=446, height=566, relief=SOLID)
    frameInput.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    frameInput.grid_rowconfigure(0, weight=0) 
    frameInput.grid_rowconfigure(1, weight=1) 
    frameInput.grid_columnconfigure(0, weight=1)

    topInput = Frame(frameInput, width=446, height=283)
    topInput.grid(row=0, column=0, sticky="nsew")
    topInput.pack_propagate(False)
    global toaDo
    toaDo =Label(topInput, 
                  text="HIỂN THỊ TỌA ĐỘ", 
                  font=('Arial', 12, 'italic'), 
                  fg='black', 
                  justify=LEFT, 
                  anchor='nw')
    toaDo.pack(expand=True, fill='both', padx=0, pady=0) 

    bottomInput = Frame(frameInput, width=446, height=283)
    bottomInput.grid(row=1, column=0, sticky="nsew")
    bottomInput.grid_rowconfigure(0, weight=1)
    bottomInput.grid_columnconfigure(0, weight=1)

    notebook = ttk.Notebook(bottomInput)
    notebook.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    # Tab 2D
    tab2D = Frame(notebook)
    notebook.add(tab2D, text="PHẦN 2D")
    tab2D.grid_rowconfigure(0, weight=1)
    tab2D.grid_columnconfigure(0, weight=1)

    lf2D = LabelFrame(tab2D, padx=5, pady=5)
    lf2D.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
    lf2D.grid_columnconfigure(0, weight=1)
    lf2D.grid_columnconfigure(1, weight=1)

    # Hàng 1
    frame2DOpt = Frame(lf2D)
    frame2DOpt.grid_columnconfigure(0, weight=1, uniform=1)
    frame2DOpt.grid_columnconfigure(1, weight=1, uniform=1)
    frame2DOpt.grid(row=0, column=0, columnspan=2, sticky="ew", pady=10)
    btnAnimation = Button(frame2DOpt, text='Animation', pady=5,
                   command=None,
                   bg="#FF4444", fg="black", font=("Arial", 9, "bold"))
    btnAnimation.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    btnPhepBienDoi = Button(frame2DOpt, text='Các phép biến đổi', pady=5,
                   command=None,
                   bg="#4CAF50", fg="white", font=("Arial", 9, "bold")) 
    btnPhepBienDoi.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

    # Hàng 2
    frameDxy = Frame(lf2D)
    frameDxy.grid(row=1, column=0, sticky="ew", pady=10) 
    lblDx = Label(frameDxy, text='Dx:', font=("Arial", 10, "bold"))
    lblDx.grid(row=0, column=0, sticky="w", padx=5)
    txtDx = Entry(frameDxy, bd=2, width=8)
    txtDx.insert(0, "0")
    txtDx.grid(row=0, column=1, sticky="ew", padx=5)
    lblDy = Label(frameDxy, text='Dy:', font=("Arial", 10, "bold"))
    lblDy.grid(row=0, column=2, sticky="w", padx=5)
    txtDy = Entry(frameDxy, bd=2, width=8)
    txtDy.insert(0, "0")
    txtDy.grid(row=0, column=3, sticky="ew", padx=5)

    frameSxy = Frame(lf2D)
    frameSxy.grid(row=1, column=1, sticky="ew", pady=5) 
    lblSx = Label(frameSxy, text='Sx:', font=("Arial", 10, "bold"))
    lblSx.grid(row=0, column=0, sticky="w", padx=5)
    txtSx = Entry(frameSxy, bd=2, width=8)
    txtSx.insert(0, "1")
    txtSx.grid(row=0, column=1, sticky="ew", padx=5)
    lblSy = Label(frameSxy, text='Sy:', font=("Arial", 10, "bold"))
    lblSy.grid(row=0, column=2, sticky="w", padx=5)
    txtSy = Entry(frameSxy, bd=2, width=8)
    txtSy.insert(0, "1")
    txtSy.grid(row=0, column=3, sticky="ew", padx=5)

    frameBtn1 = Frame(lf2D)
    frameBtn1.grid(row=2, column=0, columnspan=2, sticky="ew")
    frameBtn1.grid_columnconfigure(0, weight=1, uniform=1)
    frameBtn1.grid_columnconfigure(1, weight=1, uniform=1)
    btnTinhTien = Button(frameBtn1, text='TỊNH TIẾN', pady=5,
                   command=lambda: tinhTien(int(txtDx.get()), int(txtDy.get())),
                   bg="#FF4444", fg="black", font=("Arial", 9, "bold"))
    btnTinhTien.grid(row=0, column=0, sticky="ew", padx=5)
    btnBienDoiTiLe = Button(frameBtn1, text='BIẾN ĐỔI TỈ LỆ', pady=5,
                   command=lambda: bienDoiTiLe(float(txtSx.get()), float(txtSy.get())),
                   bg="#4CAF50", fg="white", font=("Arial", 9, "bold")) 
    btnBienDoiTiLe.grid(row=0, column=1, sticky="ew", padx=5)

    # Hàng 3
    frameQuay = Frame(lf2D)
    frameQuay.grid(row=3, column=0, columnspan=2, sticky="ew", pady=15)

    lblP = Label(frameQuay, text='[Tọa độ P]', font=("Arial", 10, "bold"))
    lblP.grid(row=0, column=0, sticky="w", padx=5)
    lblPx = Label(frameQuay, text='x:', font=("Arial", 10, "bold"))
    lblPx.grid(row=0, column=1, sticky="w", padx=5)
    txtPx = Entry(frameQuay, bd=2, width=10)
    txtPx.insert(0, "0")
    txtPx.grid(row=0, column=2, sticky="ew", padx=5)
    lblPy = Label(frameQuay, text='y:', font=("Arial", 10, "bold"))
    lblPy.grid(row=0, column=3, sticky="w", padx=5)
    txtPy = Entry(frameQuay, bd=2, width=10)
    txtPy.insert(0, "0")
    txtPy.grid(row=0, column=4, sticky="ew", padx=5)
    lblGocQuay = Label(frameQuay, text='Góc:', font=("Arial", 10, "bold"))
    lblGocQuay.grid(row=0, column=5, sticky="w", padx=5)
    txtGocQuay = Entry(frameQuay, bd=2, width=10)
    txtGocQuay.insert(0, "0")
    txtGocQuay.grid(row=0, column=6, sticky="ew", padx=5, pady=10)
    btnQuayQuanhDiem = Button(frameQuay, text='QUAY QUANH ĐIỂM', pady=5,
                   command=lambda: quayQuanhDiem(float(txtPx.get()), float(txtPy.get()), float(txtGocQuay.get())),
                   bg="#9C27B0", fg="white", font=("Arial", 9, "bold")) 
    btnQuayQuanhDiem.grid(row=1, column=0, columnspan=7, sticky="ew", padx=5)

    # Hàng 4
    frameAxy = Frame(lf2D)
    frameAxy.grid(row=4, column=0, sticky="ew", padx=5)
    lblAx = Label(frameAxy, text='Ax:', font=("Arial", 10, "bold"))
    lblAx.grid(row=0, column=0, sticky="w", padx=5)
    txtAx = Entry(frameAxy, bd=2, width=8)
    txtAx.insert(0, "0")
    txtAx.grid(row=0, column=1, sticky="ew", padx=5)
    lblAy = Label(frameAxy, text='Ay:', font=("Arial", 10, "bold"))
    lblAy.grid(row=0, column=2, sticky="w", padx=5)
    txtAy = Entry(frameAxy, bd=2, width=8)
    txtAy.insert(0, "0")
    txtAy.grid(row=0, column=3, sticky="ew", padx=5)

    frameBxy = Frame(lf2D)
    frameBxy.grid(row=4, column=1, sticky="ew", pady=5)
    lblBx = Label(frameBxy, text='Bx:', font=("Arial", 10, "bold"))
    lblBx.grid(row=0, column=0, sticky="w", padx=5)
    txtBx = Entry(frameBxy, bd=2, width=8)
    txtBx.insert(0, "0")
    txtBx.grid(row=0, column=1, sticky="ew", padx=5)
    lblBy = Label(frameBxy, text='By:', font=("Arial", 10, "bold"))
    lblBy.grid(row=0, column=2, sticky="w", padx=5)
    txtBy = Entry(frameBxy, bd=2, width=8)
    txtBy.insert(0, "0")
    txtBy.grid(row=0, column=3, sticky="ew", padx=5)
    frameBtn2 = Frame(lf2D)
    frameBtn2.grid(row=5, column=0, columnspan=2, sticky="ew", pady=5)
    frameBtn2.grid_columnconfigure(0, weight=1, uniform=1)
    frameBtn2.grid_columnconfigure(1, weight=1, uniform=1)
    btnDoiXungDiem = Button(frameBtn2, text='DX ĐIỂM', pady=5,
                   command=lambda: doiXungDiem(int(txtAx.get()), int(txtAy.get())),
                   bg="#FFCC00", fg="black", font=("Arial", 9, "bold"))
    btnDoiXungDiem.grid(row=0, column=0, sticky="ew", padx=5)
    btnDoiXungDoan = Button(frameBtn2, text='DX ĐOẠN', pady=5,
                   command=lambda: doiXungDoanThang(int(txtAx.get()), int(txtAy.get()), int(txtBx.get()), int(txtBy.get())),
                   bg="#FF9800", fg="white", font=("Arial", 9, "bold")) 
    btnDoiXungDoan.grid(row=0, column=1, sticky="ew", padx=5)

    # Hàng 5
    frameDoiXung2 = Frame(lf2D)
    frameDoiXung2.grid(row=6, column=0, columnspan=2, sticky="ew", pady=5)
    frameDoiXung2.grid_columnconfigure(0, weight=1)
    frameDoiXung2.grid_columnconfigure(1, weight=1)
    frameDoiXung2.grid_columnconfigure(2, weight=1)
    btnDoiXungOx = Button(frameDoiXung2, text='DX qua Ox', pady=5,
                   command=doiXungQuaOX,
                   bg="#F44336", fg="white", font=("Arial", 9, "bold"))
    btnDoiXungOx.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    btnDoiXungOy = Button(frameDoiXung2, text='DX qua Oy', pady=5,
                   command=doiXungQuaOY,
                   bg="#2196F3", fg="white", font=("Arial", 9, "bold")) 
    btnDoiXungOy.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
    btnDoiXungO = Button(frameDoiXung2, text='DX qua O', pady=5,
                   command=doiXungQuaO,
                   bg="#795548", fg="white", font=("Arial", 9, "bold")) 
    btnDoiXungO.grid(row=0, column=2, sticky="ew", padx=5, pady=5)

    danhSachItem = [
        txtDx, txtDy, txtSx, txtSy,
        btnTinhTien, btnBienDoiTiLe,
        txtPx, txtPy, txtGocQuay, btnQuayQuanhDiem,
        txtAx, txtAy, txtBx, txtBy,
        btnDoiXungDiem, btnDoiXungDoan,
        btnDoiXungOx, btnDoiXungOy, btnDoiXungO
    ]

    def datTrangThai(targetState):
        for widget in danhSachItem:
            widget.config(state=targetState)

    def trangThaiAnimation():
        global isAnimating
        if isAnimating:
            isAnimating = False
        isAnimating = True
        datTrangThai(DISABLED)
        t.clear()
        drawOxy()
        animation()

    def trangThaiPhepBienDoi():
        global isAnimating
        isAnimating = False
        datTrangThai(NORMAL)
        t.clear()
        drawOxy()
        if hcn:
            t.pencolor('black') 
            t.fillcolor('#ff9999')
            drawHCN(*hcn)

    btnAnimation.config(command=trangThaiAnimation)
    btnPhepBienDoi.config(command=trangThaiPhepBienDoi)

    # Tab 3D (để trống)
    tab3D = Frame(notebook)
    notebook.add(tab3D, text="PHẦN 3D")
    tab3D.grid_rowconfigure(0, weight=1)
    tab3D.grid_columnconfigure(0, weight=1)

    lf3D = LabelFrame(tab3D, padx=5, pady=10)
    lf3D.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
    lf3D.grid_columnconfigure(0, weight=1)
    lf3D.grid_columnconfigure(1, weight=1)

    frameBtn3D = Frame(lf3D)
    frameBtn3D.grid(row=0, column=0, columnspan=2, sticky="ew", pady=5)
    frameBtn3D.grid_columnconfigure(0, weight=1)
    frameBtn3D.grid_columnconfigure(1, weight=1)
    frameBtn3D.grid_columnconfigure(2, weight=1)
    btnHinhHop = Button(frameBtn3D, text='Vẽ Hình Hộp', pady=5,
                   command=lambda: drawHinhHop(0, 0, 0, 30, 30, 30),
                   bg="#F44336", fg="white", font=("Arial", 9, "bold"))
    btnHinhHop.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    btnHinhChop = Button(frameBtn3D, text='Vẽ Hình Chóp', pady=5,
                   command=lambda: drawHinhChop(0, 0, 0, 30, 30, 30),
                   bg="#2196F3", fg="white", font=("Arial", 9, "bold")) 
    btnHinhChop.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
    btnHinhCau = Button(frameBtn3D, text='Vẽ Hình Cầu', pady=5,
                   command=lambda: drawHinhCau(0, 0, 0, 30),
                   bg="#795548", fg="white", font=("Arial", 9, "bold")) 
    btnHinhCau.grid(row=0, column=2, sticky="ew", padx=5, pady=5)

    frameTxt3D = Frame(lf3D)
    frameTxt3D.grid(row=1, column=0, columnspan=2, sticky="ew", pady=5)
    frameTxt3D.grid_columnconfigure(0, weight=1, uniform=1)
    frameTxt3D.grid_columnconfigure(1, weight=1, uniform=1)
    frameTxt3D.grid_columnconfigure(2, weight=1, uniform=1)
    frameHinhHop = Frame(frameTxt3D)
    frameHinhHop.grid(row=0, column=0, sticky="ew", padx=5)
    frameHinhHop.grid_columnconfigure(0, weight=1)
    frameHinhHop.grid_columnconfigure(1, weight=1)
    frameHinhChop = Frame(frameTxt3D)
    frameHinhChop.grid(row=0, column=1, sticky="ew", padx=5)
    frameHinhChop.grid_columnconfigure(0, weight=1)
    frameHinhChop.grid_columnconfigure(1, weight=1)
    frameHinhCau = Frame(frameTxt3D)
    frameHinhCau.grid(row=0, column=2, sticky="new", padx=5)
    frameHinhCau.grid_columnconfigure(0, weight=1)
    frameHinhCau.grid_columnconfigure(1, weight=1)

    lblToaDoA = Label(frameHinhHop, text='TỌA ĐỘ A', font=("Arial", 10, "bold"))
    lblToaDoA.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5)
    lblXA = Label(frameHinhHop, text='x:', font=("Arial", 10, "bold"))
    lblXA.grid(row=1, column=0, sticky="e")
    txtXA = Entry(frameHinhHop, bd=2, width=10)
    txtXA.insert(0, "0")
    txtXA.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
    lblYA = Label(frameHinhHop, text='y:', font=("Arial", 10, "bold"))
    lblYA.grid(row=2, column=0, sticky="e")
    txtYA = Entry(frameHinhHop, bd=2, width=10)
    txtYA.insert(0, "0")
    txtYA.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
    lblZA = Label(frameHinhHop, text='z:', font=("Arial", 10, "bold"))
    lblZA.grid(row=3, column=0, sticky="e")
    txtZA = Entry(frameHinhHop, bd=2, width=10)
    txtZA.insert(0, "0")
    txtZA.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

    lblToaDoA = Label(frameHinhHop, text='KÍCH THƯỚC', font=("Arial", 10, "bold"))
    lblToaDoA.grid(row=4, column=0, columnspan=2, sticky="ew", padx=5)
    lblChieuDai = Label(frameHinhHop, text='Dài:', font=("Arial", 10, "bold"))
    lblChieuDai.grid(row=5, column=0, sticky="e")
    txtChieuDai = Entry(frameHinhHop, bd=2, width=10)
    txtChieuDai.insert(0, "30")
    txtChieuDai.grid(row=5, column=1, sticky="ew", padx=5, pady=5)
    lblChieuRong = Label(frameHinhHop, text='Rộng:', font=("Arial", 10, "bold"))
    lblChieuRong.grid(row=6, column=0, sticky="e")
    txtChieuRong = Entry(frameHinhHop, bd=2, width=10)
    txtChieuRong.insert(0, "30")
    txtChieuRong.grid(row=6, column=1, sticky="ew", padx=5, pady=5)
    lblChieuCao = Label(frameHinhHop, text='Cao:', font=("Arial", 10, "bold"))
    lblChieuCao.grid(row=7, column=0, sticky="e")
    txtChieuCao = Entry(frameHinhHop, bd=2, width=10)
    txtChieuCao.insert(0, "30")
    txtChieuCao.grid(row=7, column=1, sticky="ew", padx=5, pady=5)

    lblToaDoA2 = Label(frameHinhChop, text='TỌA ĐỘ A', font=("Arial", 10, "bold"))
    lblToaDoA2.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5)
    lblXA2 = Label(frameHinhChop, text='x:', font=("Arial", 10, "bold"))
    lblXA2.grid(row=1, column=0, sticky="e")
    txtXA2 = Entry(frameHinhChop, bd=2, width=10)
    txtXA2.insert(0, "0")
    txtXA2.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
    lblYA2 = Label(frameHinhChop, text='y:', font=("Arial", 10, "bold"))
    lblYA2.grid(row=2, column=0, sticky="e")
    txtYA2 = Entry(frameHinhChop, bd=2, width=10)
    txtYA2.insert(0, "0")
    txtYA2.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
    lblZA2 = Label(frameHinhChop, text='z:', font=("Arial", 10, "bold"))
    lblZA2.grid(row=3, column=0, sticky="e")
    txtZA2 = Entry(frameHinhChop, bd=2, width=10)
    txtZA2.insert(0, "0")
    txtZA2.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

    lblKichThuoc2 = Label(frameHinhChop, text='KÍCH THƯỚC', font=("Arial", 10, "bold"))
    lblKichThuoc2.grid(row=4, column=0, columnspan=2, sticky="ew", padx=5)
    lblChieuDai2 = Label(frameHinhChop, text='Dài:', font=("Arial", 10, "bold"))
    lblChieuDai2.grid(row=5, column=0, sticky="e")
    txtChieuDai2 = Entry(frameHinhChop, bd=2, width=10)
    txtChieuDai2.insert(0, "30")
    txtChieuDai2.grid(row=5, column=1, sticky="ew", padx=5, pady=5)
    lblChieuRong2 = Label(frameHinhChop, text='Rộng:', font=("Arial", 10, "bold"))
    lblChieuRong2.grid(row=6, column=0, sticky="e")
    txtChieuRong2 = Entry(frameHinhChop, bd=2, width=10)
    txtChieuRong2.insert(0, "30")
    txtChieuRong2.grid(row=6, column=1, sticky="ew", padx=5, pady=5)
    lblChieuCao2 = Label(frameHinhChop, text='Cao:', font=("Arial", 10, "bold"))
    lblChieuCao2.grid(row=7, column=0, sticky="e")
    txtChieuCao2 = Entry(frameHinhChop, bd=2, width=10)
    txtChieuCao2.insert(0, "30")
    txtChieuCao2.grid(row=7, column=1, sticky="ew", padx=5, pady=5)

    lblToaDoI = Label(frameHinhCau, text='TỌA ĐỘ I', font=("Arial", 10, "bold"))
    lblToaDoI.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5)
    lblXI = Label(frameHinhCau, text='x:', font=("Arial", 10, "bold"))
    lblXI.grid(row=1, column=0, sticky="e")
    txtXI = Entry(frameHinhCau, bd=2, width=10)
    txtXI.insert(0, "0")
    txtXI.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
    lblYI = Label(frameHinhCau, text='y:', font=("Arial", 10, "bold"))
    lblYI.grid(row=2, column=0, sticky="e")
    txtYI = Entry(frameHinhCau, bd=2, width=10)
    txtYI.insert(0, "0")
    txtYI.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
    lblZI = Label(frameHinhCau, text='z:', font=("Arial", 10, "bold"))
    lblZI.grid(row=3, column=0, sticky="e")
    txtZI = Entry(frameHinhCau, bd=2, width=10)
    txtZI.insert(0, "0")
    txtZI.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

    lblKichThuoc3 = Label(frameHinhCau, text='KÍCH THƯỚC', font=("Arial", 10, "bold"))
    lblKichThuoc3.grid(row=4, column=0, columnspan=2, sticky="ew", padx=5)
    lblBanKinh = Label(frameHinhCau, text='R:', font=("Arial", 10, "bold"))
    lblBanKinh.grid(row=5, column=0, sticky="e")
    txtBanKinh = Entry(frameHinhCau, bd=2, width=10)
    txtBanKinh.insert(0, "30")
    txtBanKinh.grid(row=5, column=1, sticky="ew", padx=5, pady=5)

    danhSachItem2 = [
        lblToaDoA, lblXA, txtXA, lblYA, txtYA, lblZA, txtZA, 
        lblChieuDai, txtChieuDai, lblChieuRong, txtChieuRong, lblChieuCao, txtChieuCao
    ]
    danhSachItem3 = [
        lblToaDoA2, lblXA2, txtXA2, lblYA2, txtYA2, lblZA2, txtZA2,
        lblChieuDai2, txtChieuDai2, lblChieuRong2, txtChieuRong2, lblChieuCao2, txtChieuCao2
    ]
    danhSachItem4 = [
        lblToaDoI, lblXI, txtXI, lblYI, txtYI, lblZI, txtZI,
        lblBanKinh, txtBanKinh
    ]

    def datTrangThai2(targetState):
        for widget in danhSachItem2:
            widget.config(state=targetState)
    def datTrangThai3(targetState):
        for widget in danhSachItem3:
            widget.config(state=targetState)
    def datTrangThai4(targetState):
        for widget in danhSachItem4:
            widget.config(state=targetState)

    def trangThaiHinhHop():
        datTrangThai2(NORMAL)
        datTrangThai3(DISABLED)
        datTrangThai4(DISABLED)
        try:
            x = float(txtXA.get())
            y = float(txtYA.get())
            z = float(txtZA.get())
            dai = float(txtChieuDai.get())
            rong = float(txtChieuRong.get())
            cao = float(txtChieuCao.get())
            drawHinhHop(x, y, z, dai, rong, cao)
        except ValueError:
            print("Lỗi: Vui lòng nhập giá trị số hợp lệ cho các thông số hình hộp.")

    def trangThaiHinhChop():
        datTrangThai3(NORMAL)
        datTrangThai2(DISABLED)
        datTrangThai4(DISABLED)
        try:
            x = float(txtXA2.get())
            y = float(txtYA2.get())
            z = float(txtZA2.get())
            dai = float(txtChieuDai2.get())
            rong = float(txtChieuRong2.get())
            cao = float(txtChieuCao2.get())
            drawHinhChop(x, y, z, dai, rong, cao)
        except ValueError:
            print("Lỗi: Vui lòng nhập giá trị số hợp lệ cho các thông số hình chóp.")

    def trangThaiHinhCau():
        datTrangThai4(NORMAL)
        datTrangThai2(DISABLED)
        datTrangThai3(DISABLED)
        try:
            x = float(txtXI.get())
            y = float(txtYI.get())
            z = float(txtZI.get())
            ban_kinh = float(txtBanKinh.get())
            drawHinhCau(x, y, z, ban_kinh)
        except ValueError:
            print("Lỗi: Vui lòng nhập giá trị số hợp lệ cho các thông số hình cầu.")

    btnHinhHop.config(command=trangThaiHinhHop)
    btnHinhChop.config(command=trangThaiHinhChop)
    btnHinhCau.config(command=trangThaiHinhCau)

    def chuyenTab(event):
        global isAnimating
        isAnimating = False
        if p is None or t is None or screen is None:
            return

        selectedTabText = notebook.tab(notebook.select(), "text")
        
        t.clear()

        if selectedTabText == "PHẦN 2D":
            drawOxy()
            trangThaiPhepBienDoi()
        elif selectedTabText == "PHẦN 3D":
            drawOxyz()
            trangThaiHinhHop()
        
        screen.update()

    notebook.bind("<<NotebookTabChanged>>", chuyenTab)

def draw_table(root):
    draw = Frame(root, bd=2, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, relief=SOLID)
    draw.grid(row=0, column=1, padx=10)

    canvas = Canvas(draw, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    canvas.pack()

    global screen
    screen = turtle.TurtleScreen(canvas)
    screen.screensize(WINDOW_WIDTH, WINDOW_HEIGHT)
    screen.tracer(0)

    global p #Vẽ trục
    p = turtle.RawTurtle(screen)
    p.hideturtle()

    global t #Vẽ điểm
    t = turtle.RawTurtle(screen) 
    t.hideturtle()

    root.grid_columnconfigure(0, weight=0)
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(0, weight=1)

def main():
    root = Tk()
    root.title('ĐỒ ÁN CUỐI KỲ')
    root.minsize(1500, 750)
    
    draw_table(root)
    input_table(root)
    global hcn
    hcn = [15, 15, 40, 30]
    drawHCN(hcn[0], hcn[1], hcn[2], hcn[3])
    root.mainloop()

if __name__ == "__main__":
    main()