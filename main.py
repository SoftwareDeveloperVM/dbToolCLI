import sqlite3

def run(cursor, query):
    cursor.execute(query)

def close(database):
    database.close()

class database:
    def __init__(self, name):
        self.name, self.query = name, ""
        self.database = sqlite3.connect(f"{name}.db")
        self.cursor = self.database.cursor()

    def __str__(self):
        return f"database name: {self.name}"

    def show_tables(self):
        tables = []
        self.cursor.execute("""SELECT name FROM sqlite_master WHERE type='table'""")
        unformat_tables = self.cursor.fetchall()
        for item in unformat_tables:
            tables.append(item[0])
        return tables

    def build_table(self, name, columns: list, data_types: list):
        self.query = f"CREATE TABLE {self.name} (\n"
        for i in range(0, len(columns), 1):
            self.query += f"{columns[i]} {data_types[i]}"
            if i == len(columns) - 1:
                self.query += "\n)"
            else:
                self.query += "\n"
        run(self.cursor, self.query)
