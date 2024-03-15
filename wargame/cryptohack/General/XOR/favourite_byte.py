from Crypto.Util.number import *

c="73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
c=bytes.fromhex(c)
print(c)
for i in range(256):
    ans=""
    for j in c:
        ans=ans+chr(j^i)
    if "crypto" in ans:
        print(ans)