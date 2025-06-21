import turtle
from tkinter import *
from tkinter import ttk
import math
import time

WINDOW_WIDTH = 900
WINDOW_HEIGHT = WINDOW_WIDTH * 9 // 16

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
    p.goto(450, -25)
    p.write('x', align='right', font=('arial', 12, 'normal'))
    #Vẽ trục Oy
    p.penup()
    p.goto(0, -285)
    p.pendown()
    p.setheading(90) 
    p.forward(570)
    p.penup()
    p.goto(10, 240)
    p.write('y', align='left', font=('arial', 12, 'normal'))
    #Vẽ điểm O
    p.penup()
    p.goto(-2, -22)
    p.write('O', align='right', font=('arial', 12, 'normal'))
    p.setheading(0)

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
    p.goto(450, -25)
    p.write('x', align='right', font=('arial', 12, 'normal'))
    #Vẽ trục Oy
    p.penup()
    p.goto(0, 0)
    p.pendown()
    p.setheading(90)  
    p.forward(285)
    p.penup()
    p.goto(10, 240)
    p.pendown()
    p.write('y', align='left', font=('arial', 12, 'normal'))
    #Vẽ trục Oz
    p.penup()
    p.goto(0, 0)
    p.pendown()
    p.left(135)    
    p.forward(405)
    p.penup()
    p.goto(-260, -255)
    p.pendown()
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

def drawPoint(x, y, color='red', size=5):
    x *= 5
    y *= 5
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.dot(min(size, 10), color)

def drawLine(x1, y1, x2, y2, color='red', size=5):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    step_x = 1 if x2 > x1 else -1
    step_y = 1 if y2 > y1 else -1

    if dx > dy:
        P = 2 * dy - dx
        x, y = x1, y1
        while x != x2:
            drawPoint(x, y, color, size)
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
            drawPoint(x, y, color, size)
            if P < 0:
                P += 2 * dx
            else:
                P += 2 * dx - 2 * dy
                x += step_x
            y += step_y
    drawPoint(x2, y2, color, size)

def drawHCN(x1, y1, x2, y2, color='red'):
    # t.clear()
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    t.penup()
    t.goto(x1 * 5, y1 * 5)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    drawLine(x1, y1, x2, y1, color)
    drawLine(x2, y1, x2, y2, color)
    drawLine(x2, y2, x1, y2, color)
    drawLine(x1, y2, x1, y1, color)
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
def createHCN():
    global hcn
    hcn = [10, 10, 40, 25]
    t.clear()
    drawHCN(hcn[0], hcn[1], hcn[2], hcn[3])

def tinhTien(dx, dy):
    global hcn
    if hcn:
        t.clear()
        x1, y1, x2, y2 = hcn
        newX1 = x1 + dx
        newY1 = y1 + dy
        newX2 = x2 + dx
        newY2 = y2 + dy
        hcn = (newX1, newY1, newX2, newY2)
        drawHCN(newX1, newY1, newX2, newY2)
        clearToaDo()
        hienThiToaDo([
            "Thông số Hình chữ nhật:",
            f"A({newX1}, {newY1})",
            f"B({newX2}, {newY1})",
            f"C({newX2}, {newY2})",
            f"D({newX1}, {newY2})"
        ])
    else:
        print("Không có hình chữ nhật!")

def bienDoiTiLe(Sx, Sy):
    global hcn
    if hcn and Sx > 0 and Sy > 0:
        createHCN()
        t.clear()
        x1, y1, x2, y2 = hcn
        newX1 = x1
        newY1 = y1
        newX2 = x2 * Sx
        newY2 = y2 * Sy
        # print(newX1, newY1, newX2, newY2)
        hcn = (newX1, newY1, newX2, newY2)
        drawHCN(newX1, newY1, newX2, newY2)
        clearToaDo()
        hienThiToaDo([
            "Thông số Hình chữ nhật:",
            f"A({round(newX1, 1)}, {round(newY1, 1)})",
            f"B({round(newX2, 1)}, {round(newY1, 1)})",
            f"C({round(newX2, 1)}, {round(newY2, 1)})",
            f"D({round(newX1, 1)}, {round(newY2, 1)})"
        ])
    else:
        print("Không có hình chữ nhật hoặc tỉ lệ không hợp lệ!")

def quayQuanhDiem(pX, pY, gocQuay):
    global hcn
    if hcn:
        createHCN()
        t.clear()
        color = 'red'
        color_text = 'blue'
        pX2 = pX * 5
        pY2 = pY * 5
        
        t.penup()
        t.goto(pX2, pY2)
        t.pendown()
        t.dot(8, color_text)
        
        t.penup()
        t.goto(pX2 - 2, pY2 + 2) 
        t.pencolor(color_text)
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

        # hcn = (newDiem[0][0], newDiem[0][1], newDiem[2][0], newDiem[2][1])
        t.penup()
        t.pencolor(color)
        t.fillcolor(color)
        t.penup()
        t.goto(newDiem[0][0] * 5, newDiem[0][1] * 5)
        t.pendown()
        t.begin_fill()
        slCanh = len(newDiem)
        for i in range(slCanh):
            pDau = newDiem[i]
            pCuoi = newDiem[(i + 1) % slCanh]
            drawLine(pDau[0], pDau[1], pCuoi[0], pCuoi[1], color)
        t.goto(newDiem[0][0] * 5, newDiem[0][1] * 5)
        t.end_fill()
        t.penup()

        clearToaDo()
        hienThiToaDo([
            "Thông số Hình chữ nhật:",
            f"A({newDiem[0][0]}, {newDiem[0][1]})",
            f"B({newDiem[1][0]}, {newDiem[1][1]})",
            f"C({newDiem[2][0]}, {newDiem[2][1]})",
            f"D({newDiem[3][0]}, {newDiem[3][1]})"
        ])
    else:
        print("Không có hình chữ nhật!")

def doiXungQuaO():
    global hcn
    if hcn:
        createHCN()
        # t.clear() 
        x1, y1, x2, y2  = hcn
        
        newX1 = -x1  
        newY1 = -y1  
        newX2 = -x2  
        newY2 = -y2
        # hcn = (newX1, newY1, newX2, newY2)
        drawHCN(newX1, newY1, newX2, newY2)
        clearToaDo()
        hienThiToaDo([
            "Thông số Hình chữ nhật:",
            f"A({round(newX1, 1)}, {round(newY1, 1)})",
            f"B({round(newX2, 1)}, {round(newY1, 1)})",
            f"C({round(newX2, 1)}, {round(newY2, 1)})",
            f"D({round(newX1, 1)}, {round(newY2, 1)})"
        ])
    else:
        print("Không có hình chữ nhật!")

def doiXungQuaOX():
    global hcn
    if hcn:
        createHCN()
        # t.clear()
        x1, y1, x2, y2  = hcn
        
        newX1 = x1  
        newY1 = -y1  
        newX2 = x2
        newY2 = -y2
        # hcn = (newX1, newY1, newX2, newY2)
        drawHCN(newX1, newY1, newX2, newY2)
        clearToaDo()
        hienThiToaDo([
            "Thông số Hình chữ nhật:",
            f"A({newX1}, {newY1})",
            f"B({newX2}, {newY1})",
            f"C({newX2}, {newY2})",
            f"D({newX1}, {newY2})"
        ])
    else:
        print("Không có hình chữ nhật!")

def doiXungQuaOY():
    global hcn
    if hcn:
        createHCN()
        # t.clear()
        x1, y1, x2, y2  = hcn
        
        newX1 = -x1  
        newY1 = y1  
        newX2 = -x2
        newY2 = y2
        hcn = (newX1, newY1, newX2, newY2)
        drawHCN(newX1, newY1, newX2, newY2)
        clearToaDo()
        hienThiToaDo([
            "Thông số Hình chữ nhật:",
            f"A({newX1}, {newY1})",
            f"B({newX2}, {newY1})",
            f"C({newX2}, {newY2})",
            f"D({newX1}, {newY2})"
        ])
    else:
        print("Không có hình chữ nhật nào để thực hiện đối xứng. Hãy vẽ một hình chữ nhật trước.")

def doiXungDiem(xA, yA):
    global hcn
    if hcn:
        createHCN()
        # t.clear()
        color = 'red'
        color_text = 'blue'
        xA2 = xA * 5
        yA2 = yA * 5
        
        t.penup()
        t.goto(xA2, yA2)
        t.pendown()
        t.dot(8, color_text)
        
        t.penup()
        t.goto(xA2 - 2, yA2 + 2) 
        t.pencolor(color_text)
        t.pendown()
        t.write('A', align='right', font=('arial', 15, 'normal'))

        x1, y1, x2, y2  = hcn
        
        newX1 = 2*xA - x1
        newY1 = 2*yA - y1
        newX2 = 2*xA - x2
        newY2 = 2*yA - y2
        hcn = (newX1, newY1, newX2, newY2)
        drawHCN(newX1, newY1, newX2, newY2, color)
        clearToaDo()
        hienThiToaDo([
            "Thông số Hình chữ nhật:",
            f"A({newX1}, {newY1})",
            f"B({newX2}, {newY1})",
            f"C({newX2}, {newY2})",
            f"D({newX1}, {newY2})"
        ])
    else:
        print("Không có hình chữ nhật!")

def doiXungDoanThang(xA, yA, xB, yB):
    global hcn
    if hcn and (xA != xB or yA != yB):
        createHCN()
        # t.clear() 
        color = 'red'
        color_text = 'blue'
        xA2 = xA * 5
        yA2 = yA * 5
        xB2 = xB * 5
        yB2 = yB * 5
        
        t.penup()
        t.goto(xA2, yA2)
        t.pendown()
        t.dot(8, color_text)
        
        t.penup()
        t.goto(xA2 - 2, yA2 + 2) 
        t.pencolor(color_text)
        t.pendown()
        t.write('A', align='right', font=('arial', 15, 'normal'))

        t.penup()
        t.goto(xB2, yB2)
        t.pendown()
        t.dot(8, color_text)
        
        t.penup()
        t.goto(xB2 - 2, yB2 + 2)
        t.pencolor(color_text)
        t.pendown()
        t.write('B', align='right', font=('arial', 15, 'normal'))

        drawLine(xA, yA, xB, yB, color_text)

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
        
        # hcn = (newDiem[0][0], newDiem[0][1], newDiem[2][0], newDiem[2][1])
        t.penup()
        t.pencolor(color)
        t.fillcolor(color)
        t.penup()
        t.goto(newDiem[0][0] * 5, newDiem[0][1] * 5)
        t.pendown()
        t.begin_fill()
        slCanh = len(newDiem)
        for i in range(slCanh):
            pDau = newDiem[i]
            pCuoi = newDiem[(i + 1) % slCanh]
            drawLine(pDau[0], pDau[1], pCuoi[0], pCuoi[1], color)
        t.goto(newDiem[0][0] * 5, newDiem[0][1] * 5)
        t.end_fill()
        t.penup()

        clearToaDo()
        hienThiToaDo([
            "Thông số Hình chữ nhật:",
            f"A({newDiem[0][0]}, {newDiem[0][1]})",
            f"B({newDiem[1][0]}, {newDiem[1][1]})",
            f"C({newDiem[2][0]}, {newDiem[2][1]})",
            f"D({newDiem[3][0]}, {newDiem[3][1]})"
        ])
    else:
        print("Không có hình chữ nhật hoặc đoạn thẳng!")

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

def drawHinhEllipse3D2(x, y, a, b):
    x_i, y_i = 0, b
    P = b**2 - a**2 * b + a**2 / 4
    len_dash = 5
    while a**2 * (y_i - 0.5) > b**2 * (x_i + 1):
        if len_dash >= 3:           
            drawPoint(x + x_i, y + y_i)
            drawPoint(x + x_i, y - y_i) 
        len_dash -= 1
        if len_dash == 0:  
            len_dash = 5
        drawPoint(x - x_i, y + y_i)
        drawPoint(x - x_i, y - y_i) 
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
            drawPoint(x + x_i, y - y_i) 
        len_dash -= 1
        if len_dash == 0:  
            len_dash = 5
        drawPoint(x - x_i, y + y_i)
        drawPoint(x - x_i, y - y_i) 
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
    display_coords = ["Thông số Hình hộp"]
    for idx, (point3D, point2D, label) in enumerate(points):
        px, py = point2D
        t.penup()
        t.goto((px - 1) * 5, py * 5)  # Dịch sang trái 2 pixel
        t.pendown()
        t.pencolor('blue')
        t.write(label, align='right', font=('arial', 12, 'normal'))
        
        # Thêm tọa độ vào danh sách hiển thị
        display_coords.append(f"{label}({point3D[0]}, {point3D[1]}, {point3D[2]})")
    clearToaDo()
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
    
    # Tọa độ hiển thị bên trái
    
    display_coords = ["Thông số Hình chóp"]
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
    clearToaDo()
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
    drawHinhEllipse3D2(px, py, ban_kinh * factor, ban_kinh)
    
    # Hiển thị tên và tọa độ tâm
    t.penup()
    t.goto((px - 1) * 5, py * 5)
    t.pendown()
    t.pencolor('blue')
    t.write("I", align='right', font=('arial', 12, 'normal'))
    
    # Hiển thị tọa độ tâm và bán kính
    clearToaDo()
    hienThiToaDo([
        "Thông số Hình cầu",
        f"Tâm: I({O[0]}, {O[1]}, {O[2]})",
        f"Bán kính: {ban_kinh}",
    ])

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

def drawMoon():
    color = "#ffef00"
    drawHinhTron(-63, 30, 9, color)
    hienThiToaDo([
        f"Mặt Trăng (Tròn): (-63, 30), Bán kính = 9"
    ])

def drawLineStar(x1, y1, x2, y2):
    dsDiem = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    step_x = 1 if x2 > x1 else -1
    step_y = 1 if y2 > y1 else -1

    if dx > dy:
        P = 2 * dy - dx
        x, y = x1, y1
        while x != x2:
            # drawPoint(x, y, color)
            dsDiem.append((x, y))
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
            # drawPoint(x, y, color)
            dsDiem.append((x, y))
            if P < 0:
                P += 2 * dx
            else:
                P += 2 * dx - 2 * dy
                x += step_x
            y += step_y

    # drawPoint(x2, y2, color)
    dsDiem.append((x2, y2))  
    return dsDiem

def line_intersection(p1, p2, p3, p4):
    # Tìm giao điểm của đoạn p1-p2 và p3-p4
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    d = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
    if d == 0:
        return None  # song song
    px = ((x1*y2 - y1*x2)*(x3-x4) - (x1-x2)*(x3*y4 - y3*x4)) / d
    py = ((x1*y2 - y1*x2)*(y3-y4) - (y1-y2)*(x3*y4 - y3*x4)) / d
    return (px, py)

def drawStar(gocQuay=0, a=5, offset=(0, 0)):
    color='#7675ad'
    star_positions = [
        (-86, 9), (-75, -16), (-57, 0), (-47, 33),
        (-36, -8), (-29, 23), (-8, 13), (-3, -8),
        (13, 43), (25, -7), (33, 34), (44, -21), 
        (54, 15), (76, 25), (82, -4), (88, -25)
    ]
    for x, y in star_positions:
        x += offset[0]
        y += offset[1]
    for x, y in star_positions:
        # Tính 5 đỉnh đều trên đường tròn
        points = []
        for i in range(5):
            angle = math.radians(i * 72 + 90)  # - 90: Quay xuống
            px = x + a * math.cos(angle)
            py = y + a * math.sin(angle)
            # print(px, py)
            points.append((int(round(px)), int(round(py))))

        points = xoayQuanhDiem(points, x, y, gocQuay)
        # Thứ tự vẽ ngôi sao: nối cách 2 đỉnh
        order = [0, 2, 4, 1, 3, 0]

        dsDiem = []
        for i in range(len(order) - 1):
            x1, y1 = points[order[i]]
            x2, y2 = points[order[i + 1]]
            dsDiem += drawLineStar(x1, y1, x2, y2)
        # print(dsDiem)
        points.sort(key=lambda p: math.atan2(p[1] - y, p[0] - x), reverse=True)
        # Điểm giao nhau của các cạnh
        inner_points = []
        for i in range(5):
            p1 = points[i]
            p2 = points[(i+2)%5]
            p3 = points[(i+1)%5]
            p4 = points[(i+3)%5]
            inter = line_intersection(p1, p2, p3, p4)
            if inter is not None:
                inner_points.append(inter)
        # 1. Tô ngũ giác ở giữa
        t.pencolor(color)
        t.fillcolor(color)
        t.penup()
        t.goto(inner_points[0][0] * 5, inner_points[0][1] * 5)
        t.pendown()
        t.begin_fill()
        for p in inner_points[1:]:
            if p is not None:
                drawPoint(p[0], p[1], color)
        t.goto(inner_points[0][0] * 5, inner_points[0][1] * 5)
        t.end_fill()
        t.penup()
        # Tô màu ngôi sao
        t.pencolor(color)
        t.fillcolor(color)
        t.penup()
        t.goto(dsDiem[0][0] * 5, dsDiem[0][1] * 5)
        t.pendown()
        t.begin_fill()
        for diem in dsDiem[1:]:
            if diem is not None:
                drawPoint(diem[0], diem[1], color)
        t.goto(dsDiem[0][0] * 5, dsDiem[0][1] * 5)
        t.end_fill()
    t.penup()

    hienThiToaDo([
        f"Ngôi sao: Bán kính {round(a, 1)}, {star_positions}"
    ])

def drawStar2(x, y, gocQuay=0, a=5, offset=(0, 0)):
    color='#ffffff'
    x += offset[0]
    y += offset[1]
    # Tính 5 đỉnh đều trên đường tròn
    points = []
    for i in range(5):
        angle = math.radians(i * 72 + 90)  # - 90: Quay xuống
        px = x + a * math.cos(angle)
        py = y + a * math.sin(angle)
        # print(px, py)
        points.append((int(round(px)), int(round(py))))

    points = xoayQuanhDiem(points, x, y, gocQuay)
    # Thứ tự vẽ ngôi sao: nối cách 2 đỉnh
    order = [0, 2, 4, 1, 3, 0]

    dsDiem = []
    for i in range(len(order) - 1):
        x1, y1 = points[order[i]]
        x2, y2 = points[order[i + 1]]
        dsDiem += drawLineStar(x1, y1, x2, y2)
    # print(dsDiem)
    points.sort(key=lambda p: math.atan2(p[1] - y, p[0] - x), reverse=True)
    # Điểm giao nhau của các cạnh
    inner_points = []
    for i in range(5):
        p1 = points[i]
        p2 = points[(i+2)%5]
        p3 = points[(i+1)%5]
        p4 = points[(i+3)%5]
        inter = line_intersection(p1, p2, p3, p4)
        if inter is not None:
            inner_points.append(inter)
    # 1. Tô ngũ giác ở giữa
    t.pencolor(color)
    t.fillcolor(color)
    t.penup()
    if inner_points:
        t.goto(inner_points[0][0] * 5, inner_points[0][1] * 5)
    t.pendown()
    t.begin_fill()
    for p in inner_points[1:]:
        if p is not None:
            drawPoint(p[0], p[1], color)
    if inner_points:
        t.goto(inner_points[0][0] * 5, inner_points[0][1] * 5)
    t.end_fill()
    t.penup()
    # Tô màu ngôi sao
    t.pencolor(color)
    t.fillcolor(color)
    t.penup()
    t.goto(dsDiem[0][0] * 5, dsDiem[0][1] * 5)
    t.pendown()
    t.begin_fill()
    for diem in dsDiem[1:]:
        if diem is not None:
            drawPoint(diem[0], diem[1], color)
    t.goto(dsDiem[0][0] * 5, dsDiem[0][1] * 5)
    t.end_fill()
    t.penup()

def drawSaoBang(gocQuay=0, a=5, offset=(0, 0), scale1=(1, 1), scale2=(1, 1), length=0):
    color = 'white'
    radTia=45
    star_positions = [
        (-63, 54), (97, 37), (3, 35), (41, -21),
        (-59, -13), (67, 13), (13, 0), (45,50),
    ]
    tia = []
    for x, y in star_positions:
        x += offset[0]
        y += offset[1]
        drawStar2(x, y, gocQuay, a, (offset[0], offset[1]))
        x1 = x * scale1[0]
        y1 = y * scale1[1]
        x2 = (x1 - length) * scale2[0]
        y2 = y1 * scale2[1]
        tia = xoayQuanhDiem([(x1, y1), (x2, y1), (x2, y2), (x1, y2)], x1, y1, radTia)
        # print(tia)
        drawLine(tia[0][0], tia[0][1], tia[1][0], tia[1][1], color, 8)
    hienThiToaDo([
        "Thông số Sao Băng:",
        f"Sao Băng: Bán kính {round(a, 1)}, {star_positions}",
        f"Tia sao băng (Đoạn thẳng): {tia}",
    ])

def drawHinhEllipse(x, y, a, b, color='black', gocQuay=0):
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
        if gocQuay != 0:
            dsDiem = xoayQuanhDiem(dsDiem, x, y, gocQuay)
        # print(dsDiem)
        
        t.pencolor(color)
        t.fillcolor(color)
        t.penup()
        t.goto(dsDiem[0][0] * 5, dsDiem[0][1] * 5)
        t.pendown()
        t.begin_fill()
        for diem in dsDiem:
            if diem is not None:
                drawPoint(diem[0], diem[1], color)
        t.goto(dsDiem[0][0] * 5, dsDiem[0][1] * 5)
        t.end_fill()
    t.penup()

def setUpDrawCloud():
    scale1 = 0.6
    scale2 = 0.33
    offset_scale1 = 0.9
    offset_scale2 = 0.6

    cloud1_info = [
        (int(-20*offset_scale1), int(-4*offset_scale1), int(11*scale1), int(7*scale1)),
        (int(0*offset_scale1), int(3*offset_scale1), int(14*scale1), int(11*scale1)),
        (int(12*offset_scale1), int(2*offset_scale1), int(15*scale1), int(8*scale1)),
        (int(-7*offset_scale1), int(8*offset_scale1), int(9*scale1), int(5*scale1)),
        (int(8*offset_scale1), int(7*offset_scale1), int(11*scale1), int(7*scale1)),
        (int(-24*offset_scale1), int(-6*offset_scale1), int(8*scale1), int(4*scale1)),
        (int(24*offset_scale1), int(2*offset_scale1), int(10*scale1), int(6*scale1)),
        (int(-4*offset_scale1), int(-7*offset_scale1), int(14*scale1), int(10*scale1)),
        (int(6*offset_scale1), int(-7*offset_scale1), int(11*scale1), int(8*scale1)),
        (int(-15*offset_scale1), int(-6*offset_scale1), int(10*scale1), int(6*scale1)),
        (int(20*offset_scale1), int(-2*offset_scale1), int(12*scale1), int(8*scale1)),
        (int(0*offset_scale1), int(-12*offset_scale1), int(8*scale1), int(4*scale1)),
        (int(-12*offset_scale1), int(1*offset_scale1), int(14*scale1), int(10*scale1)),
        (int(12*offset_scale1), int(-6*offset_scale1), int(7*scale1), int(4*scale1))
    ]
    cloud1_definition = {
        "centerX": -165, "centerY": -10,
        # "centerX": 0, "centerY": -10,
        "ellipses_info": cloud1_info, "color": "#6c6995"
    }

    cloud2_info = [
        (int(-11*offset_scale2*0.88), int(3*offset_scale2*0.88), int(17*scale2*0.88), int(9*scale2*0.88)),
        (int(2*offset_scale2*0.88), int(-2*offset_scale2*0.88), int(20*scale2*0.88), int(13*scale2*0.88)),
        (int(25*offset_scale2*0.88), int(5*offset_scale2*0.88), int(13*scale2*0.88), int(8*scale2*0.88)),
        (int(2*offset_scale2*0.88), int(7*offset_scale2*0.88), int(19*scale2*0.88), int(10*scale2*0.88)),
        (int(14*offset_scale2*0.88), int(10*offset_scale2*0.88), int(21*scale2*0.88), int(10*scale2*0.88)),
        (int(-25*offset_scale2*0.88), int(-5*offset_scale2*0.88), int(11*scale2*0.88), int(6*scale2*0.88)),
        (int(33*offset_scale2*0.88), int(0*offset_scale2*0.88), int(12*scale2*0.88), int(8*scale2*0.88)),
        (int(0*offset_scale2*0.88), int(-8*offset_scale2*0.88), int(17*scale2*0.88), int(12*scale2*0.88)),
        (int(10*offset_scale2*0.88), int(-10*offset_scale2*0.88), int(13*scale2*0.88), int(8*scale2*0.88)),
        (int(-14*offset_scale2*0.88), int(-6*offset_scale2*0.88), int(20*scale2*0.88), int(10*scale2*0.88)),
        (int(18*offset_scale2*0.88), int(-2*offset_scale2*0.88), int(25*scale2*0.88), int(16*scale2*0.88)),
        (int(-10*offset_scale2*0.88), int(-12*offset_scale2*0.88), int(10*scale2*0.88), int(5*scale2*0.88)),
        (int(30*offset_scale2*0.88), int(-6*offset_scale2*0.88), int(12*scale2*0.88), int(7*scale2*0.88))
    ]
    cloud2_definition = {
        "centerX": -135, "centerY": 35,
        # "centerX": 0, "centerY": 35,
        "ellipses_info": cloud2_info, "color": "#9e9dbd"
    }
    return [cloud1_definition, cloud2_definition]

def drawCloud(x=0, y=0):
    all_cloud_info = setUpDrawCloud()

    for cloud in all_cloud_info:
        centerX = cloud["centerX"]
        centerY = cloud["centerY"]
        ellipses_info = cloud["ellipses_info"]
        color = cloud["color"]
        
        for offsetX, offsetY, a, b in ellipses_info:
            drawHinhEllipse(centerX + offsetX + x, centerY + offsetY + y, a, b, color)
    # Hiển thị thông số toạ độ đám mây
    hienThiToaDo([
        "Thông số Đám Mây:",
        f"Mây 1 (14 Ellipse): ({all_cloud_info[0]['centerX'] + x}, {all_cloud_info[0]['centerY'] + y}), a = {all_cloud_info[0]['ellipses_info'][0][2]}, b = {all_cloud_info[0]['ellipses_info'][0][3]}",
        f"Mây 2 (13 Ellipse): ({all_cloud_info[1]['centerX'] + x}, {all_cloud_info[1]['centerY'] + y}), a = {all_cloud_info[1]['ellipses_info'][0][2]}, b = {all_cloud_info[1]['ellipses_info'][0][3]}"
    ])

def drawHinhTron(x, y, R, color='black'):
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
            if diem is not None:
                drawPoint(diem[0], diem[1], color)
        t.goto(dsDiem[0][0] * 5, dsDiem[0][1] * 5)
        t.end_fill()
    t.penup()

def drawDaGiac(dsDiem, color='black'):
    t.pencolor(color)
    t.fillcolor(color)
    t.penup()
    t.goto(dsDiem[0][0] * 5, dsDiem[0][1] * 5)
    t.pendown()
    t.begin_fill()
    n = len(dsDiem)
    for i in range(n):
        x1, y1 = dsDiem[i]
        x2, y2 = dsDiem[(i + 1) % n]
        drawLine(x1, y1, x2, y2, color)
    t.goto(dsDiem[0][0] * 5, dsDiem[0][1] * 5)
    t.end_fill()
    t.penup()

def drawHouse():
    color="#000000"
    # Mái nhà
    roof_points = [
        (-90, -51), (26, -51), (18, -32), (-90, -32)
    ]
    drawDaGiac(roof_points, color)
    # Ống khói
    chimney_points = [
        (-85, -14), (-85, -12), (-65, -12), (-65, -14), (-69, -14), (-69, -32), (-81, -32), (-81, -14)
    ]
    drawDaGiac(chimney_points, color)

    hienThiToaDo([
        "Thông số Nhà:",
        f"Mái nhà (Đa giác): {roof_points}",
        f"Ống khói (Đa giác): {chimney_points}"
    ])

def setupDrawLeaf():
    scale_leaf = 0.3
    offset_scale_leaf = 1
    leaf_info = [
        (int(-20 * offset_scale_leaf * scale_leaf), int(-10 * offset_scale_leaf * scale_leaf), int(40 * scale_leaf), int(30 * scale_leaf)),
        (int(10 * offset_scale_leaf * scale_leaf), int(0 * offset_scale_leaf * scale_leaf), int(30 * scale_leaf), int(23 * scale_leaf)),
        (int(-20 * offset_scale_leaf * scale_leaf), int(20 * offset_scale_leaf * scale_leaf), int(35 * scale_leaf), int(25 * scale_leaf)),
    ]
    leaf_definition = {"ellipses_info": leaf_info}
    return [leaf_definition]

def drawTree(gocQuay=80):
    offset_x = 90
    offset_y = 50
    color = 'black'
    base_branches = [
        (0, 0, -36, 30, 20),
        (-14, 12, -30, 10, 14),
        (-30, 10, -44, 16, 10),
        (-36, 30, -56, 44, 12),
        (-36, 30, -30, 50, 12),
        (-44, 16, -50, 14, 8),
        (-56, 44, -60, 50, 8),
        (-30, 50, -24, 56, 8),
        (-26, 22, -18, 34, 12),
    ]
    
    leaf_shapes = setupDrawLeaf()
    small_leaf_shape = leaf_shapes[0]["ellipses_info"]
    leaf_placement_points = [
        # Tán lá ở dưới trái, dưới phải
        (-50, -50),
        (-14, -40),
        # Tán lá ở trên trái, trên phải
        (-29, -9), 
        (-50, -20), 
    ]

    for x, y in leaf_placement_points:
        viTri = xoayQuanhDiem([(x, y)], 0, 0, gocQuay-80)
        cx, cy = viTri[0][0] + offset_x, viTri[0][1] + offset_y
        for x_offset, y_offset, w, h in small_leaf_shape:
            drawHinhEllipse(cx + x_offset, cy + y_offset, w, h, color)

    for x1, y1, x2, y2, width in base_branches:     
        viTri = xoayQuanhDiem([(x1, y1), (x2, y2)], 0, 0, gocQuay)
        p1_x, p1_y = viTri[0][0] + offset_x, viTri[0][1] + offset_y
        p2_x, p2_y = viTri[1][0] + offset_x, viTri[1][1] + offset_y
        drawLine(p1_x, p1_y, p2_x, p2_y, color, width)
    hienThiToaDo([
        "Thông số Cây:",
        f"Nhánh (Đoạn thẳng): {base_branches}",
        f"Tán lá (Ellipse): {small_leaf_shape}",
    ])

def xoayQuanhDiem(dsDiem, pX, pY, gocQuay):
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

def drawTamGiacDeu(x, y, size, color='black', gocQuay=0):
    rad = gocQuay
    points = [
        (x, y),
        (x + size, y),
        (x + size / 2, y + (size * (3 ** 0.5)) / 2)
    ]
    points = xoayQuanhDiem(points, (2 * x + size) / 2, y, rad)
    t.pencolor(color)
    t.fillcolor(color)
    t.penup()
    t.goto(points[0][0] * 5, points[0][1] * 5)
    t.pendown()
    t.begin_fill()
    drawLine(points[0][0], points[0][1], points[1][0], points[1][1], color)
    drawLine(points[1][0], points[1][1], points[2][0], points[2][1], color)
    drawLine(points[2][0], points[2][1], points[0][0], points[0][1], color)
    t.goto(points[0][0] * 5, points[0][1] * 5)
    t.end_fill()
    t.penup()

def drawCat(gocQuay=0):
    color = "#4a5a6a"
    color_chan = "#43505E"
    x = -35
    y = -23
    a = 9
    b = 10
    rad = gocQuay
    # Thân
    drawHinhEllipse(x, y, a, b, color)
    drawHinhEllipse(x, y//2, a-4, b-2, color)
    # Đầu
    drawHinhEllipse(x, y+22, a-3, b-3, color)
    # Tai
    size = 7
    drawTamGiacDeu(x-8, y+25, size, color, gocQuay=rad)
    drawTamGiacDeu(x+1, y+25, size, color, gocQuay=-rad)
    # Chân
    drawHCN(x-4, y//2, x-1, y-8, color_chan)
    drawHinhEllipse(x-3, y-9, 3, 1, color_chan)
    drawHCN(x+1, y//2, x+4, y-8, color_chan)
    drawHinhEllipse(x+3, y-9, 3, 1, color_chan)

    hienThiToaDo([
        "Thông số Mèo:",
        f"Thân lớn (Ellipse): ({x}, {y}), a lớn = {a}, b lớn = {b}",
        f"Thân nhỏ (Ellipse): ({x}, {y//2}), a nhỏ = {a-4}, b nhỏ = {b-2}",
        f"Đầu (Ellipse): ({x}, {y+22}), a = {a-3}, b = {b-3}",
        f"Tai trái (Tam giác đều): ({x-8}, {y+25}), Góc quay = {rad}, Kích thước = {size}",
        f"Tai phải (Tam giác đều): ({x+1}, {y+25}), Góc quay = {-rad}, Kích thước = {size}",
        f"Chân trái (Hình chữ nhật): ({x-4}, {y//2}), ({x-1}, {y-8})",
        f"Chân phải (Hình chữ nhật): ({x+1}, {y//2}), ({x+4}, {y-8})"
    ])

def createTailCat(x, y, a, b, isReverse=False):
    # Tạo một danh sách các điểm (x_i, y_i) tương đối của 1/4 cung ellipse (góc phần tư 1)
    # Điểm được sắp xếp từ trục y dương (0, b) đến trục x dương (a, 0)
    tail_points = []
    x_i, y_i = 0, b
    P = b**2 - a**2 * b + a**2 / 4
    while a**2 * (y_i - 0.5) > b**2 * (x_i + 1):         
        tail_points.append((x + x_i, y + y_i))
        # tail_points.append((x - x_i, y + y_i))
        # tail_points.append((x - x_i, y - y_i))
        tail_points.append((x + x_i, y - y_i))
        if P < 0:
            P += b**2 * (2 * x_i + 3)
        else:
            P += b**2 * (2 * x_i + 3) + a**2 * (-2 * y_i + 2)
            y_i -= 1
        x_i += 1

    Q = b**2 * (x_i + 0.5)**2 + a**2 * (y_i - 1)**2 - a**2 * b**2
    while y_i >= 0:          
        tail_points.append((x + x_i, y + y_i))
        # tail_points.append((x - x_i, y + y_i))
        # tail_points.append((x - x_i, y - y_i))
        tail_points.append((x + x_i, y - y_i))
        if Q < 0:
            Q += b**2 * (2 * x_i + 2) + a**2 * (-2 * y_i + 3)
            x_i += 1
        else:
            Q += a**2 * (3 - 2 * y_i)
        y_i -= 1
    if tail_points:
        # Loại bỏ các điểm trùng lặp
        tail_pointsSorted = sorted(list(set(tail_points)))
        # Sắp xếp các điểm duy nhất theo góc giảm dần quanh tâm (x, y) cho thứ tự theo chiều kim đồng hồ 
        tail_pointsSorted.sort(key=lambda p: math.atan2(p[1] - y, p[0] - x), reverse=isReverse)
        tail_points = tail_pointsSorted
        return tail_points
    else:
        return []

def drawTailCat(gocQuay=-45):
    color="#4a5a6a"
    rad = gocQuay
    x = -35
    y = -23
    a = 6
    b = 9
    tail_points_l = createTailCat(x, y-1, a, b, True)
    tail_points_r = createTailCat(x, y, a+3, b+3, False)
    # Kết hợp các điểm trên và dưới
    tail_points = tail_points_l + tail_points_r
    if tail_points:
        tail_points = xoayQuanhDiem(tail_points, x, y-b, rad)
        drawDaGiac(tail_points, color)
        t.pencolor(color)
        t.fillcolor(color)
        t.penup()
        t.goto(tail_points[0][0] * 5, tail_points[0][1] * 5)
        t.pendown()
        t.begin_fill()
        for diem in tail_points:
            if diem is not None:
                drawPoint(diem[0], diem[1], color)
        t.goto(tail_points[0][0] * 5, tail_points[0][1] * 5)
        t.end_fill()
    
    hienThiToaDo([
        f"Đuôi - nửa trái (Ellipse): ({tail_points[0][0]}, {tail_points[0][1]}), a = {a}, b = {b}, Góc quay = {rad}",
        f"Đuôi - nửa phải (Ellipse): ({tail_points[1][0]}, {tail_points[1][1]}), a = {a+3}, b = {b+3}, Góc quay = {rad}",
    ])

def drawFaceCat():
    x = -35
    y = 0
    color_mat_trang = "#ffffff"
    color_mat_den = "#2c3440"
    color_mui = "#7e8a99"
    color_mieng = "#7e8a99"
    color_rau = "#bfc9d1"
    # Mắt trái
    t.penup()
    t.goto((x - 3) * 5, (y + 2) * 5)
    t.pendown()
    t.dot(10, color_mat_trang)
    t.penup()
    t.goto((x - 2.5) * 5, (y + 2) * 5)
    t.pendown()
    t.dot(4, color_mat_den)

    # Mắt phải
    t.penup()
    t.goto((x + 3) * 5, (y + 2) * 5)
    t.pendown()
    t.dot(10, color_mat_trang)
    t.penup()
    t.goto((x + 3.5) * 5, (y + 2) * 5)
    t.pendown()
    t.dot(4, color_mat_den)

    # Mũi
    drawTamGiacDeu(x - 1, y - 2, 3, color_mui)

    # Miệng (hình cung)
    t.penup()
    mouth = createTailCat(x, y - 4, 1, 2)
    mouth = xoayQuanhDiem(mouth, x, y - 4, -90)
    for diem in mouth:
        drawPoint(diem[0], diem[1], color_mieng)

    # Râu trái
    size_rau = 3
    t.penup()
    drawLine(x - 3, y - 2, x - 10, y - 2, color_rau, size_rau)
    drawLine(x - 3, y - 1, x - 10, y - 1, color_rau, size_rau)
    drawLine(x - 3, y, x - 10, y, color_rau, size_rau)

    # Râu phải
    t.penup()
    drawLine(x + 3, y - 2, x + 10, y - 2, color_rau, size_rau)
    drawLine(x + 3, y - 1, x + 10, y - 1, color_rau, size_rau)
    drawLine(x + 3, y, x + 10, y, color_rau, size_rau)
    t.penup()

    hienThiToaDo([
        f"Mắt trái (Điểm): ({x - 2.5}, {y + 2}), Kích thước = 4",
        f"Mắt phải (Điểm): ({x + 3.5}, {y + 2}), Kích thước = 4",
        f"Mũi (Tam giác đều): ({x - 1}, {y - 2}), Kích thước = 3",
        f"Miệng (Ellipse): ({x}, {y - 4}), a = 1, b = 2",
        f"Râu trái (Đoạn thẳng): ({x - 3}, {y - 2}), ({x - 10}, {y - 2})",
        f"Râu phải (Đoạn thẳng): ({x + 3}, {y - 2}), ({x + 10}, {y - 2})"
    ])

radCat_change = True
radTailCat_change = True
scaleStar_change = True
scaleStarSB_change = True
radTree_change = True
def animation(offsetX=0, radTree=80, radCat=40, radTailCat=-45, radStar=0, scaleStar=5, scaleStarSB=0, offsetSB=(0, 0), scaleSB1=(1, 1), scaleSB2=(1, 1), lenSB=0):
    global isAnimating, radCat_change, radTailCat_change, scaleStar_change, scaleStarSB_change, radTree_change
    if not isAnimating:
        return
    start = time.time()
    t.clear()
    clearToaDo()
    drawBackground()
    drawMoon()

    drawStar(-radStar, scaleStar)
    drawSaoBang(radStar, scaleStarSB, (offsetSB[0], offsetSB[1]), (scaleSB1[0], scaleSB1[1]), (scaleSB2[0], scaleSB2[1]), lenSB)

    drawCloud(offsetX, 0)

    drawTailCat(radTailCat)
    drawHouse()
    drawTree(radTree)
    drawCat(radCat)
    drawFaceCat()
    screen.update()
    offsetX += 3.5
    
    if offsetX >= 312:
        offsetX = 0
    
    if radTree_change:
        radTree -= 2
        if radTree <= 60:
            radTree_change = False
    else:
        radTree += 2
        if radTree >= 80:
            radTree_change = True

    if radCat_change:
        radCat += 2
        if radCat >= 60:
            radCat_change = False
    else:
        radCat -= 2
        if radCat <= 40:
            radCat_change = True
    
    if radTailCat_change:
        radTailCat -= 2
        if radTailCat <= -70:
            radTailCat_change = False
    else:
        radTailCat += 2
        if radTailCat >= -45:
            radTailCat_change = True

    radStar += 2
    if radStar >= 62:
        radStar = 0

    if scaleStar_change:
        scaleStar -= 0.3
        if scaleStar < 4:
            scaleStar_change = False
    else:
        scaleStar += 0.3
        if scaleStar > 5:
            scaleStar_change = True
    
    if scaleStarSB_change:
        scaleStarSB += 1
        if scaleStarSB >= 5:
            scaleStarSB = 5
            offsetSB = (offsetSB[0] - 1, offsetSB[1] - 1)
            lenSB += 1
            if lenSB >= 18:
                lenSB = 0
                scaleStarSB_change = False
    else:
        scaleStarSB -= 1
        if scaleStarSB <= 0:
            offsetSB = (0, 0)
            scaleStarSB_change = True

    elapsed = (time.time() - start) * 1000
    delay = max(1, int(40 - elapsed))
    t.getscreen().ontimer(lambda: animation(offsetX, radTree, radCat, radTailCat, radStar, scaleStar, scaleStarSB, offsetSB, scaleSB1, scaleSB2, lenSB), delay)

def clearToaDo():
    toaDo.delete("1.0", END)
    toaDo.insert(END, "HIỂN THỊ TỌA ĐỘ")

def hienThiToaDo(hang):
    if hang:
        final_text = "\n".join(hang)
        toaDo.insert(END, '\n' + final_text)
    
def input_table(root):
    INPUT_WIDTH = 500#353
    INPUT_HEIGHT = 287
    frameInput = Frame(root, bd=2, width=INPUT_WIDTH, height=INPUT_HEIGHT, relief=SOLID)
    frameInput.grid(row=0, column=0, padx=8, pady=8, sticky="nsew")
    frameInput.grid_propagate(False) 

    topInput = Frame(frameInput, width=INPUT_WIDTH - 6, height=INPUT_HEIGHT)
    topInput.grid(row=0, column=0, sticky="nsew")
    topInput.pack_propagate(False)
    global toaDo
    toaDo = Text(topInput, wrap=WORD,
             font=('Arial', 11, 'normal'), 
             foreground='blue')
    toaDo.pack(expand=True, fill='both', padx=0, pady=0)

    bottomInput = Frame(frameInput, width=INPUT_WIDTH, height=INPUT_HEIGHT)
    bottomInput.grid(row=1, column=0, sticky="nsew")
    bottomInput.grid_rowconfigure(0, weight=1)
    bottomInput.grid_columnconfigure(0, weight=1)

    notebook = ttk.Notebook(bottomInput)
    notebook.grid(row=0, column=0, sticky="nsew", padx=3, pady=5)

    # Tab 2D
    tab2D = Frame(notebook)
    notebook.add(tab2D, text="PHẦN 2D")
    tab2D.grid_rowconfigure(0, weight=1)
    tab2D.grid_columnconfigure(0, weight=1)

    lf2D = LabelFrame(tab2D, padx=3, pady=5)
    lf2D.grid_columnconfigure(0, weight=1)
    lf2D.grid_columnconfigure(1, weight=1)
    lf2D.grid(row=0, column=0, sticky="nsew", padx=3, pady=5)
    
    # Hàng 1
    frame2DOpt = Frame(lf2D)
    frame2DOpt.grid_columnconfigure(0, weight=1, uniform=1)
    frame2DOpt.grid_columnconfigure(1, weight=1, uniform=1)
    frame2DOpt.grid(row=0, column=0, columnspan=2, sticky="ew", pady=10)
    btnAnimation = Button(frame2DOpt, text='ANIMATION', pady=5,
                   command=None,
                   bg="#FF4444", fg="white", font=("Arial", 9, "bold"))
    btnAnimation.grid(row=0, column=0, sticky="ew", padx=3, pady=5)
    btnPhepBienDoi = Button(frame2DOpt, text='PHÉP BIẾN ĐỔI', pady=5,
                   command=None,
                   bg="#4CAF50", fg="white", font=("Arial", 9, "bold")) 
    btnPhepBienDoi.grid(row=0, column=1, sticky="ew", padx=3, pady=5)

    # Hàng 2
    frameDxy = Frame(lf2D)
    frameDxy.grid_columnconfigure(0, weight=1)
    frameDxy.grid_columnconfigure(1, weight=1)
    frameDxy.grid_columnconfigure(2, weight=1)
    frameDxy.grid_columnconfigure(3, weight=1)
    frameDxy.grid(row=1, column=0, sticky="ew", pady=10) 
    lblDx = Label(frameDxy, text='Dx:', font=("Arial", 10, "bold"))
    lblDx.grid(row=0, column=0, sticky="w", padx=3)
    txtDx = Entry(frameDxy, bd=2, width=6)
    txtDx.insert(0, "0")
    txtDx.grid(row=0, column=1, sticky="ew", padx=3)
    lblDy = Label(frameDxy, text='Dy:', font=("Arial", 10, "bold"))
    lblDy.grid(row=0, column=2, sticky="w", padx=3)
    txtDy = Entry(frameDxy, bd=2, width=6)
    txtDy.insert(0, "0")
    txtDy.grid(row=0, column=3, sticky="ew", padx=3)

    frameSxy = Frame(lf2D)
    frameSxy.grid_columnconfigure(0, weight=1)
    frameSxy.grid_columnconfigure(1, weight=1)
    frameSxy.grid_columnconfigure(2, weight=1)
    frameSxy.grid_columnconfigure(3, weight=1)
    frameSxy.grid(row=1, column=1, sticky="ew", pady=5) 
    lblSx = Label(frameSxy, text='Sx:', font=("Arial", 10, "bold"))
    lblSx.grid(row=0, column=0, sticky="w", padx=3)
    txtSx = Entry(frameSxy, bd=2, width=6)
    txtSx.insert(0, "1")
    txtSx.grid(row=0, column=1, sticky="ew", padx=3)
    lblSy = Label(frameSxy, text='Sy:', font=("Arial", 10, "bold"))
    lblSy.grid(row=0, column=2, sticky="w", padx=3)
    txtSy = Entry(frameSxy, bd=2, width=6)
    txtSy.insert(0, "1")
    txtSy.grid(row=0, column=3, sticky="ew", padx=3)

    frameBtn1 = Frame(lf2D)
    frameBtn1.grid(row=2, column=0, columnspan=2, sticky="ew")
    frameBtn1.grid_columnconfigure(0, weight=1, uniform=1)
    frameBtn1.grid_columnconfigure(1, weight=1, uniform=1)
    btnTinhTien = Button(frameBtn1, text='TỊNH TIẾN', pady=5,
                   command=lambda: tinhTien(float(txtDx.get()), float(txtDy.get())),
                   bg="#FFEA00", fg="black", font=("Arial", 9, "bold"))
    btnTinhTien.grid(row=0, column=0, sticky="ew", padx=3)
    btnBienDoiTiLe = Button(frameBtn1, text='BIẾN ĐỔI TỈ LỆ', pady=5,
                   command=lambda: bienDoiTiLe(float(txtSx.get()), float(txtSy.get())),
                   bg="#FFEA00", fg="black", font=("Arial", 9, "bold"))
    btnBienDoiTiLe.grid(row=0, column=1, sticky="ew", padx=3)

    # Hàng 3
    frameQuay = Frame(lf2D)
    frameQuay.grid_columnconfigure(0, weight=1)
    frameQuay.grid_columnconfigure(1, weight=1)
    frameQuay.grid_columnconfigure(2, weight=1)
    frameQuay.grid_columnconfigure(3, weight=1)
    frameQuay.grid_columnconfigure(4, weight=1)
    frameQuay.grid_columnconfigure(5, weight=1)
    frameQuay.grid_columnconfigure(6, weight=1)
    frameQuay.grid(row=3, column=0, columnspan=2, sticky="nsew", pady=15)
   
    lblP = Label(frameQuay, text='Tọa độ P:', font=("Arial", 10, "bold"))
    lblP.grid(row=0, column=0, sticky="w", padx=3)
    lblPx = Label(frameQuay, text='Px:', font=("Arial", 10, "bold"))
    lblPx.grid(row=0, column=1, sticky="w", padx=3)
    txtPx = Entry(frameQuay, bd=2, width=6)
    txtPx.insert(0, "0")
    txtPx.grid(row=0, column=2, sticky="ew", padx=3)
    lblPy = Label(frameQuay, text='Py:', font=("Arial", 10, "bold"))
    lblPy.grid(row=0, column=3, sticky="w", padx=3)
    txtPy = Entry(frameQuay, bd=2, width=6)
    txtPy.insert(0, "0")
    txtPy.grid(row=0, column=4, sticky="ew", padx=3)
    lblGocQuay = Label(frameQuay, text='Góc:', font=("Arial", 10, "bold"))
    lblGocQuay.grid(row=0, column=5, sticky="w", padx=3)
    txtGocQuay = Entry(frameQuay, bd=2, width=6)
    txtGocQuay.insert(0, "0")
    txtGocQuay.grid(row=0, column=6, sticky="ew", padx=3, pady=10)
    btnQuayQuanhDiem = Button(frameQuay, text='QUAY QUANH ĐIỂM', pady=5,
                   command=lambda: quayQuanhDiem(float(txtPx.get()), float(txtPy.get()), float(txtGocQuay.get())),
                   bg="#B39DDB", fg="black", font=("Arial", 9, "bold")) 
    btnQuayQuanhDiem.grid(row=1, column=0, columnspan=7, sticky="ew", padx=3)

    # Hàng 4
    frameAxy = Frame(lf2D)
    frameAxy.grid_columnconfigure(0, weight=1)
    frameAxy.grid_columnconfigure(1, weight=1)
    frameAxy.grid_columnconfigure(2, weight=1)
    frameAxy.grid_columnconfigure(3, weight=1)
    frameAxy.grid(row=4, column=0, sticky="ew")
    lblAx = Label(frameAxy, text='Ax:', font=("Arial", 10, "bold"))
    lblAx.grid(row=0, column=0, sticky="w", padx=3)
    txtAx = Entry(frameAxy, bd=2, width=6)
    txtAx.insert(0, "0")
    txtAx.grid(row=0, column=1, sticky="ew", padx=3)
    lblAy = Label(frameAxy, text='Ay:', font=("Arial", 10, "bold"))
    lblAy.grid(row=0, column=2, sticky="w", padx=3)
    txtAy = Entry(frameAxy, bd=2, width=6)
    txtAy.insert(0, "0")
    txtAy.grid(row=0, column=3, sticky="ew", padx=3)

    frameBxy = Frame(lf2D)
    frameBxy.grid_columnconfigure(0, weight=1)
    frameBxy.grid_columnconfigure(1, weight=1)
    frameBxy.grid_columnconfigure(2, weight=1)
    frameBxy.grid_columnconfigure(3, weight=1)
    frameBxy.grid(row=4, column=1, sticky="ew", pady=5)
    lblBx = Label(frameBxy, text='Bx:', font=("Arial", 10, "bold"))
    lblBx.grid(row=0, column=0, sticky="w", padx=3)
    txtBx = Entry(frameBxy, bd=2, width=6)
    txtBx.insert(0, "0")
    txtBx.grid(row=0, column=1, sticky="ew", padx=3)
    lblBy = Label(frameBxy, text='By:', font=("Arial", 10, "bold"))
    lblBy.grid(row=0, column=2, sticky="w", padx=3)
    txtBy = Entry(frameBxy, bd=2, width=6)
    txtBy.insert(0, "0")
    txtBy.grid(row=0, column=3, sticky="ew", padx=3)

    frameBtn2 = Frame(lf2D)
    frameBtn2.grid(row=5, column=0, columnspan=2, sticky="ew", pady=5)
    frameBtn2.grid_columnconfigure(0, weight=1, uniform=1)
    frameBtn2.grid_columnconfigure(1, weight=1, uniform=1)
    btnDoiXungDiem = Button(frameBtn2, text='DX ĐIỂM', pady=5,
                   command=lambda: doiXungDiem(int(txtAx.get()), int(txtAy.get())),
                   bg="#81D4FA", fg="black", font=("Arial", 9, "bold"))
    btnDoiXungDiem.grid(row=0, column=0, sticky="ew", padx=3)
    btnDoiXungDoan = Button(frameBtn2, text='DX ĐOẠN', pady=5,
                   command=lambda: doiXungDoanThang(int(txtAx.get()), int(txtAy.get()), int(txtBx.get()), int(txtBy.get())),
                   bg="#81D4FA", fg="black", font=("Arial", 9, "bold")) 
    btnDoiXungDoan.grid(row=0, column=1, sticky="ew", padx=3)

    # Hàng 5
    frameDoiXung2 = Frame(lf2D)
    frameDoiXung2.grid(row=6, column=0, columnspan=2, sticky="ew", pady=5)
    frameDoiXung2.grid_columnconfigure(0, weight=1)
    frameDoiXung2.grid_columnconfigure(1, weight=1)
    frameDoiXung2.grid_columnconfigure(2, weight=1)
    btnDoiXungOx = Button(frameDoiXung2, text='DX qua Ox', pady=5,
                   command=doiXungQuaOX,
                   bg="#FFCCBC", fg="black", font=("Arial", 9, "bold"))
    btnDoiXungOx.grid(row=0, column=0, sticky="ew", padx=3, pady=5)
    btnDoiXungOy = Button(frameDoiXung2, text='DX qua Oy', pady=5,
                   command=doiXungQuaOY,
                   bg="#FFCCBC", fg="black", font=("Arial", 9, "bold")) 
    btnDoiXungOy.grid(row=0, column=1, sticky="ew", padx=3, pady=5)
    btnDoiXungO = Button(frameDoiXung2, text='DX qua O', pady=5,
                   command=doiXungQuaO,
                   bg="#FFCCBC", fg="black", font=("Arial", 9, "bold")) 
    btnDoiXungO.grid(row=0, column=2, sticky="ew", padx=3, pady=5)

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
            btnAnimation.config(text='ANIMATION')
        else:
            isAnimating = True
            btnAnimation.config(text='ANIMATION [DỪNG]')
            datTrangThai(DISABLED)
            t.clear()
            clearToaDo()
            drawOxy()
            animation()

    def trangThaiPhepBienDoi():
        global isAnimating, hcn
        isAnimating = False
        btnAnimation.config(text='ANIMATION')
        datTrangThai(NORMAL)
        t.clear()  
        drawOxy()
        if hcn:
            createHCN()           
            clearToaDo()
            hienThiToaDo([
                "Thông số Hình chữ nhật:",
                f"A({hcn[0]}, {hcn[1]})",
                f"B({hcn[2]}, {hcn[1]})",
                f"C({hcn[2]}, {hcn[3]})",
                f"D({hcn[0]}, {hcn[3]})"
            ])
            # print(hcn)
        else:
            print("Không có hình chữ nhật!")

    btnAnimation.config(command=trangThaiAnimation)
    btnPhepBienDoi.config(command=trangThaiPhepBienDoi)

    # Tab 3D
    tab3D = Frame(notebook)
    notebook.add(tab3D, text="PHẦN 3D")
    tab3D.grid_rowconfigure(0, weight=1)
    tab3D.grid_columnconfigure(0, weight=1)

    lf3D = LabelFrame(tab3D, padx=3, pady=10)
    lf3D.grid(row=0, column=0, sticky="nsew", padx=3, pady=5)
    lf3D.grid_columnconfigure(0, weight=1)
    lf3D.grid_columnconfigure(1, weight=1)

    frameBtn3D = Frame(lf3D)
    frameBtn3D.grid(row=0, column=0, columnspan=2, sticky="ew", pady=5)
    frameBtn3D.grid_columnconfigure(0, weight=1)
    frameBtn3D.grid_columnconfigure(1, weight=1)
    frameBtn3D.grid_columnconfigure(2, weight=1)
    btnHinhHop = Button(frameBtn3D, text='Vẽ Hình Hộp', pady=5,
                   command=lambda: drawHinhHop(0, 0, 0, 30, 30, 30),
                   bg="#B39DDB", fg="black", font=("Arial", 9, "bold"))
    btnHinhHop.grid(row=0, column=0, sticky="ew", padx=3, pady=5)
    btnHinhChop = Button(frameBtn3D, text='Vẽ Hình Chóp', pady=5,
                   command=lambda: drawHinhChop(0, 0, 0, 30, 30, 30),
                   bg="#BBDEFB", fg="black", font=("Arial", 9, "bold")) 
    btnHinhChop.grid(row=0, column=1, sticky="ew", padx=3, pady=5)
    btnHinhCau = Button(frameBtn3D, text='Vẽ Hình Cầu', pady=5,
                   command=lambda: drawHinhCau(0, 0, 0, 30),
                   bg="#FFCCBC", fg="black", font=("Arial", 9, "bold")) 
    btnHinhCau.grid(row=0, column=2, sticky="ew", padx=3, pady=5)

    frameTxt3D = Frame(lf3D)
    frameTxt3D.grid(row=1, column=0, columnspan=2, sticky="ew", pady=5)
    frameTxt3D.grid_columnconfigure(0, weight=1)
    frameTxt3D.grid_columnconfigure(1, weight=1)
    frameTxt3D.grid_columnconfigure(2, weight=1)
    frameHinhHop = Frame(frameTxt3D)
    frameHinhHop.grid(row=0, column=0, sticky="ew", padx=3)
    frameHinhHop.grid_columnconfigure(0, weight=1)
    frameHinhHop.grid_columnconfigure(1, weight=1)
    frameHinhChop = Frame(frameTxt3D)
    frameHinhChop.grid(row=0, column=1, sticky="ew", padx=3)
    frameHinhChop.grid_columnconfigure(0, weight=1)
    frameHinhChop.grid_columnconfigure(1, weight=1)
    frameHinhCau = Frame(frameTxt3D)
    frameHinhCau.grid(row=0, column=2, sticky="new", padx=3)
    frameHinhCau.grid_columnconfigure(0, weight=1)
    frameHinhCau.grid_columnconfigure(1, weight=1)

    lblToaDoA = Label(frameHinhHop, text='TỌA ĐỘ A', font=("Arial", 9, "bold"))
    lblToaDoA.grid(row=0, column=0, columnspan=2, sticky="ew", padx=3)
    lblXA = Label(frameHinhHop, text='x:', font=("Arial", 9, "bold"))
    lblXA.grid(row=1, column=0, sticky="e")
    txtXA = Entry(frameHinhHop, bd=2, width=8)
    txtXA.insert(0, "0")
    txtXA.grid(row=1, column=1, sticky="ew", padx=3, pady=5)
    lblYA = Label(frameHinhHop, text='y:', font=("Arial", 9, "bold"))
    lblYA.grid(row=2, column=0, sticky="e")
    txtYA = Entry(frameHinhHop, bd=2, width=8)
    txtYA.insert(0, "0")
    txtYA.grid(row=2, column=1, sticky="ew", padx=3, pady=5)
    lblZA = Label(frameHinhHop, text='z:', font=("Arial", 9, "bold"))
    lblZA.grid(row=3, column=0, sticky="e")
    txtZA = Entry(frameHinhHop, bd=2, width=8)
    txtZA.insert(0, "0")
    txtZA.grid(row=3, column=1, sticky="ew", padx=3, pady=5)

    lblToaDoA = Label(frameHinhHop, text='KÍCH THƯỚC', font=("Arial", 9, "bold"))
    lblToaDoA.grid(row=4, column=0, columnspan=2, sticky="ew", padx=3)
    lblChieuDai = Label(frameHinhHop, text='Dài:', font=("Arial", 9, "bold"))
    lblChieuDai.grid(row=5, column=0, sticky="e")
    txtChieuDai = Entry(frameHinhHop, bd=2, width=8)
    txtChieuDai.insert(0, "30")
    txtChieuDai.grid(row=5, column=1, sticky="ew", padx=3, pady=5)
    lblChieuRong = Label(frameHinhHop, text='Rộng:', font=("Arial", 9, "bold"))
    lblChieuRong.grid(row=6, column=0, sticky="e")
    txtChieuRong = Entry(frameHinhHop, bd=2, width=8)
    txtChieuRong.insert(0, "30")
    txtChieuRong.grid(row=6, column=1, sticky="ew", padx=3, pady=5)
    lblChieuCao = Label(frameHinhHop, text='Cao:', font=("Arial", 9, "bold"))
    lblChieuCao.grid(row=7, column=0, sticky="e")
    txtChieuCao = Entry(frameHinhHop, bd=2, width=8)
    txtChieuCao.insert(0, "30")
    txtChieuCao.grid(row=7, column=1, sticky="ew", padx=3, pady=5)

    lblToaDoA2 = Label(frameHinhChop, text='TỌA ĐỘ A', font=("Arial", 9, "bold"))
    lblToaDoA2.grid(row=0, column=0, columnspan=2, sticky="ew", padx=3)
    lblXA2 = Label(frameHinhChop, text='x:', font=("Arial", 9, "bold"))
    lblXA2.grid(row=1, column=0, sticky="e")
    txtXA2 = Entry(frameHinhChop, bd=2, width=8)
    txtXA2.insert(0, "0")
    txtXA2.grid(row=1, column=1, sticky="ew", padx=3, pady=5)
    lblYA2 = Label(frameHinhChop, text='y:', font=("Arial", 9, "bold"))
    lblYA2.grid(row=2, column=0, sticky="e")
    txtYA2 = Entry(frameHinhChop, bd=2, width=8)
    txtYA2.insert(0, "0")
    txtYA2.grid(row=2, column=1, sticky="ew", padx=3, pady=5)
    lblZA2 = Label(frameHinhChop, text='z:', font=("Arial", 9, "bold"))
    lblZA2.grid(row=3, column=0, sticky="e")
    txtZA2 = Entry(frameHinhChop, bd=2, width=8)
    txtZA2.insert(0, "0")
    txtZA2.grid(row=3, column=1, sticky="ew", padx=3, pady=5)

    lblKichThuoc2 = Label(frameHinhChop, text='KÍCH THƯỚC', font=("Arial", 9, "bold"))
    lblKichThuoc2.grid(row=4, column=0, columnspan=2, sticky="ew", padx=3)
    lblChieuDai2 = Label(frameHinhChop, text='Dài:', font=("Arial", 9, "bold"))
    lblChieuDai2.grid(row=5, column=0, sticky="e")
    txtChieuDai2 = Entry(frameHinhChop, bd=2, width=8)
    txtChieuDai2.insert(0, "30")
    txtChieuDai2.grid(row=5, column=1, sticky="ew", padx=3, pady=5)
    lblChieuRong2 = Label(frameHinhChop, text='Rộng:', font=("Arial", 9, "bold"))
    lblChieuRong2.grid(row=6, column=0, sticky="e")
    txtChieuRong2 = Entry(frameHinhChop, bd=2, width=8)
    txtChieuRong2.insert(0, "30")
    txtChieuRong2.grid(row=6, column=1, sticky="ew", padx=3, pady=5)
    lblChieuCao2 = Label(frameHinhChop, text='Cao:', font=("Arial", 9, "bold"))
    lblChieuCao2.grid(row=7, column=0, sticky="e")
    txtChieuCao2 = Entry(frameHinhChop, bd=2, width=8)
    txtChieuCao2.insert(0, "30")
    txtChieuCao2.grid(row=7, column=1, sticky="ew", padx=3, pady=5)

    lblToaDoI = Label(frameHinhCau, text='TỌA ĐỘ I', font=("Arial", 9, "bold"))
    lblToaDoI.grid(row=0, column=0, columnspan=2, sticky="ew", padx=3)
    lblXI = Label(frameHinhCau, text='x:', font=("Arial", 9, "bold"))
    lblXI.grid(row=1, column=0, sticky="e")
    txtXI = Entry(frameHinhCau, bd=2, width=8)
    txtXI.insert(0, "0")
    txtXI.grid(row=1, column=1, sticky="ew", padx=3, pady=5)
    lblYI = Label(frameHinhCau, text='y:', font=("Arial", 9, "bold"))
    lblYI.grid(row=2, column=0, sticky="e")
    txtYI = Entry(frameHinhCau, bd=2, width=8)
    txtYI.insert(0, "0")
    txtYI.grid(row=2, column=1, sticky="ew", padx=3, pady=5)
    lblZI = Label(frameHinhCau, text='z:', font=("Arial", 9, "bold"))
    lblZI.grid(row=3, column=0, sticky="e")
    txtZI = Entry(frameHinhCau, bd=2, width=8)
    txtZI.insert(0, "0")
    txtZI.grid(row=3, column=1, sticky="ew", padx=3, pady=5)

    lblKichThuoc3 = Label(frameHinhCau, text='KÍCH THƯỚC', font=("Arial", 9, "bold"))
    lblKichThuoc3.grid(row=4, column=0, columnspan=2, sticky="ew", padx=3)
    lblBanKinh = Label(frameHinhCau, text='R:', font=("Arial", 9, "bold"))
    lblBanKinh.grid(row=5, column=0, sticky="e")
    txtBanKinh = Entry(frameHinhCau, bd=2, width=8)
    txtBanKinh.insert(0, "30")
    txtBanKinh.grid(row=5, column=1, sticky="ew", padx=3, pady=5)

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
    draw.grid(row=0, column=1, padx=8)

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
    global root
    root = Tk()
    root.title('ĐỒ ÁN CUỐI KỲ')
    root.minsize(WINDOW_WIDTH + 410, 785)#750
    draw_table(root)
    input_table(root)
    global hcn
    hcn = [10, 10, 40, 25]
    clearToaDo()
    hienThiToaDo([
        "Thông số Hình chữ nhật:",
        f"A({hcn[0]}, {hcn[1]})",
        f"B({hcn[2]}, {hcn[1]})",
        f"C({hcn[2]}, {hcn[3]})",
        f"D({hcn[0]}, {hcn[3]})"
    ])
    root.mainloop()

if __name__ == "__main__":
    main()