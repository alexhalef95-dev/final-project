from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST', 'GET'])  # Changed route name here
def emotions_route():
    if request.method == 'POST':
        text = request.form.get('text')
        if not text or text.strip() == '':
            return render_template('index.html', error="Invalid text! Please try again!")
        result = emotion_detector(text)
        return render_template('index.html', result=result, input_text=text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=500, debug=True)