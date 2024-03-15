
hex_list = [(hex(i)[2:].zfill(2).upper()) for i in range(256)]

with open('encfile', 'rb') as f:
    enc_s=f.read()
enc_s=enc_s.hex()
enc_s="0x"+enc_s
