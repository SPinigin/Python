from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
phone_regex = r'^\+79\d{2}-\d{3}-\d{2}-\d{2}$'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    email = data.get('email')
    phone = data.get('phone')

    if not re.match(email_regex, email):
        return jsonify({'status': 'error', 'message': 'Неверный формат email'})

    if not re.match(phone_regex, phone):
        return jsonify({'status': 'error', 'message': 'Неверный формат номера телефона'})

    return jsonify({'status': 'success', 'message': 'Данные успешно отправлены'})

if __name__ == '__main__':
    app.run(debug=True)
