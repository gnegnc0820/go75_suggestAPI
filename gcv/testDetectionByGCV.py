# WEB_DETECTIONでGCVにリクエストを送信する
def test_web(img_path):
    result = {
'responses': 
[{
    'webDetection': {
        'webEntities': 
        [
            # ここから返す --------------
            {'entityId': '/m/0gzxy', 'score': 0.888271, 'description': 'Bengal cat'},
            {'entityId': '/m/012k6q', 'score': 0.59083325, 'description': 'Ocicat'},
            {'entityId': '/m/04y7lg1', 'score': 0.56017905, 'description': 'Dragon Li'},
            {'entityId': '/m/0891tx', 'score': 0.55142623, 'description': 'Toyger'}, 
            {'entityId': '/m/0g4cd0', 'score': 0.49751002, 'description': 'Tabby cat'}, 
            {'entityId': '/m/0hjzp', 'score': 0.45802948, 'description': 'Kitten'}, 
            {'entityId': '/m/04rky', 'score': 0.3102, 'description': 'Mammal'}, 
            {'entityId': '/m/01l7qd', 'score': 0.27973548, 'description': 'Whiskers'}, 
            {'entityId': '/m/01lrl', 'score': 0.25980508, 'description': 'Carnivores'}, 
            {'entityId': '/m/023kp2', 'score': 0.24739118, 'description': 'Paw'}
        ], 
        'visuallySimilarImages': 
        [
            {'url': 'https://media.istockphoto.com/phoercontent.com/p/AF1QipPuVZFzOgy6xENvO3JhxHU7Q5AWV-e7Bg-ASfIO=s1600-w400'}, 
            {'url': 'https://i.pinimg.com/originals/cd/e4/6f/cde46fa1c79451dcc5f51156f694298d.jpg'}, 
            {'url': 'https://www.jamaicaplainnews.com/wp-content/uploads/2014/12/BEFORE-the-veterinary-team-prep-Phil-for-his-operation-credit-MSPCA-Angell-771x5781.jpg'}
        ], 
        'bestGuessLabels': 
        [
            {'label': 'whiskers'}
        ]
}}]}

    # 確認として最もスコアの高い検出結果を出力
    #print(result['responses'][0]["webDetection"]["webEntities"][0]['description'])
    #print(result['responses'][0]["webDetection"]["webEntities"][0]['score'])

    return result["responses"][0]["webDetection"]["webEntities"]


# LABEL_DETECTIONでGCVにリクエストを送信する
def test_label(img_path):
    result = {
'responses': 
    [{
    'labelAnnotations': 
    [   # ここから返す --------------

        {'mid': '/m/01yrx', 'description': 'Cat', 'score': 0.9617382, 'topicality': 0.9617382}, 
        {'mid': '/m/09686', 'description': 'Vertebrate', 'score': 0.919356, 'topicality': 0.919356}, 
        {'mid': '/m/0307l', 'description': 'Felidae', 'score': 0.91411054, 'topicality': 0.91411054}, 
        {'mid': '/m/08xgn7', 'description': 'Comfort', 'score': 0.90620667, 'topicality': 0.90620667}, 
        {'mid': '/m/01lrl', 'description': 'Carnivore', 'score': 0.90333766, 'topicality': 0.90333766}, 
        {'mid': '/m/07k6w8', 'description': 'Small to medium-sized cats', 'score': 0.87635857, 'topicality': 0.87635857}, 
        {'mid': '/m/04rky', 'description': 'Mammal', 'score': 0.860003, 'topicality': 0.860003}, 
        {'mid': '/m/01l7qd', 'description': 'Whiskers', 'score': 0.8558983, 'topicality': 0.8558983}, 
        {'mid': '/m/0244x1', 'description': 'Gesture', 'score': 0.85260487, 'topicality': 0.85260487}, 
        {'mid': '/m/0276krm', 'description': 'Fawn', 'score': 0.8157809, 'topicality': 0.8157809}
    ]}]}

    # 確認として最もスコアの高い検出結果を出力
    #print(result['responses'][0]["labelAnnotations"][0]['description'])
    #print(result['responses'][0]["labelAnnotations"][0]['score'])

    return result["responses"][0]["labelAnnotations"]