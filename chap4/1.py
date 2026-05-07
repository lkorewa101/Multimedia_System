import struct

def parse_wave_raw(filename):
    with open(filename, 'rb') as wav_file:
        chunk_id = wav_file.read(4)

        chunk_size = struct.unpack('<I', wav_file.read(4))[0]

        wav_format = wav_file.read(4)

        sub_chunk_1_id = wav_file.read(4)

        sub_chunk_1_size = struct.unpack('<I', wav_file.read(4))[0]

        audio_format = struct.unpack('<H', wav_file.read(2))[0]

        num_channels = struct.unpack('<H', wav_file.read(2))[0]

        sample_rate = struct.unpack('<I', wav_file.read(4))[0]

        byte_rate = struct.unpack('<I', wav_file.read(4))[0]

        block_align = struct.unpack('<H', wav_file.read(2))[0]

        bits_per_sample = struct.unpack('<H', wav_file.read(2))[0]

        sub_chunk_2_id = wav_file.read(4)

        sub_chunk_2_size = struct.unpack('<I', wav_file.read(4))[0]

        print(f"chunk_id : {chunk_id}")
        print(f"wav_format : {wav_format}")
        print(f"sample_rate : {sample_rate}")
        print(f"byte_rate : {byte_rate}")
        print(f"chunk_size : {chunk_size}")
        print()

        samples = []
        bytes_per_sample = bits_per_sample / 8

        sample_count = int(sub_chunk_2_size / bytes_per_sample)

        for _ in range(sample_count):
            sample = struct.unpack('<h', wav_file.read(2))[0]
            samples.append(sample)

        assert chunk_size == (
            len(wav_format) +
            len(sub_chunk_1_id) + sub_chunk_1_size + 4 +
            len(sub_chunk_2_id) + sub_chunk_2_size + 4
        ), chunk_size

        assert sub_chunk_1_size == (
            2 + 2 + 4 + 4+ 2 + 2
        ), sub_chunk_1_size

        bytes_per_sample = bits_per_sample / 8
        assert byte_rate == (
            sample_rate * num_channels * bytes_per_sample
        ), byte_rate

        assert block_align == (
            num_channels * bytes_per_sample
        ), block_align

        assert sub_chunk_2_size == (
            len(samples) * bytes_per_sample
        ), sub_chunk_2_size

        length_in_seconds = (
            len(samples) / sample_rate
        )

        print('샘플 개수:', len(samples))
        print('처음 10개:', samples[:10])
        print('마지막 5개:', samples[-5:])
        print()

        return samples

samples = parse_wave_raw('3seconds.wav')

from comp import compare_lowdata
print(compare_lowdata(samples))