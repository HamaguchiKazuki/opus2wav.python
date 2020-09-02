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
    if not os.path.exists(input_dir_path):
        raise NotADirectoryError(f"No exist dir: {input_dir_path}")
    os.makedirs(output_dir_path, exist_ok=True)
    opus_file_list = os.listdir(input_dir_path)
    for opus_file in opus_file_list:
        file_name, opus_extension = os.path.splitext(opus_file)
        wav_extension = '.wav'
        input_file_path = os.path.join(input_dir_path, file_name + opus_extension)
        output_file_path = os.path.join(output_dir_path, file_name + wav_extension)
        convert_opus2wav_file_level(input_file_path, output_file_path, sampling_rate=22050)


def convert_opus2wav_file_level(input_file_path, output_file_path, sampling_rate):
    data, samplerate = lr.load(input_file_path, sr=sampling_rate)
    lr.audio.sf.write(output_file_path, data, samplerate)
