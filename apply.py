from main import database

db = database("test")
print(db.show_tables())

db.build_table("table", ["a", "b", "c"], ["INT", "INT", "INT"])
