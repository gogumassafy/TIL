from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "안녕하세요."

@app.route('/html')
def html():
    return render_template('chicken.html')

@app.route("/html_name/<string:name>")
def html_name(name):
    return render_template("chicken.html", name = name)

@app.route("/dictionary/<string:word>")
def dictionary(word):
    dictionary_book = {"apple": "사과", "banana": "바나나"}
    return render_template("dictionary.html", dictionary_book = dictionary_book, word = word)