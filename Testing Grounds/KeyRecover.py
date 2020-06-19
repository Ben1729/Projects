import hashlib
from Crypto.Util.number import long_to_bytes

class KeyRecover:

    def __init__(self,key1,key2,pub,priv):

        self.key1 = key1
        self.key2 = key2
        self.pub = pub
        self.priv = priv
        self.e = 65537

    def recover(self,target):

        print "\nRecovering Modulus: \t"+target

        #Target public key
        T = int(target,16)

        #Cut off the first half
        mid = len(target) // 2
        part1 = target[:mid]

        print "First Half: \t\t\t"+str(part1)

        for i in range(1000):

            #Get the encrypted part
            encrypted = int(part1, 16) ^ (self.key2+i)

            #Decrypt it with the private key
            decrypted = pow(encrypted,self.priv,self.pub)

            key1 = self.key1

            #Limit so we don't sit here all day
            for limit in range(100):

                for j in range(10):

                    #Try to get back the original prime P
                    prime = decrypted ^ key1

                    #If it is evenly divisible from T then we found it
                    if T%prime == 0:

                        print "Recovered P: \t\t\t"+str(prime)
                        print "Recovered Q: \t\t\t"+str(T//prime)
                        return prime,T//prime,self.get_private_key_from_p_q_e(prime,T//prime,self.e)

                    #Else increment key1
                    key1+=1

                #After 10 tries, hash key1 and keep trying
                key1 = int(hashlib.sha256(long_to_bytes(key1)).hexdigest(), 16)

        return None,None,None


    def get_private_key_from_p_q_e(self, p, q, e):

        d = 0

        #Calculate phi_n
        phi_n = (p-1) * (q-1)

        #d is the modular inverse of e and phi_n
        d = self.modinv(e,phi_n)

        return d

    def modinv(self,a,n):

        t = 0
        r = n
        nt = 1
        nr = a

        while nr != 0:
            q = r//nr
            t,nt = nt,t-q*nt
            r,nr = nr,r-q*nr

        if r > 1:
            return 0
        if t < 0:
            t += n

        return t