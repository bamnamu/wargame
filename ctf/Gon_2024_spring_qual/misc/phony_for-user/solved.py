import base64
import hashlib

def bitnot(c):
    c=bin(int(c, 16))[2:]
    d=""
    for t in range(len(c)):
        if(c[t]=='0'):
            d=d+'1'
        else:
            d=d+'0'
    d='0b'+d
    c=hex(int(d, 2))[2:]
    return c


st=0
for fn in range(1, 10000):
    format_fn=f"{fn:04}"
    f=open(rf'C:\Users\82104\Desktop\security\ctf\Gon_2024_spring_qual\misc\phony_for-user\for_user\{format_fn}.eml', 'r')
    i=1
    while True:
        line = f.readline()
        if not line: break
        if(i==11):
            bh=line[4:-2]
        elif(i==41):
            check=line[0:-1]
        i=i+1
    check=base64.b64decode(line)
    hash_obj = hashlib.sha256(check)
    body_hash = hash_obj.digest()
    encoded_body_hash = base64.b64encode(body_hash).decode('utf-8')
    if encoded_body_hash == bh:
        print(f"{fn}번째, 무결성 검증 성공: 이메일 본문이 변경되지 않았습니다.")
        break
    else:
        print(f"{fn}번째")
    """
    c=check[18:50]
    c=int(c, 16)
    if(fn==1):
        st=c
    elif(fn>=2):
        st=st^c
    print(st, fn)
    asi=""
    ans=""
    length=0
    cs=0
    for j in range(len(c)//2):
        asi=c[2*j:2*j+2]
        if(int(asi, 16)>=32 and int(asi,16)<=126):
            ans=ans+chr(int(asi, 16))
    print(ans, fn)
    if(len(ans)==len(c)//2):
        print(ans)
        break
    """
    f.close()
"""
st=hex(st)[2:]
print(bin(int(st, 16)))
st=bitnot(st)
print(bin(int(st, 16)))
asi=""
ans=""
for i in range(len(st)//2):
    asi=st[2*i: 2*i+2]
    if(int(asi, 16)>=32 and int(asi,16)<=126):
            ans=ans+chr(int(asi, 16))
print(ans)
"""