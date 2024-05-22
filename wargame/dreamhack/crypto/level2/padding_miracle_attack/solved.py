from pwn import *
from os import *

p=remote('host3.dreamhack.games', 17573)
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



#ncat host3.dreamhack.games 17573