print('[', end="")

def alternatingPrint(length, repeat, start):
    list = []
    bool = True
    if start == 0:
        bool = False
    for num in range(length):
        if bool:
            for _ in range(repeat):
                list.append(1)
                bool = False
        else:
            for _ in range(repeat):
                list.append(0)
                bool = True
    return list

x = 2
print(alternatingPrint(64, 1, 1)[:64], end=',\n')
for _ in range(1,8):
    print(alternatingPrint(64, x, 1)[1:65], end='')
    x *= 2
        
    print(',')