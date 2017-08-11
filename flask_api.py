from flask import Flask, request, session
import random

app = Flask(__name__)

numbers = []
token_dict = {
    'default': [4, 8, 15, 16, 23, 42],
    '125451': [1, 2, 3, 4, 5],
}

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/add', methods=['POST'])
def add_number():
    num = int(request.args.get('num'))
    numbers.append(num)
    return str(num)


@app.route('/sum', methods=['GET'])
def get_sum():
    token_key = request.args.get('token')
    if token_key is not None or token_key in token_dict.values():
        try:
            current = token_dict.get(token_key)
            summ = 0
            for each in current:
                summ += each
            return str(summ)
        except:
            return 'No such token'
    else:
        current = token_dict.get('default')
        summ = 0
        for each in current:
            summ += each
        return str(summ)

    # summ = 0
    # for each in numbers:
    #     summ += each
    # return str(summ)


@app.route('/count', methods=['GET'])
def get_count():
    count = 0
    for each in numbers:
        count += 1
    return str(count)


@app.route('/avg', methods=['GET'])
def get_average():
    summ = int(get_sum())
    average = summ / float(len(numbers))
    return str(average)


@app.route('/std', methods=['GET'])
def get_std_deviation():
    average = float(get_average())
    variance = 0
    for each in numbers:
        variance += (average - each) ** 2
    std_deviation = float((variance / len(numbers)) ** 0.5)
    return str(std_deviation)


@app.route('/new', methods=['GET'])
def generate_token():
    token = str(random.getrandbits(32))
    token_dict.update({token: [0]})
    # session['api_session_token'] = token
    return str(token)

if __name__ == '__main__':
    app.run()
