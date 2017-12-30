from flask import Flask, render_template, request, session
from random import randint

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index_get():
    return render_template('index.html')


@app.route('/textinput', methods=['POST'])
def vendorinput_post():
    data = request.form
    address = data['address']
    phone = data['phone']
    name = data['business']
    email = data['email']
    footfall = data['footfall']
    return render_template('confirmphone.html', message="Please Enter verification code here")


if __name__ == '__main__':
    app.run()
