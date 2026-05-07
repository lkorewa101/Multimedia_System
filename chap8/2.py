import struct


def modify_bmp_pixel(input_filename, output_filename):
    with open(input_filename, 'rb') as f:
        file_data = bytearray(f.read())

    offset = struct.unpack('<I', file_data[10:14])[0]

    img_width = struct.unpack('<i', file_data[18:22])[0]

    # --- 실습 2 조건 ---
    i = 300
    j = 1200

    pixel_index = offset + (i * img_width * 3 + j)

    file_data[pixel_index] = 255
    file_data[pixel_index + 1] = 255
    file_data[pixel_index + 2] = 255

    with open(output_filename, 'wb') as f:
        f.write(file_data)



input_file = "8_lena24b_512x512.bmp"
output_file = "output.bmp"

modify_bmp_pixel(input_file, output_file)