# go75_suggestAPI

熊本高専から Procon32 自由部門へ応募した参加作品のAPIサーバーです．

57GOの俳句に使える提案語句（種）を生成します．

過去に詠まれた俳句やWikipediaの日本語テキストから，季語と季語以外の単語を提案します．
MeCab,fasttext等を用いて，単語の分散表現による

# description
システム構成

# requirement
必要なライブラリや環境

# installation

```bash
pip install fasttext
```

# Usage

ローカルサーバーを立ち上げ，指定したポートにbase64で変換した画像データをポストすると提案語句を得られます．
```bash
cd api
python go75apiServer.py
```
pickleを用いて分散表現のモデル読み込みを高速化していますが，オブジェクトの読み込みに5~7秒程度かかります．

サーバーを立ち上げる際にgo75apiServer_loaded.pyで実行すると，オブジェクトをサーバー起動時に読み込み，待機します．オブジェクトの読み込み時間はapi呼び出し時に発生しません．

ただし，go75apiServer_loaded.pyはメモリ空間を展開したオブジェクトが占有し続けます.（タスクマネージャーで確認時:6,975.8MB）

# Note
・注意事項

# Author

熊本高専 自由部門 #procon32


*作成者

熊本高専 人間情報システム工学科 4年 野口


*e-mail

hi18noguchi(at)g.kumamoto.nct-ac.jp
