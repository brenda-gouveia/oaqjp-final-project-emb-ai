from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detection

app = Flask("Final Project")

@app.route("/emotionDetector")
def sent_emotion():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detection function and store the response
    response = emotion_detection(text_to_analyze)

    if response["dominant_emotion"] == None:
        return "Invalid text! Please try again!"

    text = "For the given statement, the system response is "

    emotions = []

    for chave, valor in response.items():
        if chave == "dominant_emotion":
            continue

        emotions.append(f"'{chave}': {valor}")

    text += ", ".join(emotions[:-1])
    text += f" and {emotions[-1]}"

    text += f". The dominant emotion is {response['dominant_emotion']}."

    return text

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5000)

