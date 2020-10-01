cap, stations = input().split()
cap = int(cap)
trainPassengers = 0
for x in range(int(stations)):
    left, entered, leftover = input().split()
    trainPassengers -= int(left)
    if trainPassengers < 0:
        print('impossible')
        exit()
    trainPassengers += int(entered)
    if trainPassengers > cap:
        print('impossible')
        exit()
    if trainPassengers < int(leftover) and trainPassengers != cap:
        print('impossible')
        exit()
if trainPassengers != 0:
    print('impossible')
    exit()
else:
    print('possible')