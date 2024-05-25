from pwn import *
from os import *

p=remote('host3.dreamhack.games', 20292)
p.recvuntil(b': ')
p.sendline(b'1')
p.recvuntil(b': ')
p.sendline(b'secret')
p.recvuntil(b'=> ')
es=bytes.fromhex(p.recvline()[:-1].decode())


def enc(pt):
    p.sendline(b'1')
    p.recvuntil(b': ')
    p.sendline(bytes.hex(pt).encode())
    p.recvuntil(b'=> ')
    return bytes.fromhex(p.recvline()[:-1].decode())

def dec(ct):
    p.sendline(b'2')
    p.recvuntil(b': ')
    p.sendline(bytes.hex(ct).encode())
    p.recvuntil(b'=> ')
    msg=p.recvline()[:-1].decode()
    if(msg=="Don't steal my secret!"):
        return True
    else:
        return False

def submit(msg):
    msg = bytes.hex(msg)
    p.sendline(b"3")
    p.sendline(msg.encode())
    p.recvuntil(b"secret: ")

def p_attack(ct):
    zero=[0]*16
    for i in range(16):
        ex1=zero[:]
        for j in range(i):
            ex1[15-j]=ex1[15-j]^(i+1)
        for k in range(256):
            ex1[15-i]=k
            if(dec(bytes(ex1)+ct)):
                break
        zero[15-i]=k^(i+1)
    return bytes(zero)

IV_secret=p_attack(es)
IV=p_attack(enc(bytes(16))[:16])

submit(xor(IV, IV_secret))
p.interactive()


#ncat host3.dreamhack.games 20292