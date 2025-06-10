import flask
from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)
DATABASE = "tools.db"

import os
import sqlite3

DATABASE = "tools.db"  # Změň na správnou cestu k tvé databázi

def get_tools(query: str = None) -> list[list[str, str]]:
    if not os.path.exists(DATABASE):
        return "Databáze nebyla nalezena"
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        if not query:
            cursor.execute("SELECT name, url FROM tools")
        else:
            cursor.execute("SELECT name, url FROM tools WHERE name LIKE ?", (f"%{query}%",))
        results = cursor.fetchall()
        conn.close()
        if not results:
            return "Nenalezeny žádné nástroje."
        return results
    except Exception as e:
        return f"Chyba při získávání seznamu nástrojů: {str(e)}"


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/generate-database')
def generate_database():
    if not os.path.exists(DATABASE):
        try:
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE tools (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    url TEXT NOT NULL
                );
            """)
            conn.commit()
            conn.close()
            return "databáze úspěšně vytvořena"
        except Exception as e:
            return str(e)
    else:
        return "databáze už byla vytvořena dříve"

@app.route('/add-tool', methods=['GET', 'POST'])
def add_tool():
    if request.method == "POST":
        name = request.form.get("name")
        url = request.form.get("url")
        try:
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tools (name, url) VALUES (?, ?)", (name, url))
            conn.commit()
            conn.close()
            return "Nástroj byl úspěšně přidán"
        except Exception as e:
            return jsonify({"error": str(e)}), 500  # OPRAVA: výjimku převést na string/JSON
    else:
        return render_template("add-tool.html")

@app.route('/get-list', methods=['GET', 'POST'])
def get_list():
    if request.method == "POST":
        data = get_tools()
        return data
    elif request.method == "GET":
        data = get_tools()
        return render_template("get-list.html", data=data)

if __name__ == "__main__":
    app.run()