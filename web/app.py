import flask
from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)
DATABASE = "tools.db"

import os
import sqlite3

DATABASE = "tools.db"  # Změň na správnou cestu k tvé databázi

def get_tools(query: str = None):
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
        return f"Chyba při získávání seznamu nástrojů: {e}"


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
            return e
    else:
        return "databáze už byla vytvořena dříve"

@app.route('/add-tool', methods=['GET', 'POST'])
def add_tool():
    if request.method == "POST":
        name = request.form["name"]
        url = request.form["url"]
        try:
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO tools VALUES ({name}, {url})")
            conn.commit()
            conn.close()
        except Exception as e:
            return e

@app.route('/get-list', methods=['GET', 'POST'])
def get_list():
    if request.method == "POST":
        data = get_tools()
        return data
    elif request.method == "GET":
        data = get_tools()
        return data

if __name__ == "__main__":
    app.run()