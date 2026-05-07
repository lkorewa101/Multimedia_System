import wave

with wave.open('3_input_audio.wav', 'rb') as wave_in:
    original_frame_rate = wave_in.getframerate()
    print('변경 전')
    print(f"Sample rate: {original_frame_rate}")

with wave.open('resampled.wav', 'rb') as wave_out:
    resampled_frame_rate = wave_out.getframerate()
    print('변경 후')
    print(f"Sample rate: {resampled_frame_rate}")