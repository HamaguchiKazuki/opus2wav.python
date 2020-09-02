import librosa as lr
import argparse
import os


def convert_opus2wav_directory_level(input_dir_path, output_dir_path, sampling_rate):
    """ 手順.
        1. input_dir_pathから.opusファイル名を走査する
        2. input_dir_pathのrootと各ファイルをつなげた文字列listを生成する
        3. output_dir_pathのrootとinput_dir_pathの各ファイル名をつなげた文字列listを生成する
        4. convert_opus2wav_file_levelを使用してwavファイルに変換する

    Args:
        input_dir_path ([type]): [description]
        output_dir_path ([type]): [description]
    """
    if not os.path.isdir(input_dir_path):
        raise NotADirectoryError(f"No exist dir: {input_dir_path}")
    os.makedirs(output_dir_path, exist_ok=True)
    opus_file_list = os.listdir(input_dir_path)
    for opus_file in opus_file_list:
        file_name, opus_extension = os.path.splitext(opus_file)
        wav_extension = '.wav'
        input_file_path = os.path.join(
            input_dir_path, file_name + opus_extension)
        output_file_path = os.path.join(
            output_dir_path, file_name + wav_extension)
        convert_opus2wav_file_level(
            input_file_path, output_file_path, sampling_rate=sampling_rate)


def convert_opus2wav_file_level(input_file_path, output_file_path, sampling_rate):
    if not os.path.isfile(input_file_path):
        raise NotADirectoryError(f"No exist file: {input_file_path}")
    data, samplerate = lr.load(input_file_path, sr=sampling_rate)
    lr.audio.sf.write(output_file_path, data, samplerate)


DESCRIPTION = \
    """ 
    convert opus file to wav file. 
    """

USAGE = \
    """
    Examples file
    python opus2wav.py -i input_opus_files/sample.opus -o output_wav_files/sample.wav -f -sr 48000
    python opus2wav.py -f -i input_opus_files/sample.opus -o output_wav_files/hoge.wav -sr 22050

    Examples directory
    python opus2wav.py -i input_opus_files -o output_wav_files -d -sr 22050
    python opus2wav.py -d -i input_opus_files -o output_wav_files -sr 16000
    """


def main():
    parser = argparse.ArgumentParser(description=DESCRIPTION, usage=USAGE)
    parser.add_argument("-i", "--input_opus_path", default="input_opus_files",
                        help="Input path of the opus file. It can be specified by a file path or a directory path.", type=str, required=True)
    parser.add_argument("-o", "--output_wav_path", default="output_wav_files",
                        help="Output path of the wav file. It can be specified by a file path or a directory path.", type=str, required=True)
    parser.add_argument("-sr", "--sampling_rate",
                        default=22050, help="convert sampling rate. Default 22050 Hz", type=int, required=False)
    parser.add_argument("-d", "--directory",
                        help="Directory level input/output.", action="store_true", required=False)
    parser.add_argument("-f", "--file",
                        help="File level input/output.", action="store_true", required=False)
    args = parser.parse_args()

    is_directory = args.directory
    is_file = args.file
    if is_directory:
        convert_opus2wav_directory_level(
            args.input_opus_path, args.output_wav_path, args.sampling_rate)
    elif is_file:
        convert_opus2wav_file_level(
            args.input_opus_path, args.output_wav_path, args.sampling_rate)
    else:
        raise NotImplemented("Be sure to use either -f or -d flags.")


if __name__ == "__main__":
    main()
