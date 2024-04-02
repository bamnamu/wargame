import base64
import hashlib

for fn in range(1, 2):
    # 이메일 파일 경로
    format_fn=f"{fn:04}"
    file_path = rf"C:\Users\82104\Desktop\security\ctf\Gon_2024_spring_qual\misc\phony_for-user\for_user\{format_fn}.eml"

    # 이메일 본문과 bh= 필드 값을 읽기
    body_encoded = ""
    bh_value = ""
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        in_body = False
        for line in lines:
            if line.startswith("bh="):
                bh_value = line.strip().split('=')[1]
            if line.strip() == "------=_Part_637668_882540399.1711440339789":
                in_body = not in_body
            elif in_body and not line.strip().startswith("Content-Type:"):
                body_encoded += line.strip()
    # Base64로 인코딩된 이메일 본문을 디코딩
    body_decoded = base64.b64decode(body_encoded).decode('utf-8')
    print(body_decoded)
    # SHA-256 해시 계산
    hash_obj = hashlib.sha256()
    hash_obj.update(body_decoded)
    body_hash = base64.b64encode(hash_obj.digest()).decode('utf-8')

    # bh= 필드 값과 비교
    if body_hash == bh_value:
        print(f"{fn}번째, 무결성 검증 성공: 이메일 본문이 변경되지 않았습니다.")
        break
    else:
        print(f"{fn}번째, 실패")