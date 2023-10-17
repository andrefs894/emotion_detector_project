from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def emotion_analyzer():
    answer = request.args.get('textToAnalyze')
    emotion = emotion_detector(answer)
    if emotion['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    else:
        return "For the given statement, the system is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {}, 'sadness': {}.\nThe dominant emotion is {}.".format(emotion["anger"], emotion["disgust"], emotion["fear"], emotion["joy"], emotion["sadness"], emotion["dominant_emotion"])

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
