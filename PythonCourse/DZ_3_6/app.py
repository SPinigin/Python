# app.py
from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = 'your_secret_key'

users = [
    {'login': 'user1', 'password': 'password1', 'fio': 'Иван Иванов'},
    {'login': 'user2', 'password': 'password2', 'fio': 'Петр Петров'},
]

def authenticate(login, password):
    for user in users:
        if user['login'] == login and user['password'] == password:
            return user
    return None

@app.route('/')
def index():
    fio = session.get('fio')
    if fio:
        return render_template('welcome.html', fio=fio)
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    login = request.form['login']
    password = request.form['password']

    user = authenticate(login, password)
    if user:
        session['fio'] = user['fio']
        return {'success': True, 'fio': user['fio']}
    else:
        return {'success': False}


@app.route('/logout')
def logout():
    session.pop('fio', None)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
