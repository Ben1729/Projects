cases = int(input())

measurments = []
n = 0
s = 0

for x in range(cases):
    stuff = input().split()
    n += int(stuff[0])
    s += int(stuff[1])

s = int(s) / 60.0
average = s / int(n)
if average > 1:
    print(average)
else:
    print("measurement error")