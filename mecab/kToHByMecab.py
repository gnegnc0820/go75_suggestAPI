from typing import Pattern
import MeCab
import re

def KatakanaToH(text):
    hiragana=[chr(i) for i in range(12353, 12436)]
    katakana=[chr(i) for i in range(12449, 12532)]
    kana=""

    # カナ⇒かな 変換する
    for text in list(text):
        for i in range(83):
            if text == katakana[i] or text == hiragana[i]:
                kana+=hiragana[i]
    return kana

def KanjiToH(text):
    # ascii文字を含んでいたらそのまま返す
    if str.isascii(text):
        return text

    mecab = MeCab.Tagger("-Ochasen")

    #空でパースする
    mecab.parse('')
    node=mecab.parseToNode(text)

    res = list()
    while node :
        #単語を代入
        origin=node.surface
        #読み仮名を代入
        kana=node.feature.split(",")[7]

        #正規表現で漢字と一致するかをチェック
        pattern = "[一-龥]"
        matchOB = re.match(pattern , origin)

        #originが空のとき、漢字以外の時はそのまま出力
        if origin != "" and matchOB:
            res.append(kana)
        else :
            res.append(origin)
        # 更新
        node=node.next
    return KatakanaToH("".join(res))

def getYomi(text):
    res = None
    pattern = re.compile(r'^[あ-ん]+$')
    if pattern.fullmatch(text):
        res = text
    else:
        m = MeCab.Tagger("-Oyomi")
        res = m.parse(text)
        res = "-".join(pattern.findall(res))

    return res