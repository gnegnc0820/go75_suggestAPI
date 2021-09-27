from bottle import request, route, run, BaseRequest
import json
import pickle
from go75api import go75api_getwords as getwords

BaseRequest.MEMFILE_MAX = 1024*1024 * 30

@route('/', method='POST')
def go75api():
    season = request.json["season"]
    image = request.json["image"]

    # 提案語句を受け取る
    body = getwords(image, season)
    
    print(body)
    return body

run(host='localhost', port=5575)