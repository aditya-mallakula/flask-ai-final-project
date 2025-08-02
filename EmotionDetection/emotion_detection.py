import json, requests

def emotion_detector(text_to_analyse):
    # Define the URL for the emotion detection API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Handle blank input or error response
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Convert the response text to a dictionary
    response_dict = json.loads(response.text)

    # Extract the required emotions and their scores
    emotions = response_dict.get('emotionPredictions', [{}])[0].get('emotion', {})
    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)

    # Find the dominant emotion
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    # If all scores are 0, treat as invalid
    if all(v == 0 for v in emotion_scores.values()):
        dominant_emotion = None
    else:
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Return the required output format
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }