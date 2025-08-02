"""
Flask server for emotion detection web application.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detector_route():
    """
    Route for emotion detection. Accepts GET and POST requests.
    Returns formatted string with emotion scores and dominant emotion.
    Handles blank/invalid input.
    """
    if request.method == 'POST':
        data = request.get_json()
        text = data.get('text', '')
    else:
        text = request.args.get('textToAnalyze', '')
    result = emotion_detector(text)
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    response_str = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} "
        f"and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response_str

@app.route('/')
def index():
    """
    Render the main index.html page.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
