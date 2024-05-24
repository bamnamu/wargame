from pwn import *
from os import *

p=remote('host3.dreamhack.games', 9554)
p.recvuntil(b': ')
p.sendline(b'1')
p.recvuntil(b': ')
p.sendline(b'secret')
p.recvuntil(b'=> ')
s=bytes.fromhex(p.recvline()[:-1].decode())


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

def p_attack(ct):
    zero=[0]*16
    for i in range(16):
        ex1=zero[:]
        for j in range(i):
            ex1[15-j]=ex1[15-j]^(i+1)
        print(f"ex1 : {ex1}")
        for k in range(256):
            ex1[15-i]=k
            if(dec(bytes(ex1)+ct)):
                break
        zero[15-i]=k^(i+1)
        print(zero)
    return
a=b'ahahah'
print(p_attack(enc(a)))
#ncat host3.dreamhack.games 15786