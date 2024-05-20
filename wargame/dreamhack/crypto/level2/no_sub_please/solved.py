from pwn import *
from Crypto.Util.number import *

p=remote('host3.dreamhack.games', 8401)

"""
subbytes 과정이 빠지면 혼돈 속성이 빠지므로

dec(암호문) XOR dec(아무거나) = dec(0) XOR dec(암호문 XOR 아무거나)
dec(암호문) = dec(아무거나) XOR dec(0) XOR dec(암호문 XOR 아무거나)

바이트의 xor 하는 법 : 
xor = lambda a, b: bytes([i ^ j for i, j in zip(a, b)])
p = xor(p1, p2)

"""


p.recvuntil(b'= ')
e=p.recvline()[:-1].decode() #암호문

p.sendline(b'2')
random_value = '00112233445566778899aabbccddeeff'
p.sendline(random_value.encode()) #아무거나
p.recvuntil(b'= ')
h=p.recvline()[:-1].decode() #dec(아무거나)

he=hex(int(random_value, 16)^int(e, 16))[2:] #아무거나 XOR 암호문
he.zfill(len(e))
p.sendline(b'2')
p.sendline(he.encode())
p.recvuntil(b'= ')
he=p.recvline()[:-1].decode() #dec(암호문 XOR 아무거나)

p.sendline(b'2')
p.sendline(b'00000000000000000000000000000000') #0
p.recvuntil(b'= ')
z=p.recvline()[:-1].decode() #dec(0)

ans=hex(int(h, 16)^int(he, 16)^int(z, 16))[2:] # dec(아무거나) XOR dec(0) XOR dec(암호문 XOR 아무거나)
ans.zfill(len(e))
p.sendline(b'1')
p.sendline(ans.encode())
p.interactive()

#DH{Now_you_know_why_substitution_and_confusion_is_important!_Also_welcome_to_galois_field_:))}