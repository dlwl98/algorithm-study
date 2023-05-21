def calculation(eq1, eq2):
    x1, y1, c1 = eq1
    x2, y2, c2 = eq2
    
    x = (y1*c2-c1*y2)/(x1*y2-y1*x2)
    y = (c1*x2-x1*c2)/(x1*y2-y1*x2)
    return[x, y]

def getLine(x1, y1, x2, y2):
    c = (x1 - x2) * y1 + (y2 - y1) * x1
    a = y1 - y2
    b = x2 - x1
    return [a, b, c]

def check(x1, y1, x2, y2, a, b):
    x3 = min(x1, x2)
    x4 = max(x1, x2)
    y3 = min(y1, y2)
    y4 = max(y1, y2)
    if x3 <= a <= x4 and y3 <= b <= y4:
        return True
    return False

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
eq1 = getLine(x1, y1, x2, y2)
eq2 = getLine(x3, y3, x4, y4)

if eq1[1] == 0 and eq2[1] == 0:
    if eq1[2]/eq1[0] == eq2[2]/eq2[0]:
        if check(x1, y1, x2, y2, x3, y3) or check(x1, y1, x2, y2, x4, y4):
            print(1)
        else:
            print(0)
    else:
        print(0)

elif eq1[1] == 0:
    if check(x3, y3, x4, y4, -eq1[2]/eq1[0], y3):
        print(1)
    else:
        print(0)

elif eq2[1] == 0:
    if check(x1, y1, x2, y2, -eq2[2]/eq2[0], y1):
        print(1)
    else:
        print(0)

elif eq1[0]/eq1[1] == eq2[0]/eq2[1]:
    if eq1[2]/eq1[1] != eq2[2]/eq2[1]:
        print(0)
    else:
        if check(x1, y1, x2, y2, x3, y3) or check(x1, y1, x2, y2, x4, y4):
            print(1)
        else:
            print(0)
else:
    a, b = calculation(eq1, eq2)
    if check(x1, y1, x2, y2, a, b) or check(x3, y3, x4, y4, a, b):
        print(1)
    else:
        print(0)
