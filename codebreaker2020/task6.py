import numpy as np
import struct, math
import matplotlib.pyplot as plt

#hamming check matrix
H = np.array(  [[0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0],+
                [0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0]])

#[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]])

#returns the int array for a binary string
def toIndex(string):
    dic = {'0000': -1, '1100': 0, '1010': 1, '0110': 2, '1110': 3, '1001': 4, '0101': 5, '1101': 6, '0011': 7, '1011': 8, '0111': 9, '1111': 10}
    try:
        return dic[string]
    except:
        return -1

def toArray(string):
    list = []
    for x in string:
        list.append([int(x)])
    return list

#returns the +1 index of any error in the vector, else returns zero if no error
def getError(b):
    r = np.array(toArray(b))

    s = np.matmul(H, r)
    #print(''.join([str(x) for x in [y[0] % 2 for y in s]]), b)
    return ''.join([str(x) for x in [y[0] % 2 for y in s]])

#returns the decoded bits from the corrected 7 bit vector
def hammingDecode(b):

    return b[:11]


bits = ''
bitsArray = []
vallarr = []

with open('signal.ham', 'rb') as file:

    #file.read(145250)
    #for x in range(131072):
    #for x in range(512):
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

        if len(bits) == 17:
            bitsArray.append(bits)
            #print(bits)
            #input()
            bits = ''

    words = {}
    with open('out.avi', 'ab') as file:
        byteBuilder = ''
        #print('|data bits  |parity|pad|')
        for vector in bitsArray:
            error = toIndex(getError(vector))
            word = hammingDecode(vector[:17])
            if error != -1:
                
                byteBuilder += word

                #if vector[error] == '1': 
                #    byteBuilder += hammingDecode(vector[:error] + '0' + vector[error:])
                #else: 
                #    byteBuilder += hammingDecode(vector[:error] + '1' + vector[error:])

            else:
                byteBuilder += word
            
            #print('|' + str(word) + '|' + str(vector[11:16]) + ' |' + str(vector[16]) + '  |')
            #words[vector] = words.setdefault(vector, 1) + 1
        #with open('test', 'w') as testOut:
         #   for key in words:
          #      val = words[key]
           #     if val > 1000:
            #        print('\'' + key + '\', ')
             #       testOut.write(str(key) + ' - ' + str(val) + '\n')
        print('almost done')
        while True:
         #   try:
            s = byteBuilder[:16]
            byteBuilder = byteBuilder[16:]
            #print(s, int(s, 2).to_bytes(2, 'big'))
            file.write(int(s, 2).to_bytes(2, 'big'))
        #except:
                