from pwn import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

p=remote('host3.dreamhack.games', 12783)

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


#ncat host3.dreamhack.games 12783
