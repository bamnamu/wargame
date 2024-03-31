from pwn import *
import math
import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pollards_rho(n):
    if n % 2 == 0:
        return 2
    x = random.randint(1, n-1)
    y = x
    c = random.randint(1, n-1)
    d = 1
    f = lambda x: (x*x + c) % n
    
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x-y), n)
        
    return d

p=remote('158.247.225.252',  13370)
p.recvuntil(b'N = ')
n=int(p.recvline()[0:-1].decode('utf-8'))
factor = pollards_rho(n)
print(f"A factor of {n} is {factor}")
p.interactive()