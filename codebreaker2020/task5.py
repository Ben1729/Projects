from Crypto.Cipher import AES


key = 0
iv = 0
ciphertext = open('20200630_161219.log','rb').read(128)
for lat in range(5,90):
    print('{:02d}'.format(lat))
    for lat_1 in range(60):
        for lng in range(180):
            for lng_1 in range(60):

                key = (str(lat).zfill(2)+str(lat_1).zfill(2)) * 4
                iv = "0" + (str(lng).zfill(3)+str(lng_1).zfill(2)) * 3

                cipher = AES.new(bytes(key,'utf-8'), AES.MODE_CBC, bytes(iv,'utf-8'))
                plaintext = cipher.decrypt(ciphertext)

                if b'GNGGA' in plaintext:
                    print(str(lat)+str(lat_1)+" - "+str(lng)+str(lng_1))
                    ciphertext = open('20200630_161219.log','rb').read()
                    plaintext = cipher.decrypt(ciphertext)
                    with open('out.txt','w') as out:
                        out.write(str(plaintext))
                        exit()
                        '{:2}'.format(lat)
                