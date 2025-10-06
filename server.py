"""
Flask web server for Emotion Detection application.
Handles text input from the user interface and returns emotion analysis results.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(
    __name__,
    template_folder="/home/project/Final_project/Flask_Emo/templates",
    static_folder="/home/project/Final_project/Flask_Emo/static"
)


@app.route("/", methods=["GET"])
def index():
    """
    Render the index page for the web application.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detection():
    """
    Handle emotion detection requests from the web interface.

    Returns:
        str: A formatted message containing emotion scores and dominant emotion,
             or an error message for invalid input.
    """
    text_to_analyze = request.args.get("textToAnalyze", "")

    result = emotion_detector(text_to_analyze)

    # Handle invalid or blank text
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    # Prepare formatted response
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
