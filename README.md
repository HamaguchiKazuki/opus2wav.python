# opus2wav
.opusファイルから.wavファイルに変換するツール
[記事](https://qiita.com/Haaamaaaaa/items/74f7ad4f37171a7ac534)

## required
- python: 3.8.5
- ffmpeg: 4.3.1-static

## 使い方
1. opusファイルが入ったフォルダかファイルを用意する
2. ```pip install -r requirements.txt```で必要なライブラリを追加
3. ```python opus2wav.py ---```を使用して変換する
usage:
    Examples file
    python opus2wav.py -i input_opus_files/sample.opus -o output_wav_files/sample.wav -f -sr 48000
    python opus2wav.py -f -i input_opus_files/sample.opus -o output_wav_files/hoge.wav -sr 22050

    Examples directory
    python opus2wav.py -i input_opus_files -o output_wav_files -d -sr 22050
    python opus2wav.py -d -i input_opus_files -o output_wav_files -sr 16000

詳細は ```python opus2wav.py -h```で確認可能
