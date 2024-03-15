

with open('encfile', 'r') as f:
    enc_list=f.read()
crypto_text=[]
for i in range(len(enc_list)//2):
    crypto_text.append(enc_list[2*i:2*i+2])

dec_list = list(range(len(crypto_text)))

hex_list = [(hex(i)[2:].zfill(2).upper()) for i in range(256)]
for i in range(len(crypto_text)):
    hex_a = crypto_text[i]
    index = hex_list.index(hex_a)
    dec_list[i] = hex_list[(index-128)%len(hex_list)]
dec_list = ''.join(dec_list)
dec_list = bytes.fromhex(dec_list)

with open('flag.png', 'wb') as f:
    f.write(dec_list)