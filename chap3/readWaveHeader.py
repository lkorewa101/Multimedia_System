import wave

filepath = '3_input_audio.wav'

with wave.open(filepath, 'rb') as wavfile:
    channels = wavfile.getnchannels()
    width = wavfile.getsampwidth()
    original_frame_rate = wavfile.getframerate()
    num_frames = wavfile.getnframes()

    duration = num_frames / original_frame_rate

    print(f"Channels : {channels}")
    print(f"Width : {width}")
    print(f"original_frame_rate : {original_frame_rate}")
    print(f"num_frames : {num_frames}")
    print(f"duration : {duration}")