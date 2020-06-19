cases = int(input())
for x in range(cases):
    b, p = input().split()
    abpm = 60/(float(p) / int(b))
    minAbpm = (float(b)-1) / float(p)*60
    maxAbpm = 60 / (float(p) / (int(b)+1))
    s = str(minAbpm) + " " + str(abpm) + " " + str(maxAbpm)
    print("{:0.4f} {:0.4f} {:0.4f}".format(minAbpm, abpm, maxAbpm))
