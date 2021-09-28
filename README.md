# go75_suggestAPI
俳句支援アプリ 57GO の単語提案APIです．
単語の分散表現と季語，その他の単語のDBを用いて単語を提案します．

# descroption
base64でエンコードされた画像データから語句を提案します．

GooglePlatFormから Cloud Vision APIを用いて物体検出を行い，
撮影された画像内に含まれるものを単語として得ます．

単語をフィルタリングした後，gensimによる分散表現モデルを用いて
検出した単語とDB内の単語の近似度を計算し，その結果に基づいて単語を提案します．

季語は季節ごとにDBに格納されており，API呼び出し時に指定した季節の季語を返します．

![tmp](https://user-images.githubusercontent.com/65235517/135016542-3c8a617e-00d5-4bba-845e-a86be91f0cb5.png)

単語の分散表現モデルはFastTextを用いています．
これはDBに存在する単語が分散表現モデルに存在しなくても単語間の近似度を算出できる（未知語の類推ができる）ためです．

分散表現は過去に詠まれた俳句とWikipediaの日本語テキストを用いて作成した二つが存在し，
それぞれ季語とそれ以外の単語の近似度計算に使い分けています．
これらのテキストは学習時点でDB内の単語をneologd辞書に追加した辞書で形態素解析を行い，品詞を絞って作成しました．
学習に用いた

「wikipedia日本語全文データ」
https://dumps.wikimedia.org/jawiki/latest/

「現代俳句抄」  
http://www.haiku-tosasaki.server-shared.com/  
「きごさい歳時記」「きごさいBASE」
https://kigosai.sub.jp/  
「俳誌のサロン」  
http://www.haisi.com/

# requirement

*動作環境  
windows10  
python 3.9.6  
gensim 4.0.1  
mecab 0.996.3  
bottle 0.12.19  

# installation
```bash
pip install gensim
pip install MeCab
pip install bottle
```
API内のMeCabで用いている辞書はipa辞書を用いています．

# usage
ローカルサーバーを立ち上げ，base64の画像データをPOSTして用います．
```bash
cd go75_suggestAPI
python go75apiServer.py
```
go75apiServer_loaded.pyを指定するとオブジェクトの読み込みをサーバー立ち上げ時に行います．
通常は画像データがPOSTされるたびにオブジェクトを読み込みます．

# note
pickleを用いてモデルの読み込みを高速化していますが，一度の読み込みに5~7秒程度かかります．
これはAPIを呼び出されるたびに発生します．

go75apiServer_loaded.pyを選択すると~1秒程度で単語の提案が完了しますが，分散表現モデルがメモリ空間を
占有し続けます．（約7GB）

実際のAPI動作ではgo75apiServer_loaded.pyを用いています．

# author
所属 : 熊本高専 : 
hi18noguchi(at)g.kumaoto-nct.ac.jp
