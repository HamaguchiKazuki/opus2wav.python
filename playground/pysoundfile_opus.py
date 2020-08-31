import soundfile as sf

opus_file_path = "sample_opus_files/sample.opus"

# https://github.com/bastibe/SoundFile/issues/252
data, samplerate = sf.read(opus_file_path)
sf.write("new_output.wav", data, samplerate)
