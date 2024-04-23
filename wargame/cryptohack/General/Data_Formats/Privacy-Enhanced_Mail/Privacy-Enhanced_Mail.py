from Crypto.PublicKey import RSA

with open('C:\\Users\\taotr\\Desktop\\wargame\\wargame\\cryptohack\\General\\Data_Formats\\Privacy-Enhanced_Mail\\privacy_enhanced_mail.pem', 'r') as key_file:
    key_info=key_file.read()

print(RSA.importKey(key_info).d)