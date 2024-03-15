from pwn import * # pip install pwntools
import json
import base64
import codecs
from Crypto.Util.number import *

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

while(True):
    received = json_recv()

    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])
    p=""
    c=received["encoded"]
    if(received["type"]=="utf-8"):
        for i in range(len(c)):
            p=p+chr( c[i] )
    elif(received["type"]=='base64'):
        p=base64.b64encode(c)
    elif(received["type"]=='hex'):
        p=bytes.fromhex(c)
    elif(received["type"]=='bigint'):
        p=long_to_bytes(c)
    else:
        decoded = codecs.encode(c, 'rot_13')
    to_send = {
        "decoded": p
    }
    json_send(to_send)
    received=json_recv()
    if "flag" in received:
        print("Flag received:", received["flag"])
        break