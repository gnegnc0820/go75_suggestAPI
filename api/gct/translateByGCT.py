import requests, json

url = "https://translation.googleapis.com/language/translate/v2"
key = "AIzaSyBzJc2aGrIrFkzKD7n1eSWea3rdlRogMD8"
post_data = {
    "source": "en",
    "target": "ja",
    "format": "text",
    "key": key
}
def trans(TRANS_WORDS):
    trans_data = "\n".join(TRANS_WORDS)
    post_data["q"] = trans_data

    res = requests.post(url, post_data)
    if res.status_code == 200:
        res = json.loads(res.text)
        res = res["data"]["translations"][0]["translatedText"].split("\n")
    else:
        print("request err in translateByGCT.")
        
    return res