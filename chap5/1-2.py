def find_binary_pattern(file_path, pattern):
    position = [] # 패턴이 발견된 위치를 저장할 리스트
    offset = 0 # 파일에서 현재까지 읽은 위치

    overlap_size = len(pattern) - 1
    previous_chunk_tail = b''

    with open(file_path, 'rb') as file:
        while True:
            chunk = file.read(4096) # 4KB씩 읽기
            if not chunk:
                break

            data_to_search = previous_chunk_tail + chunk

            start_index = 0
            while True:
                found_index = data_to_search.find(pattern, start_index)
                if found_index == -1:
                    break

                absolute_position = offset - len(previous_chunk_tail) + found_index

                if not position or position[-1] != absolute_position:
                    position.append(absolute_position)

                start_index = found_index + 1

            if overlap_size > 0:
                previous_chunk_tail = chunk[-overlap_size:]

            offset += len(chunk)

    print(f"패턴 {pattern} 찾기...")
    print(f"총 {len(position)}회 발견됨.")
    print(f"위치: {position}")

    return position

find_binary_pattern("large_data.bin", b'\xDE\xAD\xBE\xEF')
