x1, y1, x2, y2, p = input().split()

dist = (abs(int(x1) - int(x2)) ** (1 / int(p)) + abs(int(y1) - int(y2)) ** (1 / int(p)) ** (1 / int(p))) ** (1 / int(p))
print(dist)