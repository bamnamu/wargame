from pwn import *

p=remote('host3.dreamhack.games', 20025)

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

p.recv(1024)
zero='0000000000000000000000000000000000000000000000000000000000000000'
random_value='11'
enc_random_value=enc(random_value)
zr=zero+enc_random_value
print(zr)


#ncat host3.dreamhack.games 10116

#'00000000000000000000000000000000'
#'0000000000000000'
