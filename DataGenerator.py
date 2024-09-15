import sqlite3

conn = sqlite3.connect('Foods.db')
cur = conn.cursor()

cur.execute("SELECT * FROM Foods")
rawData = cur.fetchall()

indexes = ['Vitamin D', 'Dietary Fiber', 'Sugar', 'Calcium', 'Sodium', 'Saturated Fat',
           'Cholesterol', 'Potassium', 'Protein', 'Iron', 'Total Carbohydrate', 'Total Fat']
input_indexes = "".join(list(map(lambda x: f"'{x}',", indexes))).rstrip(",")
values = list(map(lambda x: str(x[3]), rawData))
for (rawIndex,val) in list(enumerate(values)):
    inputData = ["None"]*len(indexes)
    for i in val.split("#"):
        if i != "":
            if i.count("-") == 0:
                title = " ".join(i.split(" ")[:-1])
                amount = i.split(" ")[-1]
                index = indexes.index(title)
                inputData[index] = amount
            else:
                for j in i.split("-"):
                    title = " ".join(j.split(" ")[:-1])
                    amount = j.split(" ")[-1]
                    index = indexes.index(title)
                    inputData[index] = amount
    inputData = "".join(list(map(lambda x: f"'{x}',", inputData))).rstrip(",")
    curr_row = rawData[rawIndex][:-1]
    comm = f"INSERT INTO ProceedFoods ('Name','Portion Size','Calories',{input_indexes}) VALUES (?,?,?,{inputData})"
    cur.execute(comm, curr_row)

conn.commit()