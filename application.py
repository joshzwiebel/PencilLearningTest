from flask import Flask, render_template, request

from text_generation import generate_next_word
from text_generation import initialize

application = Flask(__name__)
application.secret_key = "Jl6EcFIbOe23EgdJ32MQ5WxmDz3bQ3L7KSDtVPij"

@application.route('/')
def index():
    return render_template('template.html', generated_text="your text will appear here")


@application.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    texty = generate_next_word(str(text))
    return render_template('template.html', generated_text=texty)


@application.before_first_request
def initiate():
    initialize()






if __name__ == '__main__':
    application.run(debug=True, use_reloader=False, host='0.0.0.0',port=5000)