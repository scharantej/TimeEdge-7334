
# main.py
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/schedule')
def schedule():
    tasks = [
        {'name': 'Task 1', 'time': '9:00 AM - 10:00 AM'},
        {'name': 'Task 2', 'time': '10:00 AM - 11:00 AM'},
        {'name': 'Task 3', 'time': '11:00 AM - 12:00 PM'},
    ]
    return render_template('schedule.html', tasks=tasks)

@app.route('/tracking')
def tracking():
    return render_template('tracking.html')

@app.route('/workspace')
def workspace():
    return render_template('workspace.html')

if __name__ == '__main__':
    app.run(debug=True)
