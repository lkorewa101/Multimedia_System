import os


def xor_encrypt(input_path, key, output_path="output_encrypted.bin"):
    """
    바이너리 파일을 지정된 XOR 키로 암호화 및 복호화하는 함수
    동일한 함수로 암호화와 복호화를 모두 수행할 수 있습니다.
    """
    with open(input_path, 'rb') as f_in, open(output_path, 'wb') as f_out:
        while True:
            chunk = f_in.read(4096)  # 4KB씩 읽기
            if not chunk:
                break

            # XOR 연산 수행 후 저장
            f_out.write(bytes(b ^ key for b in chunk))


if __name__ == "__main__":
    # 요구사항에 정확히 맞춘 콘솔 입력 화면
    input_file = input("input file : ")
    output_file = input("output file: ")

    # 출력 파일명을 입력하지 않으면 기본 파일명 사용
    if not output_file.strip():
        output_file = "output_encrypted.bin"

    key = int(input("input XOR key(0~255) : "))

    # 암호화/복호화 함수 호출
    xor_encrypt(input_file, key, output_file)

    # 요구사항에 정확히 맞춘 완료 출력 화면
    print(f"Complete : {output_file}")