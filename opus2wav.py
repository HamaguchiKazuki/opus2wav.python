import librosa as lr


def convert_opus2wav_directory_level(input_dir_path, output_dir_path):
    pass


def convert_opus2wav_file_level(input_file_path, output_file_path, sampling_rate):
    data, samplerate = lr.load(input_file_path, sr=sampling_rate)
    lr.audio.sf.write(output_file_path, data, samplerate)
