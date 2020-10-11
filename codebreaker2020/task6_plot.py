import numpy as np
import matplotlib.pyplot as plt

vallarr = []
with open('signal.ham', 'rb') as file:
    while True:
        try:
            vallarr.append(np.frombuffer(file.read(2), dtype=np.float16)[0])
        except:
            break
    plt.plot(vallarr)
    plt.ylabel('Value')
    plt.xlabel('Sample')
    plt.show()
        