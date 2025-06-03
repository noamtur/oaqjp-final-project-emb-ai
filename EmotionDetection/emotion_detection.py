import requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL for the emotion detection API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Set the headers with the required model ID for the API
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Make a POST request to the API
    response = requests.post(url, json=payload, headers=headers)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extracting the emotion dictionary from the first prediction
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    # Extracting each emotion score
    anger   = emotions['anger']
    disgust = emotions['disgust']
    fear    = emotions['fear']
    joy     = emotions['joy']
    sadness = emotions['sadness']

    # Determine dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    dominant_score = emotions[dominant_emotion]

    # Returning a dictionary containing all emotion scores plus the dominant one
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion,
        'dominant_score': dominant_score
    }
