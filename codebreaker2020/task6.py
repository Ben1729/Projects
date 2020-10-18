import numpy as np
import struct, math
import matplotlib.pyplot as plt

#hamming check matrix
H = np.array(  [[1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                [1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]])
                
R = np.array(  [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]])

#returns the int array for a binary string
def toArray(string):
    list = []
    for x in string:
        list.append([int(x)])
    return list

#returns the +1 index of any error in the vector, else returns zero if no error
def getError(b):
    r = np.array(toArray(b))

    s = np.matmul(H[:17][:11], r)
    return int(''.join([str(x) for x in [y[0] % 2 for y in s]]), 2)

#returns the decoded bits from the corrected 7 bit vector
def hammingDecode(b):
    r = np.array(toArray(b))

    p = np.matmul(R[:17][:11], r)
    return ''.join([str(x) for x in [y[0] % 2 for y in p]])


bits = ''
bitsArray = []
vallarr = []

with open('signal.ham', 'rb') as file:

    #file.read(145250)
    for x in range(2000):
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

        if len(bits) == 17:
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
                
                byteBuilder += hammingDecode(vector)
                #if vector[error-1] == '1': 
                #    byteBuilder += hammingDecode(vector[:error - 1] + '0' + vector[error:])
                #else: 
                #    byteBuilder += hammingDecode(vector[:error - 1] + '1' + vector[error:])
            else:
                byteBuilder += hammingDecode(vector)
            if len(byteBuilder) >= 16:
                s = byteBuilder[:16]
                byteBuilder = byteBuilder[16:]
                file.write(int(s, 2).to_bytes(2, 'little'))