from Crypto.PublicKey import RSA

with open('C:\\Users\\taotr\\Desktop\\wargame\\wargame\\cryptohack\\General\\Data_Formats\\SSH_Keys\\bruce_rsa_6e7ecd53b443a97013397b1a1ea30e14.pub', 'rb') as key_file:
    key_info=key_file.read()

print(RSA.importKey(key_info).n)