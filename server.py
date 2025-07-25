''' Executing this function initiates the application of emotion
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask(__name__)

@app.get("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs emotion analysis over it using emotion_detector()
        function. The output returned shows the proportion of each emotion
        and the dominant emotion.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    results = emotion_detector(text_to_analyze)

    # Isolate dominant emotion
    dom_label = results.pop("dominant_emotion")

    # Format other emotions
    emotions = str(results).replace("{","").replace("}","")

    # Return error message if API unsucessful
    if dom_label is None:
        return "Invalid text! Please try again!"

    # Return results if API sucessful
    p1_text = "For the given statement, the system response is"
    p2_text = "The dominant emotion is"
    return f"{p1_text} {emotions}. {p2_text} {dom_label}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
