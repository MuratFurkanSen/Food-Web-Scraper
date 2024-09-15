input_file = open("data.txt", "r")
output_file = open("FoodNames.txt", "w")
List = list()
for line in input_file:
    for i in line.split():
        if i not in List:
            List.append(i)
for i in List:
    if (i != "or" and i!= "a" and i != "in" and i != "of" and i != "for"):
        output_file.write(i + "\n")