from Crypto.PublicKey import RSA

with open('C:\\Users\\taotr\\Desktop\\wargame\\wargame\\cryptohack\\General\\Data_Formats\\Transparency\\transparency.pem', 'r') as key_file:
    key_info=key_file.read()

print(RSA.importKey(key_info).e)


#https://subdomainfinder.c99.nl/
#서브 도메인 찾는 사이트
#https://thetransparencyflagishere.cryptohack.org
#crypto{thx_redpwn_for_inspiration}