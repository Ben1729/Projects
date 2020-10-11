import numpy as np
import struct
import matplotlib.pyplot as plt

bits = []
i = 0
lastVal = np.float16()
CHANGE = .2

vallarr = []

with open('out.ham', 'ab') as out:
    with open('signal.ham', 'rb') as file:

        for _ in range(10000):
            try:
                vallarr.append(np.frombuffer(file.read(2), dtype=np.float16)[0])
            except:
                break
        print('1')
        for _ in range(10000):
            try:
                thisVal = np.frombuffer(file.read(2), dtype=np.float16)[0]

                if lastVal - thisVal > CHANGE:
                    bits.append(1)
                elif lastVal - thisVal < 0 - CHANGE:
                    bits.append(0)

                i += 1
                if i == 8:
                    i = 0
            except:
                pass

    plt.plot(vallarr, bits)
    plt.ylabel('Value')
    plt.xlabel('Sample')
    plt.show()

    # multiple line plot
plt.plot( 'x', 'y1', data=df, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4)
plt.plot( 'x', 'y2', data=df, marker='', color='olive', linewidth=2)
plt.plot( 'x', 'y3', data=df, marker='', color='olive', linewidth=2, linestyle='dashed', label="toto")
plt.legend()
