import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 
    response = requests.post(url, json = myobj, headers=header)

    if response.status_code == 400:
        response_text = (
            {
                "anger": None, 
                "disgust": None, 
                "fear": None, 
                "joy": None, 
                "sadness": None, 
                "dominant_emotion": None
            }
        )

        return response_text
    else:

        formatted_response = json.loads(response.text)
        emotions = formatted_response['emotionPredictions'][0]['emotion']

        emotions['dominant_emotion'] = max(emotions, key=emotions.get)

        response_text = (
            f"For the given statement, the system response is "
            f"'anger': {emotions['anger']}, "
            f"'disgust': {emotions['disgust']}, "
            f"'fear': {emotions['fear']}, "
            f"'joy': {emotions['joy']} and "
            f"'sadness': {emotions['sadness']}. "
            f"The dominant emotion is {emotions['dominant_emotion']}."
        )

        return response_text
