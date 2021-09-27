import re
from gcv.detectionByGCV import render_detect_label, render_detect_web
from gcv.testDetectionByGCV import test_label, test_web

#from gas.translateByGas import trans
from gct.translateByGCT import trans
from models.getSuggestWords_loaded import getSuggestWords, getKigoWords
from mecab.kToHByMecab import KanjiToH as ktoh, getYomi

import MeCab
import re

def go75api_getwords_loaded(IMAGE,SEASON,SUGGEST_MODEL,KIGO_MODEL): 

    # 画像検出のデータを返す
    detection_web = render_detect_web(IMAGE)
    detection_lab = render_detect_label(IMAGE)
    #detection_web = test_web(IMAGE)
    #detection_lab = test_label(IMAGE)

    # 検出単語を受け取る
    words = dict()

    for l in detection_web:
        if "description" in l:
            line = l["description"].lower()
            words[line] = l["score"]

    for l in detection_lab:
        if "description" in l:
            line = l["description"].lower()
            words[line] = l["score"]


    # 複数回出現する単語を取得する
    wordList = list()
    mlt = dict()
    for word in words:
        for l in word.split(" "):
            wordList.append(l)

    u = list(set(wordList))

    for l in u:
        if wordList.count(l) >= 2:
            mlt[l] = wordList.count(l)
    mlt = sorted(mlt.items(), key=lambda x:x[1], reverse=True)


    # 複数出現した単語をリストに追加する(score=1)
    for l in mlt:
        if not l[0] in words:
            words[l[0]] = 1.0

    words = sorted(words.items(), key=lambda x:x[1], reverse=True)

    # scoreを落としてデータを翻訳する
    for i in range(len(words)):
        words[i] = words[i][0]
    words = trans(words)

    # 正規表現で不安定なカタカナを含む語を排除する
    use_words = list()
    re_katakana = re.compile(r'[\u30A1-\u30F4]+')
    for word in words:
        if not re_katakana.match(word):
            use_words.append(word)

    # 提案語句・季語を得る

    suggest_words = getSuggestWords(use_words,SUGGEST_MODEL)
    suggest_kigos = getKigoWords(use_words,SEASON,KIGO_MODEL)

    
    # 文字数でフィルタをかけて読み仮名を与える
    
    m = MeCab.Tagger("-Oyomi")  

    res = dict()
    res["suggest_words"] = list(set([
        l[0] for k in suggest_words
            for j in k.values()
                for l in j
                    if len(m.parse(l[0])) <= 8
    ]))

    res["suggest_kigos"] = list(set([
        l[0] for k in suggest_kigos
            for j in k.values()
                for l in j
                    if len(m.parse(l[0])) <= 8 
    ])) 


    for i in range(len(res["suggest_words"])):
#        res["suggest_words"][i] = res["suggest_words"][i] + f"({ktoh(res['suggest_words'][i])})"
        res["suggest_words"][i] = res["suggest_words"][i] + f"({getYomi(res['suggest_words'][i]).strip()})"

    for i in range(len(res["suggest_kigos"])):
#        res["suggest_kigos"][i] = res["suggest_kigos"][i] + f"({ktoh(res['suggest_kigos'][i])})"
        res["suggest_kigos"][i] = res["suggest_kigos"][i] + f"({getYomi(res['suggest_kigos'][i]).strip()})"
    
    return res
