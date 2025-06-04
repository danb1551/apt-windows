import flask
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/get-list', methods=['GET', 'POST'])
def get_list():
    if request.method == "POST":
        data = "f"
        return data
    elif request.method == "GET":
        data = "ff"
        return data

if __name__ == "__main__":
    app.run()