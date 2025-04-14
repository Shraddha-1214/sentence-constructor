import os
import json
from flask import Flask, render_template, request

app = Flask(__name__)

def load_json_data(file_path):
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Get current directory
    full_path = os.path.join(base_dir, file_path)  # Join with the filename
    print("Loading file from:", full_path)  # Debugging output
    with open(full_path, 'r', encoding='utf-8') as file:
        return json.load(file)

@app.route('/')
def index():
    data = load_json_data('sentences.json')  # File is in root directory
    questions = data['data']['questions']
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    data = load_json_data('sentences.json')
    questions = data['data']['questions']
    user_answers = {}

    for question in questions:
        question_id = question['questionId']
        selected_answers = request.form.getlist(question_id)
        user_answers[question_id] = selected_answers

    return render_template('result.html', user_answers=user_answers, questions=questions)

if __name__ == '__main__':
    app.run(debug=True)
