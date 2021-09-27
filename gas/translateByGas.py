import requests
path = "https://script.google.com/macros/s/AKfycbzXkJWgV4uqc3ARQ-mFc8IQ9weG73C9QEF5LlbAy4it0k6r6m3jM8Ny4ktftXlCn3iq/exec"

source = ('source', 'en')
target = ('target', 'ja')

def trans(TRANS_WORDS):
    res = list()
    
    # リクエストを送信する
    post = "\n".join(TRANS_WORDS)
    params = (("text",post),source,target)
    response = requests.get(path, params=params)

    # 正しく翻訳できていれば翻訳結果を返す
    if response.json()["code"] == 200:
        for tw in response.json()["text"].split("\n"):
            res.append(tw)
    else:
        print("request err in translateByGas.")
    return res
