import struct
import numpy as np
syndromeArray = [['1000000000011010'],['0100000000001011'],['0010000000001101'],
                 ['0001000000011100'],['0000100000011111'],['0000010000010011'],
                 ['0000001000011001'],['0000000100001110'],['0000000010010110'],
                 ['0000000001010101'],['0000000000100111']]

H = [[1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0],
     [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0],
     [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

def getSyndrome(vector):
    return int(''.join([str(x) for x in [y[0] % 2 for y in np.matmul(H, vector)]]), 2)

with open(r"C:\Users\maqui\Desktop\signal.ham","rb") as f:
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
with open ("last_try.avi","wb") as f:
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

