import requests
import base64
import json

API_KEY = 'AIzaSyBzJc2aGrIrFkzKD7n1eSWea3rdlRogMD8'
GOOGLE_CLOUD_VISION_API_URL = 'https://vision.googleapis.com/v1/images:annotate?key='
MAX_RESULTS = 10


# GCVにwebでリクエストする -> json
def request_cloud_vison_api(image_base64, type):
    api_url = GOOGLE_CLOUD_VISION_API_URL + API_KEY
    req_body = json.dumps({
        'requests': [{
            'image': {
                'content': image_base64
            },
            'features': [{
                'type': type,
                'maxResults': MAX_RESULTS,
            }]
        }]
    })
    res = requests.post(api_url, data=req_body)
    return res.json()


# WEB_DETECTIONでGCVにリクエストを送信する
def render_detect_web(img):
    DETECTION_TYPE = "WEB_DETECTION"
    result = request_cloud_vison_api(image_base64=img,
                                     type=DETECTION_TYPE)

    # 確認として最もスコアの高い検出結果を出力
    #print(result['responses'][0]["webDetection"]["webEntities"][0]['description'])
    #print(result['responses'][0]["webDetection"]["webEntities"][0]['score'])

    return result["responses"][0]["webDetection"]["webEntities"]


# LABEL_DETECTIONでGCVにリクエストを送信する
def render_detect_label(img):
    DETECTION_TYPE = "LABEL_DETECTION"
    result = request_cloud_vison_api(image_base64=img,
                                     type=DETECTION_TYPE)

    # 確認として最もスコアの高い検出結果を出力
    #print(result['responses'][0]["labelAnnotations"][0]['description'])
    #print(result['responses'][0]["labelAnnotations"][0]['score'])

    return result["responses"][0]["labelAnnotations"]