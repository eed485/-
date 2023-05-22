import argparse
from spleeter.separator import Separator

def separate_audio(input_path, output_path):
    separator = Separator('spleeter:2stems')
    separator.separate_to_file(input_path, output_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Audio Separation')
    parser.add_argument('-i', '--input', required=True, help='Path to input audio file')
    parser.add_argument('-o', '--output', required=True, help='Path to output folder for the separated audio files')
    args = parser.parse_args()

    separate_audio(args.input, args.output)