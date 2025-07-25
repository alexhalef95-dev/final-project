import requests
import json

def emotion_detector(text_to_analyse):
    """ Use Emotion Predict function of the Watson NLP Library to analyse text
    """
    # URL of the emotion analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
   
    # Custom header specifying the model ID for the emotion analysis service
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
   
    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }
   
    # Sending a POST request to the emotion analysis API
    response = requests.post(url, json = myobj, headers=headers)
   
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
   
    # Extract emotions and scores
    if response.status_code == 200:
        emotions = formatted_response["emotionPredictions"][0]["emotion"]

        # Identify dominant emotion
        dom_label = max(emotions, key=emotions.get)

        # Add the dominant emotion to dictionary of emotions
        emotions['dominant_emotion'] = dom_label

    # If error
    elif response.status_code == 400:
        emotions = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # Return list of emotions
    return emotions