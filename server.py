"""
Flask server for the Emotion Detection web app.

- /emotionDetector: returns emotion scores and dominant emotion for the given text.
- /: renders the index page.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")


@app.route("/emotionDetector")
def em_detect():
    """
    Handle the emotion detection request with the parameter 'textToAnalyze'.
    If the dominant emotion is None, returns an invalid text message.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector
    response = emotion_detector(text_to_analyze)

    # Extract scores and dominant emotion
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant = response['dominant_emotion']

    # If dominant emotion is None, show the invalid text message
    if dominant is None:
        return "Invalid text! Please try again!"

    # Return the formatted string
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )

@app.route("/")
def render_index_page():
    """
    Render the index page template.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
