import struct
import numpy as np
syndromeArray = [['0000000000000000'],['0000000000000001'],['1000000001000000'],['0000000000000010'],['1000000000010000'],['0000000000000100'],['1010000000000000'],
                 ['0000000000100000'],['1001000000000000'],['0000000000001000'],['1000000010000000'],['0100000000000000'],['1000001000000000'],['0000010000000000'],
                 ['1000100000000000'],['0000000100000000'],['1000000000000100'],['0000000000010000'],['1000000000100000'],['0010000000000000'],['1000000000000001'],
                 ['1000000000000000'],['1000000000000010'],['0000000001000000'],['1000010000000000'],['0000001000000000'],['1000000100000000'],['0000100000000000'],
                 ['1000000000001000'],['0001000000000000'],['1100000000000000'],['0000000010000000']]

H = [[1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0],
     [0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0],
     [1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0],
     [0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

def getSyndrome(vector):
    return int(''.join([str(x) for x in [y[0] % 2 for y in np.matmul(H, vector)]]), 2)

with open("signal.ham","rb") as f:
    bitstream = []
    while True:
        try:
            twobytes = f.read(2)
            myfloat = struct.unpack("<e", twobytes)
            if  (myfloat[0] > 0) : 
                bitstream.append( '1' )
            else:
                bitstream.append( '0' )
        except:
            break
        
group=17
correctedBits = ''
with open ("out.avi","wb") as f:
    for x in range (0,len(bitstream),group):
        vector = bitstream[x:x+16]
        
        l = []
        for x in vector:
            l.append([int(x)])
        error = getSyndrome(l)
        correctedWord = int(syndromeArray[error][0],2) ^ int(''.join(vector),2)
        correctedBits += ('{0:016b}'.format(correctedWord))[:11]
    for x in range(0,len(correctedBits), 16):

        f.write(int(correctedBits[x:x+16], 2).to_bytes(2, 'big'))