cases = int(raw_input())

for x in range(cases):
    num = int(raw_input())
    if num % 2 == 0:
        print str(num) + " is even"
    else:
        print str(num) + " is odd"