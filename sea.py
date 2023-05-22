import math
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
menu = math.pow((x1 - x2), 2)
btn = math.pow((y1 - y2), 2)
square = math.sqrt((btn + menu))
print(square)
