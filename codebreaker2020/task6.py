import numpy as np
import struct, math
import matplotlib.pyplot as plt

H=np.array([[0,1,0,1,0,1,1,1,0,1,1,1,0,0,0,0,0],
            [1,1,1,0,0,0,0,1,1,1,1,0,1,0,0,0,0],
            [1,1,0,0,1,1,1,0,1,1,0,0,0,1,0,0,0],
            [1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,0,0],
            [0,1,1,1,1,0,1,1,1,0,0,0,0,0,0,1,0]])

#returns the int array for a binary string
def toIndex(string):
    try:
        dic = {'00000': -1, '01110': 0, '11111': 1, '01011': 2, '10011': 3, '00111': 4, '10110': 5,
        '10101': 6, '11001': 7, '01101': 8, '11100': 9, '11010': 10, '10000': 11, '01000': 12,
        '00100': 13, '00010': 14, '00001': 15}
        #print(string)
        #input()
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

def thing(bitsArray):
    
    words = {}
    for vector in bitsArray:
        words[vector] = int(words.setdefault(vector, 0)) + 1
    for key in words:
        val = words[key]
        if val > 20:
            if  key[:11] == '10000000000':
                print(key, words[key])
            if  key[:11] == '01000000000':
                print(key, words[key])
            if  key[:11] == '00100000000':
                print(key, words[key])
            if  key[:11] == '00010000000':
                print(key, words[key])
            if  key[:11] == '00001000000':
                print(key, words[key])
            if  key[:11] == '00000100000':
                print(key, words[key])
            if  key[:11] == '00000010000':
                print(key, words[key])
            if  key[:11] == '00000001000':
                print(key, words[key])
            if  key[:11] == '00000000100':
                print(key, words[key])
            if  key[:11] == '00000000010':
                print(key, words[key])
            if  key[:11] == '00000000001':
               print(key, words[key])
    
    
bits = ''
bitsArray = []
vallarr = []


with open('signal.ham', 'rb') as file:

    #file.read(145250)
    #for x in range(131072):
    #for x in range(2048):
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
    #thing(bitsArray)
    
    with open('out.avi', 'ab') as file:
        byteBuilder = ''
        #print('|data bits  |parity|pad|')
        for vector in bitsArray:
            #print(vector)
            error = toIndex(getError(vector))
            word = hammingDecode(vector[:17])
            if error != -1:
                
                #yteBuilder += word

                if vector[error] == '1': 
                    byteBuilder += hammingDecode(vector[:error] + '0' + vector[error:])
                else: 
                    byteBuilder += hammingDecode(vector[:error] + '1' + vector[error:])

            else:
                byteBuilder += word
            
            #print('|' + str(word) + '|' + str(vector[11:16]) + ' |' + str(vector[16]) + '  |')
            #words[vector] = words.setdefault(vector, 1) + 1
        print('almost done')
        while True:
         #   try:
            s = byteBuilder[:16]
            byteBuilder = byteBuilder[16:]
            #print(int(s, 2).to_bytes(2, 'big'))
            file.write(int(s, 2).to_bytes(2, 'big'))
        #except:
                