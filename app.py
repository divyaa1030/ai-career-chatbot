from flask import Flask, render_template, request, jsonify
from chatbot_logic import get_bot_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat')
def chat():
    return render_template('chatbot.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json['message']
    bot_reply = get_bot_response(user_input)
    return jsonify({'reply': bot_reply})

if __name__ == '__main__':
    app.run(debug=True)
