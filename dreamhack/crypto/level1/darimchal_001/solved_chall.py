JOKER ="\x40\x53\x06\x03\x43\x52\x54\x3b"
KEY  = "023661dd4"
ans = ""
for i in range(len(JOKER)):
    jo=JOKER[i]
    ans=ans+chr(ord(jo)^ord(KEY[i]))
print(ans)
ans2=""
for i in range(len(ans)):
    print(hex(ord(ans[i])^ord(KEY[i])))
print(ans2)
#pa55uc0_
#pa55uc0
#C:\Users\82104\Desktop\dreamhack\darimchal_001\chall1.exe pa55uc0_