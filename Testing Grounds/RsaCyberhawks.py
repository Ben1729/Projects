from Crypto.PublicKey import RSA
from base64 import b64decode
from KeyRecover import KeyRecover

P = 5
Q = 7

rec = KeyRecover(0,0,0,0)
D = rec.get_private_key_from_p_q_e(P,Q,65537)

print hex(D)