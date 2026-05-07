import wave
import numpy as np
import scipy.signal as signal

input_file = '3_input_audio.wav'

new_sample_rate = 11025

with wave.open(input_file, 'rb') as wave_file:
    n_channels = wave_file.getnchannels()
    sample_width = wave_file.getsampwidth()
    sample_rate = wave_file.getframerate()
    n_frames = wave_file.getnframes()

    audio_data = wave_file.readframes(n_frames)
    audio_date = np.frombuffer(audio_data, dtype=np.int16)

    resampled_data = signal.resample(audio_date, int(len(audio_date)*float(new_sample_rate)/sample_rate))

output_file = 'resampled.wav'
with wave.open(output_file, 'wb') as wave_file:
    wave_file.setnchannels(n_channels)
    wave_file.setsampwidth(sample_width)
    wave_file.setframerate(new_sample_rate)
    wave_file.writeframes(resampled_data)