with open('Lin64_5b.not','rb') as file:

    file.read(0x90e)

    encodedFlag = []
    for _ in range(0x27):
        encodedFlag.append(int.from_bytes(file.read(1),'little'))
        file.read(3)

    file.read(27)

    keyMask = []
    for _ in range(8):
        keyMask.append(int.from_bytes(file.read(1),'little'))
    
    bitmask = []
    for num in range(256):
        bitmask.append(num)

    n = 0
    for num in range(256):
        n = bitmask[num] + n + keyMask[num % 8] & 0xff
        temp = bitmask[num]
        bitmask[num] = bitmask[n]
        bitmask[n] = temp

    n = 0
    t = 0
    new_list = [] * 256
    for iterator in range(0x27):
        t = t + 1 & 0xff
        n = bitmask[t] + n & 0xff
        uVar1 = bitmask[t]
        bitmask[t] = bitmask[n]
        bitmask[n] = uVar1
        new_list.append(bitmask[(bitmask[n] + bitmask[t]) & 0xff])

    print(''.join([chr(new_list[num] ^ encodedFlag[num]) for num in range(39)]))