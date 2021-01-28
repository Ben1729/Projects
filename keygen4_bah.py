with open('Lin64_4b.not','rb') as file:

    padding = 0x90e
    skip = 3

    file.read(padding)

    encodedFlag = []
    for _ in range(39):
        encodedFlag.append(int.from_bytes(file.read(1),'little'))
        file.read(skip)

    file.read(27)

    keyMask = []
    for _ in range(8):
        keyMask.append(int.from_bytes(file.read(1),'little'))
    
    bitmask = []
    i = 0
    while i < 256:
        bitmask.append(i)
        i += 1

    n = 0
    i = 0
    while i < 256:
        n = bitmask[i] + n + keyMask[i % 8] & 0xff
        temp = bitmask[i]
        bitmask[i] = bitmask[n]
        bitmask[n] = temp
        i += 1

    n = 0
    t = 0
    new_list = []
    i = 0
    while i < 39:
        t = t + 1 & 0xff
        n = bitmask[t] + n & 0xff
        uVar1 = bitmask[t]
        bitmask[t] = bitmask[n]
        bitmask[n] = uVar1
        new_list.append(bitmask[(bitmask[n] + bitmask[t]) & 0xff])
        i += 1

    s = ''
    for num in range(39):
        s += chr(new_list[num] ^ encodedFlag[num])
    print(s)