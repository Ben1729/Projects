import numpy as np
import struct, math
import matplotlib.pyplot as plt


SMOOTHING = 10

bits = []
i = 0
lastVal = 0

vallarr = []
changeArr = []
lastBit = 0

smoothingStack = [0]*SMOOTHING

def Average(lst): 
    return sum(lst) / len(lst)

with open('signal.ham', 'rb') as file:

    for _ in range(1000000):
        try:
            #import floats from file
            val = np.frombuffer(file.read(2), dtype=np.float16)[0]

            #calculate change since last sample
            change = (val - lastVal)
            lastVal = val

            #append value and change to arrays
            vallarr.append(val)
            changeArr.append(change)

        except:
            pass

    for i in range(len(vallarr)):
        try:

            #if change is positive and greater than .5, bit must be a 1
            average = Average(smoothingStack)

            if vallarr[i] - average > 0:
                bits.append(1)
                lastBit = 1

            #if change is negitive and less than -.5, bit must be a 0
            elif vallarr[i] < 0:
                bits.append(-1)
                lastBit = -1

            #otherwise use last bit
            else:
                bits.append(lastBit)

            smoothingStack.append(math.ceil(vallarr[i], 10))
            smoothingStack.popleft()

        except:
            pass

plt.plot(vallarr, color='blue', linewidth=1)
#plt.plot(changeArr, color='orange', linewidth=1)
plt.plot(bits, color='red', linewidth=1)
plt.show()