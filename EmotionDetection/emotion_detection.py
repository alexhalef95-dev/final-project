import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }

    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # Convert the response text to a Python dictionary
    response_dict = json.loads(response.text)

    # Extract the first emotion prediction
    emotions = response_dict["emotionPredictions"][0]["emotion"]

    # Find the emotion with the highest value
    dominant_emotion = max(emotions, key=emotions.get)

    return dominant_emotion


