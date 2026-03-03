import sqlite3

def init(name: str):
    global database, cursor
    database = sqlite3.connect(f"{name}.db")
    cursor = database.cursor()

def run(command: str):
    cursor.execute(command)

def close():
    database.close()

def show_tables():
    tables = []
    cursor.execute("""SELECT name FROM sqlite_master WHERE type='table'""")
    unformat_tables = cursor.fetchall()
    for item in unformat_tables:
        tables.append(item[0])
    return tables

def table_exist(table: str):
    if table in show_tables():
        return "exists"
    else:
        return "no exist"

class invalid_parameter(Exception):
    pass

class table:
    def __init__(self, name, columns: list, data_types: list):
        self.name, self.columns, self.data_types = name, columns, data_types
        if len(data_types) == 1:
            temp_list = []
            for data_type in range(0, len(columns), 1):
                temp_list.append(self.data_types[0])
            self.data_types = temp_list
        elif len(columns) != len(data_types):
            raise invalid_parameter("invalid number of data types")

    def __str__(self):
        return f"Table Name: {self.name}"

    def create(self):
        query = f"CREATE TABLE {self.name} (\n"
        for i in range(0, len(self.columns), 1):
            query += f"{self.columns[i]} {self.data_types[i]}"
            if i == len(self.columns)-1:
                query += "\n)"
            else:
                query += "\n"
        run(query)
        print(query)
