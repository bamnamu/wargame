from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import base64
import binascii

# PEM 형식의 공개 키
pem_key = """MIIBIDANBgkqhkiG9w0BAQEFAAOCAQ0AMIIBCAKBgQFSOuj6SExa7VtHUvbbnY57
aGVM9brzp5p/Iq4O4CcLaa4Ssj6lc2AY6iAHIgciWDwrYVrnmKyEXaFVZvjvsh9N
snuDq5RpIe3X9GAnvH6BWROxpPwmyPtULcyCFfkx5kR2sjQSVTbRXoste6xNzm63
524mnnhJ2FhXPMLzg/vSmQKBgQEKnblIfuXfwtCild+olEsxXmNu5c/RGi4AOWmm
jMqvGoXYNKW5UvJJwIhjnAkU5JiMWTAjndXZGCZ7xWgZsJ/iziDVVsa3WzFEh494
3TQva3LG9hwOXRYD2BYsSajZ7RWz/yLqKRAmBE5Si2dTxUhmwHgScSKDsSzqKBhc
YFQd2Q=="""

# PEM 형식의 시작 및 끝 문자열 제거
pem_key = pem_key.replace("-----BEGIN PUBLIC KEY-----", "").replace("-----END PUBLIC KEY-----", "")

# Base64 디코딩
binary_data = base64.b64decode(pem_key) #base64로 된걸 디코딩해서 바이트 스트림(이진 데이터)으로 바꿈

# ASN.1 구조 파싱
try:
    key = serialization.load_der_public_key(binary_data, backend=default_backend()) #바이트 스트림을 der 형식(표준 형식)의 공개키로 파싱(디코딩+파이썬 객체로 변환),
    public_numbers = key.public_numbers()
    
    # 모듈러 n과 공개 지수 e 출력
    n = hex(public_numbers.n)
    e = hex(public_numbers.e)

except Exception as e:
    print(f"Error parsing the public key: {e}")


"""
PEM 형식의 공개 키는 X.509 표준에 따라 ASN.1 (Abstract Syntax Notation One) 형식으로 인코딩되어 있습니다.
이것은 공개 키에 대한 표준 데이터 형식을 정의합니다.
RSA 공개 키의 구조는 다음과 같습니다:
SEQUENCE: 전체 공개 키 구조는 SEQUENCE로 시작합니다.
AlgorithmIdentifier: 공개 키의 알고리즘 식별자를 나타냅니다.
이 부분은 사용된 알고리즘의 유형과 매개변수에 대한 정보를 제공합니다.
BIT STRING: 실제 공개 키 값이 포함된 BIT STRING입니다.
이 부분이 RSA 공개 키의 핵심입니다.
RSA 공개 키의 BIT STRING 부분을 디코딩하면 다시 다음과 같은 구조가 나타납니다:
SEQUENCE: 다시 한 번 SEQUENCE로 시작합니다.
INTEGER (n): 모듈러 n의 값이 들어 있습니다. 이는 두 개의 소수인 p와 q를 곱한 결과입니다.
INTEGER (e): 공개 지수 e의 값이 들어 있습니다.
이렇게 ASN.1 구조로 표현된 것이 PEM 형식의 공개 키입니다.
따라서, PEM 형식의 공개 키에서 n과 e 값을 추출하려면 BIT STRING 부분을 디코딩하고, 그 안에서 다시 INTEGER 값을 추출하면 됩니다.
"""

n=int(n, 16)
e=int(e, 16)
print(e/n)