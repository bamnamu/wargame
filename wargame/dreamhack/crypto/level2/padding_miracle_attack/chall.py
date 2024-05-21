from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

flag = open("flag.txt", "r").read()
secret, key, iv = [os.urandom(16) for _ in range(3)]

while True:
	mode = int(input("[1] Encrypt [2] Decrypt [3] Submit: "))

	if mode == 1:
		pt = input("Input plaintext: ")
		if pt == "secret":
			pt = secret
		else:
			pt = bytes.fromhex(pt)
		pt = pad(pt, 16)
		cipher = AES.new(key, AES.MODE_CBC, iv)
		ct = bytes.hex(cipher.encrypt(pt))
		print("pt ==Encryption=>", ct)
		
	elif mode == 2:
		ct = bytes.fromhex(input("Input ciphertext: "))
		try:
			cipher = AES.new(key, AES.MODE_CBC, iv)
			pt = unpad(cipher.decrypt(ct), 16)
			pt = "Don't steal my secret!"
		except:
			pt = "Invalid ciphertext."
		print("ct ==Decryption=>", pt)

	elif mode == 3:
		if bytes.fromhex(input("Enter secret: ")) == secret:
			print("You are a human decryptor!!", flag)
			exit()
		else:
			print("Try again.. T.T")
	else:
		exit()
