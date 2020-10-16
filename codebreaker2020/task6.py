import numpy as np
import struct, math
import matplotlib.pyplot as plt

#hamming check matrix
H = np.array(  [[0, 1, 1, 1, 1, 0, 0],
                [1, 0, 1, 1, 0, 1, 0],
                [1, 1, 0, 1, 0, 0, 1]])

R = np.array(  [[1, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0]])

#returns the +1 index of any error in the vector, else returns zero if no error
def getError(b):
    r =np.array([[int(b[0])],
        [int(b[1])],
        [int(b[2])],
        [int(b[3])],
        [int(b[4])],
        [int(b[5])],
        [int(b[6])]])
    s = np.matmul(H, r)
    return int(''.join([str(x) for x in [s[0][0] % 2, s[1][0] % 2, s[2][0] % 2]]), 2)

#returns the decoded bits from the corrected 7 bit vector
def hammingDecode(b):
    r = np.array([[int(b[0])],
        [int(b[1])],
        [int(b[2])],
        [int(b[3])],
        [int(b[4])],
        [int(b[5])],
        [int(b[6])]])

    p = np.matmul(R, r)
    return ''.join([str(x) for x in [p[0][0] % 2, p[1][0] % 2, p[2][0] % 2, p[3][0] % 2]])


bits = ''
bitsArray = []
vallarr = []

with open('signal.ham', 'rb') as file:

    #file.read(145250)
    while True:
        try:
            #import floats from file
            val = np.frombuffer(file.read(2), dtype=np.float16)[0]

            #append value and change to arrays
            vallarr.append(val)

        except:
            break

    for i in range(len(vallarr)):

        if vallarr[i] >= 0:
            bits += '1'

        elif vallarr[i] < 0:
            bits += '0'

        if len(bits) == 72:
            bitsArray.append(bits)
            #print(bits)
            #input()
            bits = ''
    
    with open('decodedOutput2.h264', 'ab') as file:
        byteBuilder = ''
        for vector in bitsArray:
            vector = vector[::-1]
            error = getError(vector)
            if error != 0:
                errorbit = vector[error-1]
                print(error)
                if errorbit == '1': 
                    byteBuilder += hammingDecode(vector[:error - 1] + '0' + vector[error:])
                else: 
                    byteBuilder += hammingDecode(vector[:error - 1] + '1' + vector[error:])
            else:
                byteBuilder += hammingDecode(vector)
            if len(byteBuilder) == 8:
                file.write(int(byteBuilder, 2).to_bytes(1, 'big'))
                byteBuilder = ''