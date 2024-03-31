from Crypto.Util.number import getPrime
from Crypto.Random.random import randint
import os

BITS = 2048

n = randint(2,50)
N = 1
for i in range(n):
    bit = BITS//n
    if i < BITS%n:
        bit += 1
    N *= getPrime(bit)

m = randint(1,N-1)
e = 65537
c = pow(m,e,N)
print(f"{n = }")
print(f"{N = }")
print(f"{c = }")
m_inp = int(input("m = "))

if m_inp == m:
    print("Correct!")
    flag = open("flag.txt","r").read().strip()
    print(flag)
else:
    print("Wrong!")