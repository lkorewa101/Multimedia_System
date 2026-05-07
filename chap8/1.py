import struct

def bmp_header(filename):
    with open(filename, 'rb') as bmp_file:
        magic_num = struct.unpack('<H', bmp_file.read(2))[0]
        print(f"Type : {magic_num:x}")

        file_size = struct.unpack('<I', bmp_file.read(4))[0]
        print(f"Size : {file_size:x}")

        bmp_file.read(4)

        start_offset = struct.unpack('<I', bmp_file.read(4))[0]
        print(f"OffBits : {start_offset:x}")

        dib_header_size = struct.unpack('<I', bmp_file.read(4))[0]

        width = struct.unpack('<i', bmp_file.read(4))[0]
        height = struct.unpack('<i', bmp_file.read(4))[0]

        print(f"Height : {height}")
        print(f"Width : {width}")

        bmp_file.read(2)

        bit_count = struct.unpack('<H', bmp_file.read(2))[0]
        print(f"BitCount : {bit_count}")

        bmp_file.read(4)

        size_image = struct.unpack('<I', bmp_file.read(4))[0]
        print(f"SizeImage : {size_image}")

        xpels = struct.unpack('<i', bmp_file.read(4))[0]
        print(f"XpelsPerMeter : {xpels}")

        ypels = struct.unpack('<i', bmp_file.read(4))[0]
        print(f"YPelsPerMeter : {ypels}")

        clr_used = struct.unpack('<I', bmp_file.read(4))[0]
        print(f"ClrUsed : {clr_used}")

        clr_important = struct.unpack('<I', bmp_file.read(4))[0]
        print(f"ClrImportant : {clr_important}")


# 함수 실행
bmp_header("8_lena24b_512x512.bmp")