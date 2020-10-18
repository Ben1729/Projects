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


print('[', end="")

x = 2
lst = []
for y in range(11):
    vector = []
    print('[', end="")
    for x in range(11):
        if x == y:
            vector.append(1)
            print(1, end=', ')
        else:
            vector.append(0)
            print(0, end=', ')
    for _ in range(8):
        print(0, end=', ')
    print('],')
