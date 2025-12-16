from flask import Flask, request, render_template, jsonify
from EmotionDetection import emotion_detector
import requests
import json

app = Flask(__name__)

# Define the route as requested
@app.route("/emotionDetector", methods=["POST"])
def emotionDetector():
    # Get the statement from the POST request
    data = request.json
    statement = data.get("text", "")

    # Call the Watson API directly to get full emotion scores
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    payload = {
        "raw_document": {"text": statement}
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    response_dict = response.json()

    # Extract emotions
    emotions = response_dict["emotionPredictions"][0]["emotion"]
    # Determine dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    # Add dominant emotion to output
    emotions["dominant_emotion"] = dominant_emotion

    # Prepare formatted string for display
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {emotions['anger']}, "
        f"'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, "
        f"'joy': {emotions['joy']}, "
        f"'sadness': {emotions['sadness']}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    # Return JSON
    return jsonify(emotions=emotions, message=formatted_response)

# Run the server on localhost:5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
