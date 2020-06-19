s = input().split()
a = int(s[0])
b = int(s[1])
c = int(s[2])

arTimes = []
dpTimes = []

for x in range(3):
    t = input().split()
    arTimes.append(int(t[0]))
    dpTimes.append(int(t[1]))

curentlyParked = 0
totalCost = 0

for x in range(1,101):
    if x in arTimes:
        curentlyParked += 1
    if x in dpTimes:
        curentlyParked -= 1

    if curentlyParked == 1: 
        totalCost += a
    if curentlyParked == 2: 
        totalCost += (b*2)
    if curentlyParked == 3: 
        totalCost += (c*3)

print(totalCost)