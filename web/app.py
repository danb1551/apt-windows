import flask
from flask import Flask, render_template, request, jsonify, send_file
import sqlite3
import os
import __lib__ as lib
from urllib.parse import unquote

app = Flask(__name__)
DATABASE = "tools.db"
#UPLOAD_FOLDER = os.path.join(os.getcwd(), 'tools')
UPLOAD_FOLDER = "tools"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("error/404.html"), 404

@app.route('/favicon.png')
def favicon():
    return flask.send_from_directory(os.path.join(app.root_path, 'static'),
                                     'favicon.png', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    return render_template("index.html")


#  <---- GENERATE DATABASE ---->
@app.route('/generate-database')
def generate_database():
    return lib.generate_database()


@app.route('/add-tool', methods=['GET', 'POST', 'PUT'])
def add_tool():
    if request.method == "POST":
        name = request.form.get('name')
        file = request.files.get('zipfile')

        if not name or not file:
            return jsonify({'error': 'Name, URL and ZIP file is required'}), 400

        if not file.filename.endswith('.zip'):
            return jsonify({'error': 'Must be a .zip file'}), 400

        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        try:
            #url = os.path.join("tools", file.filename)
            lib.add_tool(name=name, url=filepath)
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
        query = request.args.get("query")
        data = lib.get_tools(query=query)
        try:
            return render_template("get-list.html", data=data, query=query)
        except Exception as e:
            return render_template("get-list.html", query=query)
        


@app.route('/tools/<string:name>', methods=['GET'])
def download_tool_route(name: str):
    name = unquote(name)
    name = name.replace(".zip", "")
    path = lib.get_url_of_tool(name)
    print(path)
    if not path or not os.path.exists(os.path.join(os.getcwd(), path)):
        return "Tool not found", 404
    return send_file(os.path.join(os.getcwd(), path), as_attachment=True, download_name=os.path.basename(path))




if __name__ == "__main__":
    app.run()