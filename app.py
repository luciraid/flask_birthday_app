from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# List of responses
responses = {
    "sarcastic": [
        "Oh sure, because that's what I do best: sarcasm.",
        "Right, like I haven't heard that one before.",
        "Wow, you must have a degree in Captain Obvious."
    ],
    "compliment": [
        "You have a great sense of humor!",
        "You're really insightful.",
        "You have a wonderful smile."
    ],
    "motivational": [
        "Keep going, you're doing amazing!",
        "Believe in yourself and all that you are.",
        "Every day is a new opportunity."
    ],
    "heartfelt": [
        "Thank you for being such a great friend.",
        "I truly appreciate having you in my life.",
        "Your presence brings me joy every day."
    ]
}

# Index route
@app.route('/')
def index():
    return render_template('index.html')

# Get response route
@app.route('/get_response', methods=['POST'])
def get_response():
    message_type = request.json.get('type', '')
    response = random.choice(responses.get(message_type, ["Sorry, I don't have a response for that."]))
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)



