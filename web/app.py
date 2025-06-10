import flask
from flask import Flask, render_template, request, jsonify
import sqlite3
import os
import lib

app = Flask(__name__)
DATABASE = "tools.db"

import os
import sqlite3

DATABASE = "tools.db"



@app.route('/')
def index():
    return render_template("index.html")


#  <---- GENERATE DATABASE ---->
@app.route('/generate-database')
def generate_database():
    return lib.generate_database()

@app.route('/add-tool', methods=['GET', 'POST'])
def add_tool():
    if request.method == "POST":
        name = request.form.get("name")
        url = request.form.get("url")
        try:
            lib.add_tool(name=name, url=url)
            return render_template("add-succes.html")
        except Exception as e:
            return jsonify({"ERROR": str(e)}), 500
    else:
        return render_template("add-tool.html")

@app.route('/get-list', methods=['GET', 'POST'])
def get_list():
    if request.method == "POST":
        data = lib.get_tools()
        return data
    elif request.method == "GET":
        query = request.form.get("query")
        if query != "" or query != " " or query != None:
            data = lib.get_tools(query=query)
        else:
            data = lib.get_tools()
        return render_template("get-list.html", data=data)

if __name__ == "__main__":
    app.run()