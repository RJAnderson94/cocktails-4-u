import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_cocktail')
def add_cocktail():
    return render_template('addcocktail.html')


@app.route('/cocktail_page')
def cocktail_page():
    return render_template('cocktailpage.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(
        os.environ.get('PORT')), debug=True)
