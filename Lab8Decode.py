with open('Lin64_3b.not','rb') as file:

    #Read past buffer
    file.read(0x000005c1)
    
    #Read in our encoded flag
    encodedFlag = []
    for _ in range(39):
        encodedFlag.append(file.read(1))
        file.read(3)

    #Skip 6 bytes
    file.read(6)

    #Get our xor key
    key = int.from_bytes(file.read(1), 'big')

    #Xor each byte by the key
    print(''.join([chr(int.from_bytes(byte, 'big') ^ key) for byte in encodedFlag]))