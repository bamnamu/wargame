import base64

with open("target.txt", 'r') as f:
    target=f.read()[:-3]
print(target)
mid=""
for i in range(len(target)):
    if(ord(target[i])<=90):
        ft=bin(ord(target[i])-65)[2:]
        while(len(ft)!=5):
            ft="0"+ft
        mid=mid+ft
    else:
        ft=bin(ord(target[i])-71)[2:]
        while(len(ft)!=5):
            ft="0"+ft
        mid=mid+ft
ans=""
for i in range(len(mid)//8):
    key=int("0b"+mid[8*i: 8*i+8], 2)
    print(bin(key), key)
    ans=ans+chr(key)
print(ans)