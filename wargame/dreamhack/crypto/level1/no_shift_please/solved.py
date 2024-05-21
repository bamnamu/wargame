from pwn import *

p=remote('host3.dreamhack.games', 24492)

def dec(ct):
    p.sendline(b'2')
    p.sendline(ct.encode())
    p.recvuntil(b'= ')
    return p.recvline()[:-1].decode()

def enc(pt):
    p.sendline(b'1')
    p.sendline(pt.encode())
    p.recvuntil(b'= ')
    return p.recvline()[:-1].decode()

p.recvuntil(b'= ')
e=p.recvline()[:-1].decode()
e1=e[0:8]+"000000000000000000000000"
e2="00000000"+e[8:16]+"0000000000000000"
e3="0000000000000000"+e[16:24]+"00000000"
e4="000000000000000000000000"+e[24:32]
d=dec(e1)[0:8]+dec(e2)[8:16]+dec(e3)[16:24]+dec(e4)[24:32]
print(d)
print(e)
print(enc(d))
p.interactive()

"""
Shift row 함수가 없다면 암호문에서 확산이 일어나지 않고, 이는 평문의 변화가 암호문에 특정 부분에만 나타난다.
특히 shift row는 열이 섞이지 않으므로, 평문에서 각 열의 변화는 다른 열에 영향을 끼치지 않는다.
즉 평문은 4개의 4바이트가 독립적으로 계산되어, 암호문의 4개의 4바이트로 나타난다.
그래서 각 4바이트를 쪼개서 복호화 한다음, 합쳐주면 된다.

"""
