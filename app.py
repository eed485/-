import streamlit as st
import subprocess
import os
import pathlib

def check_directory():
    pathlib.Path("tmp").mkdir(parents=True, exist_ok=True)
    pathlib.Path("output").mkdir(parents=True, exist_ok=True)
    pathlib.Path("output/separated_audio").mkdir(parents=True, exist_ok=True)

def main():
    check_directory()

    st.title("音源分離 Web アプリ")
    st.write("この Web アプリは、音源をvocal drum bass othersの4つのステムに分離します。")

    input_audio = st.file_uploader("アップロードしたい音声ファイルを選択してください (.mp3, .wav)")

    if input_audio is not None:
        input_path = os.path.join('tmp', 'input_audio.wav')
        with open(input_path, "wb") as f:
            f.write(input_audio.read())

        output_path = os.path.join('output', 'separated_audio')

        if st.button("分離を開始"):
            st.write("音源分離プロセスを開始します...")

            command = f"spleeter separate {input_path} -o {output_path} -p spleeter:4stems"
            try:
                subprocess.run(command, shell=True, check=True, text=True)
                st.write("音源分離プロセスが正常に終了しました。")

                # Provide links to separated audio files if needed
                st.write(f"[バスドラムのダウンロードリンク](file:///{output_path}/bass.wav)")
                st.write(f"[ボーカルのダウンロードリンク](file:///{output_path}/vocals.wav)")
            except subprocess.CalledProcessError as e:
                st.write("音源分離プロセスでエラーが発生しました。")
                st.write("エラーメッセージ: ", e)

if __name__ == "__main__":
    main()