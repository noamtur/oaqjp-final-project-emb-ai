"""Flask server for emotion detection application."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)


@app.route('/')
def home():

    """Render the home page."""
    return render_template('index.html')


@app.route('/emotion_detector', methods=['GET', 'POST'])
def emotion_detector_endpoint():
    """Handle emotion detection requests via GET or POST."""
    if request.method == 'POST':
        data = request.get_json()
        if data is None or 'text' not in data:
            return _invalid_text_response()
        text_to_analyze = data['text']
    else:
        text_to_analyze = request.args.get('text_to_analyze', '')

    result = emotion_detector(text_to_analyze)
    dominant = result.get('dominant_emotion')

    if dominant is None:
        return _invalid_text_response()

    anger = result.get('anger')
    disgust = result.get('disgust')
    fear = result.get('fear')
    joy = result.get('joy')
    sadness = result.get('sadness')

    response_str = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy}, 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )

    return response_str, 200


def _invalid_text_response():
    """Return a consistent response for invalid or empty text."""
    return 'Invalid text! Please try again!', 200


def main():
    """Run the Flask app on port 5001."""
    app.run(port=5001, debug=False)


if __name__ == '__main__':
    main()
