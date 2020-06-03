from flask import Flask, render_template, request

from text_generation import generate_next_word

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('template.html', generated_text="your text will appear here")


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    texty = generate_next_word(str(text))
    return render_template('template.html', generated_text=texty)


with app.app_context():
    from text_generation import initialize

    initialize()


def run():
    app.run(debug=True, port=33507, use_reloader=False)


if __name__ == '__main__':
    run()
