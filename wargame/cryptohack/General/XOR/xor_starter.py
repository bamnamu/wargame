
key=13
string="label"
ans=""
for i in range(len(string)):
    ans=ans+chr(ord(string[i])^key)
print("crypto{"+ans+"}")