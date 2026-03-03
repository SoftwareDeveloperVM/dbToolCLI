import sqlite3

def init(name: str):
    global database, cursor
    database = sqlite3.connect(f"{name}.db")
    cursor = database.cursor()

def run(command: str):
    cursor.execute(command)

def close():
    database.close()

class query:
    def __init__(self, value=""):
        self.value = value
