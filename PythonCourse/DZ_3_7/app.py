from flask import Flask, request, jsonify
import operations

app = Flask(__name__)


@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Mini Calculator</title>
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    </head>
    <body>
        <h1>Мини-калькулятор</h1>
        <form id="calculator-form">
            <label for="num1">Число 1:</label>
            <input type="number" id="num1" name="num1" required>
            <br>
            <label for="num2">Число 2:</label>
            <input type="number" id="num2" name="num2" required>
            <br>
            <label for="operation">Операция:</label>
            <select id="operation" name="operation">
                <option value="add">Сложение</option>
                <option value="subtract">Вычитание</option>
                <option value="multiply">Умножение</option>
                <option value="divide">Деление</option>
            </select>
            <br>
            <button type="submit">Вычислить</button>
        </form>
        <h2>Результат: <span id="result"></span></h2>

        <script>
            $(document).ready(function() {
                $('#calculator-form').submit(function(event) {
                    event.preventDefault();
                    var num1 = $('#num1').val();
                    var num2 = $('#num2').val();
                    var operation = $('#operation').val();

                    $.ajax({
                        url: '/calculate',
                        type: 'POST',
                        data: { num1: num1, num2: num2, operation: operation },
                        success: function(response) {
                            $('#result').text(response.result);
                        }
                    });
                });
            });
        </script>
    </body>
    </html>
    '''


@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == 'add':
            result = operations.add(num1, num2)
        elif operation == 'subtract':
            result = operations.subtract(num1, num2)
        elif operation == 'multiply':
            result = operations.multiply(num1, num2)
        elif operation == 'divide':
            result = operations.divide(num1, num2)
        else:
            result = 'Неверная операция'

        return jsonify({'result': result})

    except ValueError:
        return jsonify({'result': 'Ошибка: Неправильный ввод данных'})


if __name__ == '__main__':
    app.run(debug=True)
