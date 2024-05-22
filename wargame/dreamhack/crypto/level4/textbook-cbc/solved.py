from pwn import *
from Crypto.Cipher import AES
<<<<<<< HEAD
from Crypto.Util.Padding import unpad

p=remote('host3.dreamhack.games', 14845)
=======
from Crypto.Util.Padding import pad, unpad
import os

p=remote('host3.dreamhack.games', 15078)

p.recv(1024)
>>>>>>> d17e4a9069e5da0b2625e88bd87470cf8a257ccd

def enc(pt):
    p.sendline(b'1')
    p.recvuntil(b': ')
    p.sendline(pt.encode())
    return p.recvline()[:-1].decode()

def dec(ct):
    p.sendline(b'2')
    p.recvuntil(b': ')
    p.sendline(ct.encode())
    return p.recvline()[:-1].decode()

<<<<<<< HEAD
def hexxor(a, b):
    return hex(int(a, 16)^int(b, 16))[2:]

p.recv(1024)
zero='0000000000000000000000000000000000000000000000000000000000000000'
random_value='11111111111111111111111111111111'
enc_random_value=enc(random_value)
zr=zero+enc_random_value
dec_zr=dec(zr)
IV=hexxor(dec_zr[0:32], dec_zr[32:64])
IV=bytes.fromhex(IV)
p.sendline(b'3')
p.recvuntil(b'= ')
enc_flag=bytes.fromhex(p.recvline()[:-1].decode())
flag=AES.new(IV, AES.MODE_CBC, IV).decrypt(enc_flag)
print(flag)
flag=unpad(flag, 16).decode()
print(flag)


#ncat host3.dreamhack.games 10116
=======
def xxor(a, b):
    return hex(int(a, 16)^int(b, 16))[2:]

zero='00000000000000000000000000000000' 
rand=enc('11111111111111111111111111111111')
zeroIV=zero+rand
d_zero_xor_IV=dec(zeroIV)[0:16]
d_zero=dec(zeroIV)[16:32]
IV=xxor(d_zero, d_zero_xor_IV)
p.sendline(b'3')
p.recvuntil(b'= ')
enc_flag=p.recvline()[:-1]
IV=IV.encode()
flag=AES.new(IV, AES.MODE_CBC, IV).decrypt(enc_flag)
flag=unpad(flag, 16).decode()
print(flag)
#ncat host3.dreamhack.games 15078
>>>>>>> d17e4a9069e5da0b2625e88bd87470cf8a257ccd
