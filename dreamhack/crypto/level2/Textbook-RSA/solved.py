from pwn import *

p=remote('host3.dreamhack.games', 20607)
p.sendline(b'3')
p.recvuntil(b'N: ')
n=int(p.recvline()[0:-1].decode('utf-8'))
p.recvuntil(b'e: ')
e=int(p.recvline()[0:-1].decode('utf-8'))
p.recvuntil(b'FLAG: ')
cflag=int(p.recvline()[0:-1].decode('utf-8'))
two=(pow(2, e)%n)
mid=(two*cflag)%n
p.sendline(b'2')
p.sendline(hex(mid)[2:])
p.recvuntil(':')
ans=int(p.recvline()[0:-1].decode('utf-8'))
if(ans%2==0):
    ans=ans//2
else:
    ans=(ans+n)//2
ans=hex(ans)
ansstr=""
for i in range(1, len(ans)//2):
    ansstr=ansstr+chr(int("0x"+ans[2*i:2*i+2], 16))
print(ansstr)
