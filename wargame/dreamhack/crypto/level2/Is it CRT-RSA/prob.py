from Crypto.Util.number import getPrime, bytes_to_long
import os

with open("flag.txt","rb") as f:
    flag = f.read()
L = len(flag)

p1,q1 = getPrime(512),getPrime(512)
p2,q2 = getPrime(512),getPrime(512)
n1,n2 = p1*q1,p2*q2
dp = p2-p1
dq = q2-q1
e = 65537

m1 = flag[:L//2]+os.urandom(8)
m2 = flag[L//2:]+os.urandom(8)
c1 = pow(bytes_to_long(m1),e,n1)
c2 = pow(bytes_to_long(m2),e,n2)

print(f"{n1=}")
print(f"{c1=}")
print("")
print(f"{n2=}")
print(f"{c2=}")
print("")
print(f"{dp=}")
print(f"{dq=}")