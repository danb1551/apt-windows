import os
import sqlite3

DATABASE = "tools.db"

def generate_database() -> None:
    if not os.path.exists(DATABASE):
        try:
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE tools (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    url TEXT NOT NULL,
                    author TEXT
                );
            """)
            conn.commit()
            conn.close()
            return "Database created succesfully"
        except Exception as e:
            return str(e)
    else:
        return "Database is created before"


def add_tool(name: str, url: str) -> None:
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tools (name, url) VALUES (?, ?)", (name, url))
    conn.commit()
    conn.close()


def get_tools(query: str = None) -> list[list[str, str]]:
    data = []
    if not os.path.exists(DATABASE):
        return "Database is not here"
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        if not query:
            cursor.execute("SELECT name, url FROM tools")
        else:
            cursor.execute("SELECT name, url FROM tools WHERE name LIKE '%?%'", (query))
        results = cursor.fetchall()
        conn.close()
        for items in results:
            if query in items:
                data.append(items)
        if not results:
            return "Still there are not any tool"
        return data
    except Exception as e:
        return f"Error when getting list of tools: {str(e)}"