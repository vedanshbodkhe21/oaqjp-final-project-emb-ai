"""Main server code"""

from flask import Flask, request, render_template

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def detect_emotion():
    """Main emotion detection code"""

    # Extract text from the request
    text = request.args.get('textToAnalyze')

    # Detect text emotion
    emotion_dict = emotion_detector(text)

    # Compose the final result string
    result_string = "For the given statement, the system response is "

    scores = list(emotion_dict.values())

    result_string += (
        f"'anger': {    scores[0]   }, "
        f"'disgust': {  scores[1]   }, "
        f"'fear': {     scores[2]   }, "
        f"'joy': {      scores[3]   } and "
        f"'sadness': {  scores[4]   }. "
        )

    # Dominant emotion is the last value of scores
    dominant_emotion = scores[-1]

    result_string += f"The dominant emotion is <b>{dominant_emotion}</b>."

    return result_string

@app.route("/")
def render_index_page():
    """Render homepage""" 
    return render_template('index.html')

if __name__ == '__main__':

    app.run(host='127.0.0.1', debug=True, port=5000)
