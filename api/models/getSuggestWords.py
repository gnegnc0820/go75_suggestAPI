import MeCab
from gensim.models import fasttext
import sqlite3
import pickle

# 極端に短い単語、複合した単語、名詞以外の入力を切り捨てる
def cutNoCommonWords(WORDS):
    m = MeCab.Tagger("-Ochasen")
    mo = MeCab.Tagger("-Oyomi")
    res = list()
    
    # 名詞以外を切り捨てる
    for word in WORDS:
        mouns = [l[:l.find("\t")] for l in m.parse(word).splitlines()
                            if ("名詞" in l.split()[-1] 
                            #and("固有" in l.split()[-1]  or "一般" in l.split()[-1] )
                            )
                        ]
        # 一音の単語、複合した単語を切り捨てる
        if len(mouns) == 1 and len(mo.parse(mouns[0]).strip()) >=2:
            res.append(mouns[0])
    return list(set(res))


# 季語以外の提案語句を得る
def getSuggestWords(SEARCH_WORDS):

    # 入力単語の切り捨て
    SEARCH_WORDS = cutNoCommonWords(SEARCH_WORDS)

    # データの読み込み
    #model_path = "./models/model_haiku_fasttext.bin"
    #model_path = "./models/model_wiki_fasttext.bin"
    #model_path = "./models/model_wiki_fasttext_meisi.bin"
    model_path = "./models/wiki_fasttext.pickle"
    db_path = "./models/goi1.0.db"

    #model = fasttext._load_fasttext_format(model_path)
    model = None
    with open(model_path, "rb") as f:
        model = pickle.load(f)

    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    words = c.execute("select * from goi").fetchall()


    # 入力ごとに提案語句の類似度を計算する
    SUGGEST_WORDS = []
    for search in SEARCH_WORDS:
        res = {}
        for word in words:
            word = word[1]
            per = model.wv.similarity(word,search)
            res[word] = per


    # 類似度が高い語句を得る
        li = sorted(res.items(),key=lambda x:x[1])
        li = li[-1:-4:-1]
        res = {}
        res[search] = li
        SUGGEST_WORDS.append(res)
    return SUGGEST_WORDS


# 提案する季語を得る
def getKigoWords(SEARCH_WORDS,SEASON):

    # 入力単語の切り捨て
    SEARCH_WORDS = cutNoCommonWords(SEARCH_WORDS)

    # データの読み込み
    #model_path = "./models/model_haiku_fasttext.bin"
    db_path = "./models/kigo2.0.db"

    #model= fasttext._load_fasttext_format(model_path)
    model_path = "./models/haiku_fasttext.pickle"
    model = None
    with open(model_path, "rb") as f:
        model = pickle.load(f)

    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    kigo = c.execute("select * from kigo").fetchall()

    # 入力ごとに季語の類似度を計算する
    SUGGEST_WORDS = list()
    for search in SEARCH_WORDS:
        seasons = {"春":{},"夏":{},"秋":{},"冬":{}}
        for i in range(len(kigo)):
            word = str(kigo[i][1])
            per = model.wv.similarity(word,search)
            seasons[kigo[i][2]][word] = per

    # 類似度が高い季語を得る
        li = sorted(seasons[SEASON].items(),key=lambda x:x[1])
        li = li[-1:-4:-1]
        res = dict()
        res[search] = li
        SUGGEST_WORDS.append(res)
    return SUGGEST_WORDS
