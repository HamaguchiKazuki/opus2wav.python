import librosa as lr
import os


def convert_opus2wav_directory_level(input_dir_path, output_dir_path):
    """ 手順.
        1. input_dir_pathから.opusファイル名を走査する
        2. input_dir_pathのrootと各ファイルをつなげた文字列listを生成する
        3. output_dir_pathのrootとinput_dir_pathの各ファイル名をつなげた文字列listを生成する
        4. convert_opus2wav_file_levelを使用してwavファイルに変換する

    Args:
        input_dir_path ([type]): [description]
        output_dir_path ([type]): [description]
    """
    os.makedirs(output_dir_path, exist_ok=True)


def convert_opus2wav_file_level(input_file_path, output_file_path, sampling_rate):
    data, samplerate = lr.load(input_file_path, sr=sampling_rate)
    lr.audio.sf.write(output_file_path, data, samplerate)
