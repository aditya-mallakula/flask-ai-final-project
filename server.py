from flask import Flask, request, render_template, jsonify
from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detector_route():
    if request.method == 'POST':
        data = request.get_json()
        text = data.get('text', '')
    else:  # GET
        text = request.args.get('textToAnalyze', '')
    result = emotion_detector(text)
    # Format the response as per customer requirement
    response_str = (
        f"For the given statement, the system response is 'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response_str

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
