target = int(input())
dic = dict( [ ('triple', 3), ('double', 2), ('single', 1)] )
for _ in range(3):
    for mult1 in ['triple', 'double', 'single']:
        for a in range(1,21):
            tot = dic[mult1] * a
            if tot == target:
                print(str(mult1) + ' ' + str(a))
                exit()
            for mult2 in ['triple', 'double', 'single']:
                for b in range(1,21):
                    tot2 = dic[mult1] * a + dic[mult2] * b
                    if tot2 == target:
                        print(str(mult1) + ' ' + str(a))
                        print(str(mult2) + ' ' + str(b))
                        exit()
                    for mult3 in ['triple', 'double', 'single']:
                        for c in range(1,21):
                            tot3 = dic[mult1] * a + dic[mult2] * b + dic[mult3] * c
                            if tot3 == target:
                                print(str(mult1) + ' ' + str(a))
                                print(str(mult2) + ' ' + str(b))
                                print(str(mult3) + ' ' + str(c))
                                exit()
print('impossible')