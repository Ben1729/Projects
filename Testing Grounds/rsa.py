from Crypto.PublicKey import RSA
key = RSA.importKey(open('pubkey.pem').read())
print(key.n, key.e)