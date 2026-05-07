import os
import random

def generate_large_binary_file(file_path, file_size=50 * 1024 * 1024, pattern=b'\xDE\xAD\xBE\xEF', insert_count=10):
    with open(file_path, 'wb') as file:
        file.write(os.urandom(file_size))

        for _ in range(insert_count):
            position = random.randint(0, file_size - len(pattern))
            file.seek(position)
            file.write(pattern)

generate_large_binary_file("large_data.bin", file_size=50 * 1024 * 1024, insert_count=10)