import numpy as np
import random

H=np.array([[0,1,0,1,0,1,1,1,0,1,1,1,0,0,0,0],
            [1,1,1,0,0,0,0,1,1,1,1,0,1,0,0,0],
            [1,1,0,0,1,1,1,0,1,1,0,0,0,1,0,0],
            [1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,0],
            [0,1,1,1,1,0,1,1,1,0,0,0,0,0,0,1]])
                
                
def toArray(string):
    list = []
    for x in string:
        list.append([int(x)])
    return list

def hammingDecode(b):
    rb = np.array(toArray(b))

    p = np.matmul(H, rb)
    return ''.join([str(x) for x in [y[0] % 2 for y in p]])

def ri():
    return int(random.randint(0,1))

def test(list):
    if list:
        print(True)
    else: 
        print(False)

if __name__ == "__main__":
    rArr = ['0000000000000000']
    for r in rArr:
        for x in range(16):
            s = r[:x] + '1' + r[x:]
            print('\''+hammingDecode(s[:16])+'\'', ':',str(x)+',')
    