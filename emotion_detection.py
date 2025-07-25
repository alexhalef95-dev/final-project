import requests
import json

def emotion_detector(detected_text):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)
    if all(value is None for value in text_to_analyse.values()):
        return detected_text
    emotions = detected_text['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions.items(), key=lambda x: x[1])[0]
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']
    max_emotion = max(emotions, key=emotions.get)
    #max_emotion_score = emotions[max_emotion]
    formatted_dict_emotions = {
                            'anger': anger,
                            'disgust': disgust,
                            'fear': fear,
                            'joy': joy,
                            'sadness': sadness,
                            'dominant_emotion': max_emotion
                            }
    return formatted_dict_emotions
