''' Initiates the application of emotion detector over the Flask channel deployed on localhost:5000.
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    ''' This code receives the text and runs emotion detection using emotion_detector() function. 
        The output returned shows emotions and emotion scores for the provided text.
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion:
        message = f"For the given statement, the sysytem response is 'anger': {response['anger']},"
        message += f" 'disgust': {response['disgust']}, 'fear': {response['fear']},"
        message += f"'joy': {response['joy']}, 'sadness': {response['sadness']}"
        message += f". The dominant emotion is {response['dominant_emotion']}."
        return message
    return "Invalid text! Please try again!"

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
