from flask import Flask, render_template, request, redirect, url_for, session
from chatbot_logic import get_career_suggestion
import os
import openpyxl
from datetime import datetime

app = Flask(__name__)
app.secret_key = "secret123"

user_data_path = 'user_data/daily_updates.xlsx'

# Create Excel file if not exists
if not os.path.exists(user_data_path):
    os.makedirs(os.path.dirname(user_data_path), exist_ok=True)
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Date", "Month", "Year", "Hours Studied", "What Learned"])
    wb.save(user_data_path)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        session["user"] = name
        return redirect(url_for("chat"))
    return render_template("login.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        session["user"] = name
        return redirect(url_for("chat"))
    return render_template("register.html")

@app.route('/chat', methods=["GET", "POST"])
def chat():
    response = ""
    user_input = ""
    if request.method == "POST":
        user_input = request.form["message"]
        stream = request.form.get("stream", "")  # from dropdown or hidden field
        response = get_career_suggestion(user_input, stream)
    return render_template("chatbot.html", user_input=user_input, response=response)

@app.route('/history')
def history():
    if 'user' in session:
        return render_template("history.html", user=session['user'])
    return redirect(url_for('login'))

@app.route('/daily-update', methods=["GET", "POST"])
def daily_update():
    if request.method == "POST":
        date = request.form["date"]
        month = request.form["month"]
        year = request.form["year"]
        hours = request.form["hours"]
        learned = request.form["learned"]

        wb = openpyxl.load_workbook(user_data_path)
        ws = wb.active
        ws.append([date, month, year, hours, learned])
        wb.save(user_data_path)

        return redirect(url_for("daily_update"))

    return render_template("daily_update.html")

@app.route('/monthly-schedule')
def monthly_schedule():
    return render_template("monthly_schedule.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("index"))
from flask import jsonify

@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.get_json()
    message = data.get('message', '')
    stream = data.get('stream', '')
    reply = get_career_suggestion(message, stream)
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
