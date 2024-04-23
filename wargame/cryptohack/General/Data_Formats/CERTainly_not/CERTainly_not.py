from Crypto.PublicKey import RSA

with open('C:\\Users\\taotr\\Desktop\\wargame\\wargame\\cryptohack\\General\\Data_Formats\\CERTainly_not\\2048b-rsa-example-cert.der', 'rb') as key_file:
    key_info=key_file.read()

print(RSA.importKey(key_info).n)

#바이너리 파일을 열때는 'rb' 써야 한다.