# read from "Lin64_2"
with open("Lin64_2", "rb") as f:
    #get rid of offset
    offset = 0x5b0
    skip = 15
    f.read(offset) #
    flag = []
    for x in range(39):
        byte = f.read(1)
        flag.append(chr(int.from_bytes(byte, "little")))
        f.read(skip)
    print(flag)
    print("".join(flag))
    
