"""Flask server for the emotion detection application."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the emotion detection home page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze the emotion in the submitted text."""
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze:
        return "Invalid text! Please try again!"

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is "
        "'anger': " + str(response["anger"]) + ", "
        "'disgust': " + str(response["disgust"]) + ", "
        "'fear': " + str(response["fear"]) + ", "
        "'joy': " + str(response["joy"]) + " and "
        "'sadness': " + str(response["sadness"]) + ". "
        "The dominant emotion is " + str(response["dominant_emotion"]) + "."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    