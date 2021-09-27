from bottle import request, route, run, BaseRequest
import json
import pickle
from go75api_loaded import go75api_getwords_loaded as getwords

BaseRequest.MEMFILE_MAX = 1024*1024 * 30

# APIにオブジェクトを渡す
model_path = "./models/wiki_fasttext.pickle"
SUGGEST_MODEL = None
with open(model_path, "rb") as f:
    SUGGEST_MODEL = pickle.load(f)

model_path = "./models/haiku_fasttext.pickle"
SUGGEST_KIGO_MODEL = None
with open(model_path, "rb") as f:
    SUGGEST_KIGO_MODEL = pickle.load(f)

@route('/', method='POST')
def go75api():
    season = request.json["season"]
    image = request.json["image"]

    # 提案語句を受け取る
    body = getwords(image, season, SUGGEST_MODEL, SUGGEST_KIGO_MODEL)
    
    print(body)
    return body

run(host='localhost', port=5575)