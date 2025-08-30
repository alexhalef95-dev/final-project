"""Server module for Emotion Detection web application using Flask."""

from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route('/emotionDetector', methods=['GET', 'POST'])
@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detector_endpoint():
    """Endpoint for detecting emotions from a given text.

    Accepts GET and POST requests:
    - POST: expects JSON {"text": "<user_text>"}
    - GET: expects query parameter textToAnalyze=<user_text>

    Returns:
        JSON response containing emotion scores and dominant emotion,
        or an error message if the input is invalid.
    """
    if request.method == 'POST':
        data = request.get_json()
        text_to_analyze = data.get('text', '')
    else:
        text_to_analyze = request.args.get('textToAnalyze', '')

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return jsonify({"message": "Invalid text! Please try again!"})

    formatted_response = {
        "anger": result['anger'],
        "disgust": result['disgust'],
        "fear": result['fear'],
        "joy": result['joy'],
        "sadness": result['sadness'],
        "dominant_emotion": result['dominant_emotion']
    }

    return jsonify(formatted_response)



@app.route('/')
def index():
    """Render the main index page."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
