import os
import sqlite3


def __init__():
    pass

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


def filter_tools(tools: list[dict], query: str = None) -> list[tuple[str, str]]:
    new_tools = []
    for names, url in tools:
        if query in names:
            new_tuple = (names, url)
            new_tools.append(new_tuple)
    print("ff")
    return new_tools


def get_tools(query: str = None) -> list[list[str, str]]:
    data = []
    if not os.path.exists(DATABASE):
        return "Database is not here"
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        if not query:
            cursor.execute("SELECT name, url FROM tools")
            results = cursor.fetchall()
        else:
            cursor.execute("SELECT name, url FROM tools")
            results = filter_tools(cursor.fetchall(), query)
        conn.close()
        if not results:
            return "Still there are not any tool"
        return results
    except Exception as e:
        return f"Error when getting list of tools: {str(e)}"