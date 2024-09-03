import numpy as np

# Khởi tạo ma trận
a = np.array([[2, 8, 3], [1, 6, 4], [7, 0, 5]])
A = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
b = np.array([[2, 8, 3], [1, 6, 4], [7, 0, 5]])
I, J, I1, J1, g, h = 0, 0, 0, 0, 0, 0

def xuly():
    global g
    while not ketthuc():
        g += 1
        xetchon()
        print("h =", h)
        print("Trạng thái hiện tại:")
        print(a)
        input("Nhấn Enter để tiếp tục...")

def ketthuc():
    return np.array_equal(a, A)

def tinh():
    bac = 0
    for i in range(3):
        for j in range(3):
            if tim(b[i, j]):
                bac += abs(I1 - i) + abs(J1 - j)
    return bac

def tim(x):
    global I1, J1
    for i in range(3):
        for j in range(3):
            if A[i, j] == x and x != 0:
                I1, J1 = i, j
                return True
    return False

def timdinhtrong():
    global I, J
    for i in range(3):
        for j in range(3):
            if a[i, j] == 0:
                I, J = i, j
                return

def swap(x, y):
    return y, x

def xetchon():
    global h
    f = 100
    timdinhtrong()
    for j in range(3):
        for l in range(3):
            if abs(I - j) + abs(J - l) == 1:
                b[j, l], b[I, J] = swap(b[j, l], b[I, J])
                h = tinh()
                if h < f:
                    f = h
                    chep2()
                b[j, l], b[I, J] = swap(b[j, l], b[I, J])
    chep1()
    h = f

def chep1():
    global b, a
    b = np.copy(a)

def chep2():
    global a, b
    a = np.copy(b)

# Chạy chương trình
print("Dữ liệu đầu vào:")
print(a)
print("Ma trận mục tiêu:")
print(A)
xuly()
print(f"Số bước cần thiết: {g}")
