import struct


def draw_hollow_rectangle(input_filename, output_filename):
    with open(input_filename, 'rb') as f:
        file_data = bytearray(f.read())

    offset = struct.unpack('<I', file_data[10:14])[0]
    width = struct.unpack('<i', file_data[18:22])[0]
    height = struct.unpack('<i', file_data[22:26])[0]

    x_start, x_end = 260, 420
    y_start, y_end = 80, 280
    thickness = 3

    for y in range(y_start, y_end):
        row_in_file = height - 1 - y

        for x in range(x_start, x_end):
            is_top_border = (y - y_start < thickness)
            is_bottom_border = (y_end - 1 - y < thickness)
            is_left_border = (x - x_start < thickness)
            is_right_border = (x_end - 1 - x < thickness)

            if is_top_border or is_bottom_border or is_left_border or is_right_border:
                pixel_index = offset + (row_in_file * width * 3) + (x * 3)

                file_data[pixel_index] = 0
                file_data[pixel_index + 1] = 255
                file_data[pixel_index + 2] = 0

    with open(output_filename, 'wb') as f:
        f.write(file_data)



input_file = "8_lena24b_512x512.bmp"
output_file = "output_hollow_rect.bmp"

draw_hollow_rectangle(input_file, output_file)