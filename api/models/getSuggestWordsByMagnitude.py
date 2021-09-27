import MeCab
from pymagnitude import Magnitude
import sqlite3

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
    model_path = "./models/wiki_default.magnitude"
    db_path = "./models/goi1.0.db"
    model= Magnitude(model_path)
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    words = c.execute("select * from goi").fetchall()


    # 入力ごとに提案語句の類似度を計算する
    SUGGEST_WORDS = []
    for search in SEARCH_WORDS:
        res = {}
        for word in words:
            word = word[1]
            per = model.similarity(word,search)
            res[word] = per


    # 類似度が高い語句を得る
        li = sorted(res.items(),key=lambda x:x[1])
        li = li[-1:-4:-1]
        res = {}
        res[search] = li
        SUGGEST_WORDS.append(res)
    return SUGGEST_WORDS

