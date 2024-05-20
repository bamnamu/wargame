from pwn import *
import os

io = remote("host3.dreamhack.games", 8401)

# 첫 번째 코드
io.recvuntil(b'= ')
secret_enc = bytes.fromhex(io.recvline().decode())
e = bytes.hex(secret_enc)  # 암호문
print(f"암호문 (e): {e}")

# 첫 번째 코드에서 사용한 임의의 값
random_value = '00112233445566778899aabbccddeeff'

io.sendline(b'2')
io.sendline(random_value.encode())  # 아무거나
io.recvuntil(b'= ')
h = io.recvline()[:-1].decode()  # dec(아무거나)
print(f"dec(아무거나) (h): {h}")

he = hex(int(random_value, 16) ^ int(e, 16))[2:]  # 아무거나 XOR 암호문
he.zfill(len(e))
print('처음 : ', he)
io.sendline(b'2')
io.sendline(he.encode())
io.recvuntil(b'= ')
he = io.recvline()[:-1].decode()  # dec(암호문 XOR 아무거나)
print(f"dec(암호문 XOR 아무거나) (he): {he}")

io.sendline(b'2')
io.sendline(b'00000000000000000000000000000000')  # 0
io.recvuntil(b'= ')
z = io.recvline()[:-1].decode()  # dec(0)
print(f"dec(0) (z): {z}")

ans = hex(int(h, 16) ^ int(he, 16) ^ int(z, 16))[2:]  # dec(아무거나) XOR dec(0) XOR dec(암호문 XOR 아무거나)
print(f"최종 결과값 (ans): {ans}")
ans.zfill(len(e))

# 두 번째 코드
xor = lambda a, b: bytes([i ^ j for i, j in zip(a, b)])

print(f"암호문 (secret_enc): {secret_enc.hex()}")

def encrypt(plaintext):
    io.sendline(b"1")
    io.sendline(bytes.hex(plaintext).encode())
    io.recvuntil(b"= ")
    ciphertext = bytes.fromhex(io.recvline().decode())
    return ciphertext

def decrypt(ciphertext):
    io.sendline(b"2")
    io.sendline(bytes.hex(ciphertext).encode())
    io.recvuntil(b"= ")
    plaintext = bytes.fromhex(io.recvline().decode())
    return plaintext

# 첫 번째 코드와 동일한 임의의 값 사용
b = bytes.fromhex('00112233445566778899aabbccddeeff')

p1 = decrypt(bytes(16))
print(f"dec(0) (p1): {p1.hex()}")
p2 = decrypt(xor(secret_enc, b))
print("나중 : ", bytes.hex(xor(secret_enc, b)))
print(f"dec(secret_enc XOR b) (p2): {p2.hex()}")
p3 = decrypt(b)
print(f"dec(b) (p3): {p3.hex()}")

p = xor(p1, xor(p2, p3))
print(f"최종 결과값 (p): {p.hex()}")
io.sendline(b'1')
io.sendline(ans.encode())
#encrypt(p)

io.interactive()