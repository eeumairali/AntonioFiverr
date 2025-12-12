from flask import Flask, render_template
from helper import generate_random_string

app = Flask(__name__)


@app.route('/')
def home():
    random_string = generate_random_string()
    return render_template('index.html', random_string=random_string)



app.run(debug=True)


