num1, num2 = input().split()
if num1 == num2:
    print('too late')
else:
    numList = []
    for x in range(int(num2)):
        numList.append(int(input()))
    for x in range(int(num1)):
        if x+1 not in numList:
            print(x+1)
            exit()