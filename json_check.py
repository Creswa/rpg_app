import json

with open("skills.json", "r") as file:
    data = json.load(file)

print("Json is ok")

formatted_data = json.dumps(data, indent = 4)

data["Sex"] = {"level":2, "experience":2} #adding skill

for x in data:
    print(x)
    print(data[x]["level"])

