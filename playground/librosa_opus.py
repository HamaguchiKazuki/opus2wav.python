import librosa as lr

opus_file_path = "input_opus_files/sample.opus"

# Required ffmpeg(Fast Forward MPEG) https://ffmpeg.org/download.html
data, samplerate = lr.load(opus_file_path, sr=None)

save_wav_file_path = "output_wav_files/a.wav"
lr.audio.sf.write(save_wav_file_path, data, samplerate)
