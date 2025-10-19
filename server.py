"""Flask app for detecting emotions from text input."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """Render the home page."""
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detect():
    """Handle emotion detection requests."""
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is not None:
        return response

    return "Invalid text! Please try again!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
