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
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Date", "Month", "Year", "Hours Studied", "What Learned"])
    wb.save(user_data_path)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/chat', methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        user_input = request.form["message"]
        response = get_career_suggestion(user_input)
        return render_template("chatbot.html", user_input=user_input, response=response)
    return render_template("chatbot.html")

@app.route('/history')
def history():
    if 'user' in session:
        return render_template("history.html", user=session['user'])
    return redirect(url_for('login'))

@app.route('/schedule')
def schedule():
    return render_template("schedule.html")

@app.route('/daily_update', methods=["GET", "POST"])
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

    return render_template("daily_update.html")

@app.route('/reminder')
def reminder():
    # Here we’d check Excel data for missed days
    return render_template("reminder.html")

@app.route('/set_user', methods=["POST"])
def set_user():
    session['user'] = request.form["username"]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
