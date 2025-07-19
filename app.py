from flask import Flask, render_template, request, jsonify, redirect, session, url_for
from chatbot_logic import get_bot_response

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # You can use any strong random string

@app.route('/')
def home():
    if 'user' in session:
        return redirect(url_for('chat'))
    return render_template('login.html')  # New login page

@app.route('/login', methods=['POST'])
def login():
    user_input = request.form['user_input']
    if user_input:  # In real app, validate this properly
        session['user'] = user_input
        return redirect(url_for('chat'))
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

@app.route('/chat')
def chat():
    if 'user' not in session:
        return redirect(url_for('home'))
    return render_template('chatbot.html', user=session['user'])

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json['message']
    bot_reply = get_bot_response(user_input)
    return jsonify({'reply': bot_reply})

if __name__ == '__main__':
    app.run(debug=True)

