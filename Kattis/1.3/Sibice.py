import math
count, length, width = raw_input().split()
length = int(length)
width = int(width)
maxMatchSize = math.sqrt((length * length)+(width * width))
count = int(count)

for x in range(count):
    if int(raw_input()) > int(maxMatchSize):
        print "NE"
    else: print "DA"