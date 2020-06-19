cases = int(raw_input())
for x in range(cases):
    r, e, c = raw_input().split()
    r = int(r)
    e = int(e)
    c = int(c)
    if (e-c) > r:
        print "advertise"
    elif (e-c) < r:
        print "do not advertise"
    else:
        print "does not matter"

