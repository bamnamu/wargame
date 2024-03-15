from pwn import *

p = remote('host3.dreamhack.games', 8238)
p.sendline(b'2')
p.sendline(b'01FE01FE01FE01FE')
p.recvuntil(b'enc_flag(hex)> ')
enc_flag=p.recvline()[0:-1]
p.sendline(b'1')
p.sendline(b'FE01FE01FE01FE01')
p.sendline(enc_flag)
p.recvuntil(b'enc(hex)> ')
flag=p.recvline()[0:-1].decode('utf-8')
ans=""
for i in range(len(flag)//2):
    num=int(flag[2*i:2*i+2], 16)
    if(num==8):
        break
    ans=ans+chr(num)
print(ans)
