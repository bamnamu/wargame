c="0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
c=bytes.fromhex(c)
check=b"crypto{"

key=""

for i in range(len(check)):
    key=key+chr(c[i]^check[i])

#key=myXORke
    
key=key+"y"
ans=""
for i in range(len(c)):
    ans=ans+chr(c[i]^ord(key[i%8]))

print(ans)
