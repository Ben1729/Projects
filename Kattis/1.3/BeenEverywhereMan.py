cases = int(input())

for x in range(cases):
    i = 0
    list = ["a"]
    dests = int(input())
    for y in range(dests):
        dest = str(input())
        if dest not in list:
            list.append(dest)
            i += 1
            
    print(i)