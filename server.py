"""
Flask server for the Emotion Detection application.

This module exposes a web interface that allows users to analyze
text emotions using the EmotionDetection package.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

# Constants
HOST = "localhost"
PORT = 5000
TEMPLATE_FOLDER = "templates"
STATIC_FOLDER = "static"

app = Flask(
    __name__,
    template_folder=TEMPLATE_FOLDER,
    static_folder=STATIC_FOLDER
)


@app.route("/")
def index():
    """
    Render the home page.

    Returns:
        str: Rendered HTML template.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """
    Handle emotion detection requests.

    Expects a query parameter named 'textToAnalyze'.
    Returns emotion analysis results or an error message.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return jsonify(result)


def main():
    """
    Run the Flask development server.
    """
    app.run(host=HOST, port=PORT)


if __name__ == "__main__":
    main()
