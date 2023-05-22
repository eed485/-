# API
## 環境構築
anacondaをインストール
https://www.python.jp/install/anaconda/windows/install.html

ターミナルで
$ pip install -r requirements.txt

$ streamlit run app.py

## やってること
音源分離の学習済みモデルがpretrained_modeに格納
web上で音源ファイル受け取り
学習済みモデルで推論
コマンドラインをpython上で実行し，outputに4stem(vocal,drum,bass,others)で格納


