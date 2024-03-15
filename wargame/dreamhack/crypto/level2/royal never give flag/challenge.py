from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

def gmul(x, y):
    v = 0
    for i in range(8):
        v <<= 1
        if (y >> (7 - i)) & 1:
            v ^= x
        if v & 0x100:
            v ^= 0x11B
    return v

class RNG:
    def __init__(self, key):
        assert type(key) == bytes and len(key) == 16
        self.state = [*key]

        A, B = ord('r'), ord('b')
        self.sbox = [None] # Hint for you :)
        for i in range(1, 0x100):
            for j in range(1, 0x100):
                # Find inverse
                if gmul(i, j) == 1:
                    # This is pretty safe. Check 'Rijndael S-box'
                    self.sbox.append(gmul(A, j) ^ B)
                    break

        for _ in range(100):
            self.update()
    
    def update(self):
        s = self.state
        nxt = s[0] ^ s[3] ^ s[7]
        nxt ^= gmul(s[1], s[2]) # More difficult!
        nxt ^= gmul(s[3], s[8])  # More difficult!!!
        nxt = self.sbox[nxt] # More difficult!!!!!
        self.state = s[1:] + [nxt]
    
    def output(self):
        self.update()
        return self.state[-1]

with open('flag.txt', 'rb') as f:
    flag = f.read()

key = os.urandom(16)
rng = RNG(key)
hint = bytes([rng.output() for _ in range(16)]).hex()
print(f"Hint: {hint}")

cipher = AES.new(key, AES.MODE_ECB) # Who cares ¯\_(ツ)_/¯
print(cipher.encrypt(pad(flag, 16)).hex())




        
        
