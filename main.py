import sqlite3

conn = sqlite3.connect('Foods.db')
cur = conn.cursor()

cur.execute("SELECT Nutritious FROM Foods")
values = cur.fetchall()
values = list(map(lambda x: str(x[0]), values))
attributes = set()
for val in values:
    pieces = val.split("#")
    for piece in pieces:
        if piece != "":
            for i in piece.split("-"):
                A = i.split(" ")[:-1]
                B = " ".join(A)
                attributes.add(B)

attributes = sorted(list(attributes))


variable_string = ""
for i in attributes:
    variable_string += f"'{i}',"
variable_string = variable_string[:-1]
cur.execute("DROP TABLE IF EXISTS ProceedFoods ")
cur.execute(f"CREATE TABLE IF NOT EXISTS ProceedFoods (id INTEGER PRIMARY KEY AUTOINCREMENT,'Name','Portion Size','Calories', {variable_string})")
conn.commit()