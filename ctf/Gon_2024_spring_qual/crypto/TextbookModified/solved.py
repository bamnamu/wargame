from pwn import *
from Crypto.Util.number import long_to_bytes
import math
import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pollards_rho(n):
    if n==1:
        return 1
    if n % 2 == 0:
        return 2
    x = randint(2, n - 1)
    y = x
    c = randint(1, n - 1)
    d = 1
    f = lambda x: (x*x + c) % n
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x-y), n)
        if d == n:
            return pollards_rho(n)
    return d

def is_prime(n, k=5):  # Miller-Rabin 테스트를 k번 반복 O(k*log(n)^3)
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # n-1 = 2^r * d 형태로 표현
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # 테스트 반복
    for _ in range(k):
        a = randint(2, n - 2)
        x = pow(a, d, n)  # a^d % n
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

p=remote('158.247.225.252',  13370)
p.recvuntil(b'n = ')
n=int(p.recvline()[0:-1].decode('utf-8'))
p.recvuntil(b'N = ')
N=int(p.recvline()[0:-1].decode('utf-8'))
p.recvuntil(b'c = ')
c=int(p.recvline()[0:-1].decode('utf-8'))
sb=[]
pb=(2048//n)+2
e=65537
i=1
print(n)
while(N>pow(2, pb)):
    factors = pollards_rho(N)
    if(is_prime(factors)):
        print(f"{i}번째 N의 소인수: {factors}")
        N=N//factors
        sb.append(factors)
        i=i+1
print(f"{n}번째 N의 소인수: {N}")
sb.append(N)
phi=1
for i in range(len(sb)):
    phi=phi*(sb[i]-1)
d=pow(e, -1, phi)
m=pow(c, d, N)
print(m)
p.sendline(long_to_bytes(m))
p.interactive()