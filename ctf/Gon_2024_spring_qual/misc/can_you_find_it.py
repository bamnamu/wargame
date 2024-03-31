a=input()
decrypt=0
for i in range(26):
    for j in range(len(a)):
        if(a[j]==3):
            a[j]
        decrypt=ord(a[j])-97
        if(decrypt>=0 and decrypt<=25):
            decrypt=(decrypt+i)%26
            decrypt=decrypt+97
        else:
            decrypt=decrypt+97
        print(chr(decrypt), end="")
    print("")
#qebaslc
#recbsmd
#sedcsne
#hesrsct
#iets