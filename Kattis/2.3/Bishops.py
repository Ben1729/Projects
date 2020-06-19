while True:
    try:
        num = int(input())
        if num <= 2:
            print(num)
        else:
            print(2*num-2)
    except:
        exit()
    