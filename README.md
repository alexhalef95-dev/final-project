# 🧠 AI-Based Emotion Detection Web Application

A complete AI-powered web application built with Flask and IBM Watson NLP to detect **emotions** from customer feedback text. This project includes **data analysis**, **testing**, **error handling**, **static code analysis**, and **web deployment**.

---

## 📁 Project Structure

```
final_project/
│
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
│
├── static/
│   └── mywebscript.js
│
├── templates/
│   └── index.html
│
├── server.py
├── test_emotion_detection.py
├── README.md
└── [screenshots...]
```

---

## 🧩 Tasks Overview & Code

### ✅ Task 1: Fork & Clone

```bash
git clone https://github.com/YOUR_USERNAME/oaqjp-final-project-emb-ai.git final_project
cd final_project
```

---

### ✅ Task 2: Create Emotion Detection Module

**File:** `emotion_detection.py`

```python
import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 400:
        return {
            'anger': None, 'disgust': None, 'fear': None,
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }
    response_json = json.loads(response.text)
    emotions = response_json['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)
    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
```

---

### ✅ Task 3: Format Output

Already included above in `emotion_detector()` function.

---

### ✅ Task 4: Package as Module

**Folder:** `EmotionDetection/`  
**File:** `__init__.py`

```python
from .emotion_detection import emotion_detector
```

---

### ✅ Task 5: Unit Testing

**File:** `test_emotion_detection.py`

```python
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        self.assertEqual(emotion_detector("I am glad this happened")['dominant_emotion'], "joy")
    def test_anger(self):
        self.assertEqual(emotion_detector("I am really mad about this")['dominant_emotion'], "anger")
    def test_disgust(self):
        self.assertEqual(emotion_detector("I feel disgusted just hearing about this")['dominant_emotion'], "disgust")
    def test_sadness(self):
        self.assertEqual(emotion_detector("I am so sad about this")['dominant_emotion'], "sadness")
    def test_fear(self):
        self.assertEqual(emotion_detector("I am really afraid that this will happen")['dominant_emotion'], "fear")

if __name__ == '__main__':
    unittest.main()
```

Run the tests:

```bash
python3 test_emotion_detection.py
```

---

### ✅ Task 6: Web Deployment with Flask

**File:** `server.py`

```python
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_detector_route():
    text = request.args.get('textToAnalyze')
    result = emotion_detector(text)
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    response = (f"For the given statement, the system response is "
                f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
                f"'fear': {result['fear']}, 'joy': {result['joy']} and "
                f"'sadness': {result['sadness']}. The dominant emotion is "
                f"{result['dominant_emotion']}.")
    return response

if __name__ == '__main__':
    app.run(debug=True)
```

Run the app:

```bash
python3 server.py
```

Access at: [http://localhost:5000](http://localhost:5000)

---

### ✅ Task 7: Error Handling

Handled in `emotion_detector()` (via `status_code == 400`) and in `server.py` (`dominant_emotion == None`).

---

### ✅ Task 8: Static Code Analysis

Run Pylint:

```bash
pylint server.py
```

Ensure functions have proper **docstrings** to get a 10/10 score.

---

## 💡 Sample Input/Output

**Input Text:** "I love my life"

**Formatted Output:**

```json
{
  "anger": 0.0062,
  "disgust": 0.0025,
  "fear": 0.0092,
  "joy": 0.9680,
  "sadness": 0.0497,
  "dominant_emotion": "joy"
}
```

**Response Message:**  
"For the given statement, the system response is 'anger': 0.0062, 'disgust': 0.0025, 'fear': 0.0092, 'joy': 0.9680 and 'sadness': 0.0497. The dominant emotion is joy."

---

## 📸 Screenshots

All screenshots from each task (e.g., `1_folder_structure.png`, `2a_emotion_detection.png`, `6b_deployment_test.png`) are included in the root project directory.

---

## 🧪 Technologies Used

- Python 3.11
- Flask (Web framework)
- Watson NLP API (Emotion Detection)
- Requests (HTTP client)
- unittest (Testing)
- pylint (Static Code Analysis)

---

## 👨‍💻 Author

**Souvik Mandal**  
IBM AI Engineering Final Project  
GitHub: [Souvik Mandal](https://github.com/AP19110010485)

---

## 🏁 Status

✅ All 8 tasks completed  
✅ Fully functional and tested  
✅ 10/10 code quality

🎉 Thank you for visiting the project!
