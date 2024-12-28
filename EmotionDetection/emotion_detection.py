import requests
import json

def emotion_detector(text_to_analyze):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    text_obj = { "raw_document": { "text": text_to_analyze }}
    response = requests.post(url, json=text_obj, headers=header)

    if response.status_code == 400:
        emotions = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 
                    'dominant_emotion': None}
    elif response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotion = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion, key=emotion.get)
        emotions = {'anger': emotion['anger'], 'disgust': emotion['disgust'], 'fear': emotion['fear'],
                    'joy': emotion['joy'], 'sadness': emotion['sadness'], 
                    'dominant_emotion': dominant_emotion}
    
    return emotions