from pwn import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os

io = remote("host3.dreamhack.games", 10116)

def encrypt(pt):
    io.sendline(b"1")
    io.sendlineafter(b"(hex): ", bytes.hex(pt).encode())
    return bytes.fromhex(io.recvline().decode())

def decrypt(pt):
    io.sendline(b"2")
    io.sendlineafter(b"(hex): ", bytes.hex(pt).encode())
    return bytes.fromhex(io.recvline().decode())

def getflag():
    io.sendline(b"3")
    io.recvuntil(b"flag = ")
    return bytes.fromhex(io.recvline().decode())

zeroblock = bytes(16)

enc = encrypt(os.urandom(16))
print(bytes.hex(zeroblock*2+enc))
dec = decrypt(zeroblock * 2 + enc)
key = xor(dec[:16], dec[16:32])

enc_flag = getflag()

flag = AES.new(key, AES.MODE_CBC, key).decrypt(enc_flag)
flag = unpad(flag, 16).decode()

print(flag)