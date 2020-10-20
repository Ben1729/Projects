import numpy as np
import random

#R = np.array(  [[1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
#                [1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0],
#                [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0],
#                [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0]])
                
                
def toArray(string):
    list = []
    for x in string:
        list.append([int(x)])
    return list

def hammingDecode(R, b):
    rb = np.array(toArray(b))

    p = np.matmul(R[:72][:8], rb)
    return ''.join([str(x) for x in [y[0] % 2 for y in p]])

def ri():
    return int(random.randint(0,1))

def test(list):
    if list:
        print(True)
    else: 
        print(False)

if __name__ == "__main__":
    rArr = ['0101001001001010','0100011001000110','0100000101010110','0100100100100000','0100110001001010','0101001101010110','0110100001100100']#,'0111001001101100','0110000101110110','0110100101101010','0011100000000010']#,'01101101010110111','11111110011100001','10110110010100110','01101111101110111','11110001101110101','10110110001000111','10001101001110101','10110111111100111','11000110111110110','11011011011110111','11111111111110111','00110111111000110','11111100111000011','11000111011100110','10110110111100111','10000110100000001','11100000001101100','11111111111101111','00011000111000110','11011010101101011','00001101100000011','01101100101001101','11000010001001000','01101111111001110','10110110111101111','11011011000101011','01111110011101000','01101111111001111','10111110001001000','01101100010001111','11011010101101111','11110000101100110','11011111011101100','00110001110101101','11111001001000011','00011011011001011','10111110001001100','10110111111000110','11111101100000001','10001100010101101','11011111011101110','11100011011101011','00011010011101011','11110001101001101','11000111111000110']
    workingAs = []
    workingBs = [] 
    workingCs = [] 
    workingDs = [] 
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    for e in range(2):
                        for f in range(2):
                            for g in range(2):
                                for h in range(2):
                                    for i in range(2):
                                        for j in range(2):
                                            for k in range(2):
                                                A = [a, b, c, d, e, f, g, h, i, j, k, 1, 0, 0, 0, 0]
                                                works = True
                                                for r in rArr:
                                                    if hammingDecode([A], r[:16]) != '0':
                                                        works = False
                                                if works:
                                                    print(A)
                                                    workingAs.append(A)
    for A in workingAs:
        for a in range(2):
            for b in range(2):
                for c in range(2):
                    for d in range(2):
                        for e in range(2):
                            for f in range(2):
                                for g in range(2):
                                    for h in range(2):
                                        for i in range(2):
                                            for j in range(2):
                                                for k in range(2):
                                                    B = [a, b, c, d, e, f, g, h, i, j, k, 0, 1, 0, 0, 0]
                                                    works = True
                                                    for r in rArr:
                                                        if hammingDecode([A,B], r[:16]) != '00':
                                                            works = False
                                                    if works:
                                                        print(A, B)
                                                        workingBs.append(B)
        for B in workingBs:
            for a in range(2):
                for b in range(2):
                    for c in range(2):
                        for d in range(2):
                            for e in range(2):
                                for f in range(2):
                                    for g in range(2):
                                        for h in range(2):
                                            for i in range(2):
                                                for j in range(2):
                                                    for k in range(2):
                                                        C = [a, b, c, d, e, f, g, h, i, j, k, 0, 0, 1, 0, 0]
                                                        works = True
                                                        for r in rArr:
                                                            if hammingDecode([A,B, C], r[:16]) != '000':
                                                                works = False
                                                        if works:
                                                            print(A, B, C)
                                                            workingCs.append(C)
            for C in workingCs:
                for a in range(2):
                    for b in range(2):
                        for c in range(2):
                            for d in range(2):
                                for e in range(2):
                                    for f in range(2):
                                        for g in range(2):
                                            for h in range(2):
                                                for i in range(2):
                                                    for j in range(2):
                                                        for k in range(2):
                                                            D = [a, b, c, d, e, f, g, h, i, j, k, 0, 0, 0, 1, 0]
                                                            works = True
                                                            for r in rArr:
                                                                if hammingDecode([A, B, C, D], r[:16]) != '0000':
                                                                    works = False
                                                            if works:
                                                                print(A, B, C, D)
                                                                workingDs.append(D)