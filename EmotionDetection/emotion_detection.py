import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=input, headers=headers)
    if response.status_code == 400:
        emotions = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        return emotions
    else:
        fresponse = json.loads(response.text)
        emotions = fresponse['emotionPredictions'][0]['emotion']
        dominant = max(emotions,key=emotions.get)
        emotions['dominant_emotion'] = dominant
        return emotions